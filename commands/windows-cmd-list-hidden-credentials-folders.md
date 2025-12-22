---
id: e712a6c1-7f04-4e6e-a92f-215c2a940737
name: windows-cmd-list-hidden-credentials-folders
type: command
executor: cmd
data: >-
  dir /a:h C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\*\ndir /a:h
  C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Credentials\*\
output: null
created_at: '2023-04-06T03:56:26.245204+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - dpapi
  - enumeration
verified: true
validated: true
---

# windows-cmd-list-hidden-credentials-folders

## Command

```cmd
dir /a:h C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\*
dir /a:h C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Credentials\*\
```

## Description

This command uses the Windows Command Prompt to list all hidden files and directories in the DPAPI Credentials folders for both local and roaming user profiles. It is useful for initial reconnaissance of encrypted credential storage locations during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The target Windows username (e.g., 'john.doe') | Yes |
| /a:h | Display only hidden files and directories | Built-in |
| * | Wildcard to list contents recursively if needed | Built-in |

## Examples

### Basic Usage

```cmd
dir /a:h C:\Users\john.doe\AppData\Local\Microsoft\Credentials\*
```

### Advanced Usage

```cmd
dir /a:h C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\* | findstr .cred
```

This filters output to show only .cred files.

## Expected Output

```
 Volume in drive C is Windows
 Volume Serial Number is 1234-5678

 Directory of C:\Users\john.doe\AppData\Local\Microsoft\Credentials

2023/04/06  10:30    <DIR>          .
2023/04/06  10:30    <DIR>          ..
2023/04/06  09:45             1,024 Credentials_ABC123-DEF4-5678-9ABC-DEF123456789.cred
               1 File(s)          1,024 bytes

 Directory of C:\Users\john.doe\AppData\Roaming\Microsoft\Credentials

2023/04/06  10:30    <DIR>          .
2023/04/06  10:30    <DIR>          ..
2023/04/06  09:45             2,048 Credentials_XYZ789-GHI0-JKL1-MNO2-PQR345678901.cred
               1 File(s)          2,048 bytes
```

Success is indicated by the presence of .cred files, which are DPAPI-encrypted credential blobs.

## Related

- [[procedures/Windows-DPAPI-Credential-Files-Enumeration]]
- [[commands/powershell-list-hidden-credentials-folders]]

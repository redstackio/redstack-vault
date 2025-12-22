---
id: 589b3bbc-3d84-4da4-a72a-8c03b590a697
name: dir-list-user-credentials-folder
type: command
executor: cmd
data: 'dir C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\*'
output: null
created_at: '2023-04-06T03:56:27.473425+00:00'
updated_at: '2023-04-10T20:37:18.798330+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - enumeration
verified: true
validated: true
---

# dir-list-user-credentials-folder

## Command

```cmd
dir C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\*
```

## Description

This command lists all encrypted credential files in the user's Credential Manager directory, helping identify targets for DPAPI extraction. Use it as the first step to discover stored credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target Windows username (e.g., 'john.doe') | Yes |

## Examples

### Basic Usage

```cmd
dir C:\Users\john.doe\AppData\Local\Microsoft\Credentials\*
```

### Advanced Usage

```cmd
dir /b C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\*
```

## Expected Output

```
 Directory of C:\Users\john.doe\AppData\Local\Microsoft\Credentials

[date]  [time]    <DIR>          .
[date]  [time]    <DIR>          ..
[date]  [time]             1,024 2647629F5AA74CD934ECD2F88D64ECD0
               1 File(s)          1,024 bytes
```

## Related

- [[procedures/Credential-Theft-with-Mimikatz-and-DPAPI]]
- [[tools/Mimikatz]]

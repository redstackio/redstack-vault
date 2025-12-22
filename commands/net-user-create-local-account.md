---
type: command
executor: cmd
data: net user $_USERNAME $_PASSWORD /add /Y
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - account-creation
verified: true
validated: true
---

# net-user-create-local-account

## Command

```cmd
net user $_USERNAME $_PASSWORD /add /Y
```

## Description

Creates a new local user account on a Windows system using the built-in net command. This is useful for establishing persistence by adding a backdoor account during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The desired username for the new account (e.g., hacker) | Yes |
| $_PASSWORD | The password for the account (e.g., Hcker_12345678*) | Yes |
| /add | Adds the user to the system | Built-in |
| /Y | Suppresses the "Are you sure?" prompt | Built-in |

## Examples

### Basic Usage

```cmd
net user hacker Hcker_12345678* /add /Y
```

### Advanced Usage

```cmd
net user backupuser Passw0rd123 /add /Y
```

## Expected Output

The command completed successfully.

If the account already exists: "The user name could not be found" or similar error.

## Related

- [[procedures/windows-credential-enumeration]]
- [[commands/net-localgroup-add-to-administrators]]

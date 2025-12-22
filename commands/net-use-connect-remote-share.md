---
type: command
executor: cmd
data: 'net use \\TARGET_HOSTNAME\SHARE_NAME /user:DOMAIN\USERNAME PASSWORD'
tags:
  - lateral-movement
  - smb
  - windows
platforms:
  - Windows
verified: true
validated: true
---

# net-use-connect-remote-share

## Command

```cmd
net use \\TARGET_HOSTNAME\SHARE_NAME /user:DOMAIN\USERNAME PASSWORD
```

## Description

This command connects a local Windows system to a remote network share using SMB protocol and provided credentials. It is commonly used in lateral movement to access administrative shares (e.g., C$, ADMIN$) on target Windows hosts, enabling file read/write operations without full remote execution rights.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `\\TARGET_HOSTNAME` | UNC path prefix with target hostname or IP (e.g., \\srv01.domain.local) | Yes |
| `SHARE_NAME` | Name of the remote share (e.g., C$ for system drive) | Yes |
| `/user:DOMAIN\USERNAME` | Domain-qualified username for authentication | Yes |
| `PASSWORD` | Plaintext password for the user | Yes |
| `/persistent:yes` (optional) | Makes the connection persistent across reboots | No |

## Examples

### Basic Usage

Connect to C$ share on a domain-joined server:

```cmd
net use \\srv01.domain.local\C$ /user:CONTOSO\adminuser MyPass123
```

### Advanced Usage

Connect with persistence and save credentials for reuse:

```cmd
net use \\10.0.0.50\IPC$ /user:LOCAL\user /savecred /persistent:yes
```

## Expected Output

Successful execution:
```
The command completed successfully.
```

Error for invalid credentials:
```
System error 1326 has occurred.

The user name or password is incorrect.
```

List active connections with `net use` to verify.

## Related

- [[Related Procedure]]: [[procedures/Connect-to-Windows-Remote-Share]]
- [[Related Command]]: [[commands/net-use-delete-connection]]

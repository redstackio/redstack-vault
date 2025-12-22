---
type: command
executor: command_prompt
data: 'net use $_DRIVE: \\$_TARGET_IP\$_SHARE_NAME'
output: The command completed successfully.
platforms:
  - Windows
tags:
  - network
  - smb
  - post-exploitation
verified: true
validated: true
---

# mount-remote-smb-share

## Command

```command_prompt
net use $_DRIVE: \\$_TARGET_IP\$_SHARE_NAME
```

## Description

This command maps a remote SMB share to a local drive letter on a Windows system, allowing access to files on a remote server. It's useful in post-exploitation for data exfiltration or lateral movement when credentials are available or null sessions are permitted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DRIVE | Local drive letter to assign (e.g., Z) | Yes |
| $_TARGET_IP | IP address or hostname of the remote server | Yes |
| $_SHARE_NAME | Name of the SMB share on the remote server | Yes |
| `/user:$_USERNAME` | Optional: Specify username for authentication | No |
| `/password:$_PASSWORD` | Optional: Specify password for authentication | No |

## Examples

### Basic Usage

Mount a share without credentials (null session):

```command_prompt
net use Z: \\10.10.10.100\files
```

### Advanced Usage

Mount with credentials:

```command_prompt
net use Z: \\10.10.10.100\files /user:domain\admin password123
```

## Expected Output

```
C:\>net use Z: \\10.10.10.100\files
The command completed successfully.
```

If successful, the drive appears in File Explorer or via `dir Z:`. Errors like "System error 5 has occurred. Access is denied." indicate permission issues.

## Related

- [[Related Procedure: Access-Remote-Share-via-Net-Use]]
- [[tools/net-windows]]

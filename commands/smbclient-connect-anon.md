---
id: cmd-uuid-003
data: smbclient //target-ip/CCTV-Backup -N
tags:
  - access
  - smb
type: command
output: null
executor: bash
platforms:
  - Linux
  - SMB
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.656Z'
verified: false
validated: true
submitted: true
---
# smbclient-connect-anon

## Command

```bash
smbclient //target-ip/CCTV-Backup -N
```

## Description

Connects to an SMB share anonymously to access files without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `//target-ip/share` | Target server and share path | Yes |
| `-N` | Null session (no password) | Yes |

## Examples

### Basic Usage

```bash
smbclient //192.168.1.100/IPC$ -N
```

### Advanced Usage

```bash
smbclient //target-ip/CCTV-Backup -N -c 'ls'
```

## Expected Output

Interactive smb: \> prompt for file operations.

## Related

- [[Related Procedure: Access-SMB-Shares-Without-Authentication]]

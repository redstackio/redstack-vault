---
id: cmd-uuid-002
data: smbclient -L //target-ip -N
tags:
  - enumeration
  - smb
type: command
output: null
executor: bash
platforms:
  - Linux
  - SMB
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.660Z'
verified: false
validated: true
submitted: true
---
# smbclient-enum-shares

## Command

```bash
smbclient -L //target-ip -N
```

## Description

Enumerates available SMB shares on a target host using an anonymous (null) session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | List shares | Yes |
| `//target-ip` | Target SMB server | Yes |
| `-N` | No password (anonymous) | Yes |

## Examples

### Basic Usage

```bash
smbclient -L //192.168.1.100 -N
```

### Advanced Usage

```bash
smbclient -L //target-ip -N -U guest
```

## Expected Output

List of sharename, type, and description, e.g., 'Sharename: CCTV-Backup Type: Disk'.

## Related

- [[Related Procedure: Discover-Exposed-SMB-Servers]]

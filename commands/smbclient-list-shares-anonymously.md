---
id: 8a9f6edb-60bb-431a-8420-686425fe923f
type: command
executor: bash
data: smbclient -L $_TARGET -N
output: null
created_at: '2023-04-06T03:56:03.238680+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
  - enumeration
verified: true
validated: true
---

# smbclient-list-shares-anonymously

## Command

```bash
smbclient -L $_TARGET -N
```

## Description

This command lists available SMB shares on a target host anonymously, without providing credentials. It is useful for initial reconnaissance to identify accessible shares like IPC$, ADMIN$, or user-created shares on Windows systems running SMB services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -L | List shares of the target server | Yes |
| -N | No password (anonymous access) | Yes |
| $_TARGET | Target hostname or IP address (e.g., 192.168.1.100 or hostname) | Yes |

## Examples

### Basic Usage

```bash
smbclient -L 192.168.1.100 -N
```

### Advanced Usage

```bash
smbclient -L //target.domain.com -N
```

## Expected Output

```
Sharename       Type      Comment
---------       ----      -------
ADMIN$          Disk      Remote Admin
C$              Disk      Default share
IPC$            IPC       Remote IPC
Users           Disk      Default share
```

This output shows available shares, their types (Disk for file shares, IPC for inter-process communication), and comments. Anonymous access may be limited based on server configuration.

## Related

- [[tools/smbclient]]
- [[procedures/SMB-Share-Enumeration]]

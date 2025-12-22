---
id: 07f3bebc-8d60-45ae-ae78-0741b4d11041
name: net-time-sync-to-dc
type: command
executor: bash
data: net time set -S $_DC_IP
output: 'root@kali:~# net time set -S 10.10.10.5'
created_at: '2020-06-24T05:08:26.192653+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - time-sync
  - smb
verified: true
validated: true
---

# net-time-sync-to-dc

## Command

```bash
net time set -S $_DC_IP
```

## Description

This command synchronizes the local system's clock to a remote Windows system's time via anonymous SMB, ensuring Kerberos tolerance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -S $_DC_IP | DC IP address to sync from | Yes |

## Examples

### Basic Usage

```bash
net time set -S 10.10.10.5
```

### Advanced Usage

Sync with verbose output:
```bash
net time -S 192.168.1.10
```

## Expected Output

Confirms time set; may show current time difference.

```
root@kali:~# net time set -S 10.10.10.5
```

## Related

- [[procedures/Create-Golden-Ticket-and-Launch-Windows-SYSTEM-Shell-from-Linux]]

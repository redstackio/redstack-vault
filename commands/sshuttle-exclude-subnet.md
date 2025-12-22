---
id: 4bcd9541-ae85-417d-8b27-423e91f71af4
name: sshuttle-exclude-subnet
type: command
executor: bash
data: sshuttle -vvr $_USER@$_PIVOT_HOST $_SUBNET -x $_EXCLUDE_SUBNET
output: null
created_at: '2023-04-06T03:56:22.695058+00:00'
updated_at: '2023-04-10T20:25:19.583732+00:00'
platforms:
  - Linux
tags:
  - pivoting
  - sshuttle
  - exclude
verified: true
validated: true
---

# sshuttle-exclude-subnet

## Command

```bash
sshuttle -vvr $_USER@$_PIVOT_HOST $_SUBNET -x $_EXCLUDE_SUBNET
```

## Description

Sets up an sshuttle tunnel while excluding specific subnets from being routed through it, preventing interference with local traffic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -vv | Verbose mode | No |
| -r | Remote host | Yes |
| $_USER | Username | Yes |
| $_PIVOT_HOST | Pivot host | Yes |
| $_SUBNET | Primary subnet to tunnel | Yes |
| -x | Exclude subnet from tunnel | Yes |
| $_EXCLUDE_SUBNET | Subnet to bypass (e.g., 192.168.1.0/24) | Yes |

## Examples

### Basic Usage

```bash
sshuttle -vvr user@10.10.10.10 10.1.1.0/24 -x 192.168.1.0/24
```

### Advanced Usage

Exclude multiple:

```bash
sshuttle -vvr user@10.10.10.10 10.1.1.0/24 -x 192.168.1.0/24 -x 10.0.0.0/8
```

## Expected Output

"Excluding 192.168.1.0/24 from tunnel\nTunnel established for 10.1.1.0/24\nLocal traffic routed directly"

## Related

- [[procedures/network-pivoting-with-sshuttle]]
- [[tools/sshuttle]]

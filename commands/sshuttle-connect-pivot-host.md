---
id: 2c5118ab-f1be-422a-bcee-3069774bebc2
name: sshuttle-connect-pivot-host
type: command
executor: bash
data: sshuttle -vvr $_USERNAME@$_PIVOT_HOST $_TARGET_SUBNET
output: null
created_at: '2023-04-06T03:56:22.694948+00:00'
updated_at: '2023-04-10T20:25:19.583732+00:00'
platforms:
  - Linux
tags:
  - pivoting
  - sshuttle
  - connect
verified: true
validated: true
---

# sshuttle-connect-pivot-host

## Command

```bash
sshuttle -vvr $_USERNAME@$_PIVOT_HOST $_TARGET_SUBNET
```

## Description

Connects to a pivot host using a hostname variable and tunnels traffic to a specific internal subnet. Useful when the pivot is referenced dynamically.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -vv | Verbose output (detailed) | No |
| -r | Remote host specification | Yes |
| $_USERNAME | SSH username | Yes |
| $_PIVOT_HOST | Pivot hostname or IP | Yes |
| $_TARGET_SUBNET | Subnet to forward (e.g., 10.2.2.0/24) | Yes |

## Examples

### Basic Usage

```bash
sshuttle -vvr username@pivot_host 10.2.2.0/24
```

### Advanced Usage

Combine with method override:

```bash
sshuttle -vvr username@pivot_host 10.2.2.0/24 -M udp
```

## Expected Output

"sshuttle: info: starting VPN on tun0\nsshuttle: info: SSH connection established\nForwarding traffic for 10.2.2.0/24"

## Related

- [[procedures/network-pivoting-with-sshuttle]]
- [[tools/sshuttle]]

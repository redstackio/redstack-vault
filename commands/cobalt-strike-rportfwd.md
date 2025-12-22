---
id: d0ad88d6-7733-4c58-acc7-7c774b12c5ad
name: cobalt-strike-rportfwd
type: command
executor: bash
data: beacon > rportfwd $_BIND_PORT $_FORWARD_HOST $_FORWARD_PORT
output: null
created_at: '2023-04-06T03:56:16.576379+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - port-forward
verified: true
validated: true
---

# cobalt-strike-rportfwd

## Command

```bash
beacon > rportfwd $_BIND_PORT $_FORWARD_HOST $_FORWARD_PORT
```

## Description

Binds to a port on the Beacon host and forwards incoming connections to a remote host and port, enabling access to internal services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BIND_PORT | Port to listen on Beacon host (e.g., 8080) | Yes |
| $_FORWARD_HOST | Internal IP/hostname to forward to | Yes |
| $_FORWARD_PORT | Port on forward host (e.g., 445 for SMB) | Yes |

## Examples

### Basic Usage

```bash
beacon > rportfwd 8080 192.168.1.100 445
```

## Expected Output

Console: "[*] Request 1 forwarded to 192.168.1.100:445". Successful connections show traffic in logs.

## Related

- [[procedures/Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]

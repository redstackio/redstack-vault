---
id: 8de9130a-21f7-4aeb-8225-bf4c6ac7f70e
name: plink-forward-port-to-vps
type: command
executor: bash
data: 'plink -R $_REMOTE_PORT:localhost:$_LOCAL_PORT $_VPS_IP'
output: null
created_at: '2023-04-06T03:56:23.000085+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - network-pivoting
  - ssh-forwarding
  - vps
verified: true
validated: true
---

# plink-forward-port-to-vps

## Command

```bash
plink -R $_REMOTE_PORT:localhost:$_LOCAL_PORT $_VPS_IP
```

## Description

Forwards a local port to a remote port on a VPS via SSH, useful for chaining pivots or accessing services through a cloud intermediary.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -R $_REMOTE_PORT:localhost:$_LOCAL_PORT | Remote forward mapping (e.g., 445:localhost:445) | Yes |
| $_VPS_IP | VPS IP or hostname | Yes |
| -l $_USERNAME | SSH username (default if omitted) | No |
| -pw $_PASSWORD | SSH password | No |

## Examples

### Basic Usage

```bash
plink -R 445:localhost:445 203.0.113.1
```

### Advanced Usage

```bash
plink -l user -pw pass -R 445:localhost:445 203.0.113.1
```

## Expected Output

```
Access granted
Forwarded ports: localhost:$_LOCAL_PORT
```
Verify by connecting to VPS IP on $_REMOTE_PORT.

## Related

- [[procedures/Network-Pivoting-with-Plink-Port-Forwarding]]
- [[tools/Plink]]

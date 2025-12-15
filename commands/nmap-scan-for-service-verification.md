---
data: 'nmap -sS -p 22,53,67,80,443 TARGET_NETWORK'
tags:
  - scan
  - dos
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.319Z'
id: ead4c7a8-f0f7-46e4-aa6f-d7e3191c6cd6
verified: false
validated: true
submitted: true
---
# Nmap-Scan-for-Service-Verification

## Command

```bash
nmap -sS -p 22,53,67,80,443 192.168.1.0/24
```

## Description

Performs a SYN scan on key ports to verify open status post-DoS, where ports show open but services fail to respond.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -sS | SYN scan for stealth | Yes |
| -p | Ports to scan (22 SSH, 53 DNS, 67 DHCP, 80 HTTP, 443 HTTPS) | Yes |
| TARGET_NETWORK | Network range (e.g., 192.168.1.0/24) | Yes |

## Examples

### Basic Usage

```bash
nmap -sS -p 53,67,80,443 192.168.1.1
```

### Advanced Usage

```bash
nmap -sS -p- -T4 192.168.1.0/24 -oN dos_verify.txt
```

## Expected Output

Nmap output showing ports open on router (e.g., 192.168.1.1:53/tcp open domain, 80/tcp open http), but subsequent connection tests fail due to DoS.

## Related

- [[Related Procedure: Verify-DoS-with-Nmap-Scan]]

---
id: b97cfb88-e3d3-4a13-a0ca-4953086946ea
name: scan-for-vulnerabilities
type: command
executor: bash
data: nmap -sS -A $_MALICIOUS_HOST
output: null
created_at: '2023-04-06T03:56:31.693477+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - recon
verified: true
validated: true
---

# scan-for-vulnerabilities

## Command

```bash
nmap -sS -A $_MALICIOUS_HOST
```

## Description

Performs a comprehensive SYN scan with OS detection, version scanning, and script execution on the malicious host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -sS | SYN scan | Yes |
| -A | Aggressive scan (OS, version, scripts) | Yes |
| $_MALICIOUS_HOST | Target | Yes |

## Examples

### Basic Usage

```bash
nmap -sS -A evil-website.tld
```

## Expected Output

Host OS: Linux 5.x
PORT   STATE SERVICE VERSION
80/tcp open  http   Apache httpd 2.4.41

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/port-scan]]

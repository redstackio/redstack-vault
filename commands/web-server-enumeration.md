---
id: 16e2ef41-2ce4-4128-8be4-809e2a478223
name: web-server-enumeration
type: command
executor: bash
data: 'nmap -sV -p80,443 $_MALICIOUS_HOST'
output: null
created_at: '2023-04-06T03:56:31.692950+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - recon
  - web
verified: true
validated: true
---

# web-server-enumeration

## Command

```bash
nmap -sV -p80,443 $_MALICIOUS_HOST
```

## Description

Enumerates web server versions on standard HTTP/HTTPS ports of the malicious host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -sV | Service version detection | Yes |
| -p80,443 | Ports to scan | Yes |
| $_MALICIOUS_HOST | Target host | Yes |

## Examples

### Basic Usage

```bash
nmap -sV -p80,443 evil-website.tld
```

## Expected Output

PORT    STATE SERVICE VERSION
80/tcp  open  http     Apache httpd 2.4.41
443/tcp open  https    Apache httpd 2.4.41 (SSL)

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/directory-brute-force]]

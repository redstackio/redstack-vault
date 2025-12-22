---
id: edcf54db-2ead-418e-ba9c-c69971d63816
name: port-scan
type: command
executor: bash
data: nmap -p- $_MALICIOUS_HOST
output: null
created_at: '2023-04-06T03:56:31.692856+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - recon
verified: true
validated: true
---

# port-scan

## Command

```bash
nmap -p- $_MALICIOUS_HOST
```

## Description

Scans all ports on the malicious host to identify open services for hosting phishing content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p- | Scan all 65535 ports | Yes |
| $_MALICIOUS_HOST | Target host | Yes |

## Examples

### Basic Usage

```bash
nmap -p- evil-website.tld
```

## Expected Output

PORT   STATE SERVICE
80/tcp open  http
443/tcp open https

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/web-server-enumeration]]

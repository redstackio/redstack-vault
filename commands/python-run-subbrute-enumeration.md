---
type: command
executor: bash
data: python subbrute.py $_DOMAIN
tags:
  - recon
  - dns
  - enumeration
platforms:
  - Linux
verified: true
validated: true
---

# python-run-subbrute-enumeration

## Command

```bash
python subbrute.py $_DOMAIN
```

## Description

This command runs the Subbrute Python script to brute-force enumerate subdomains of the specified target domain by querying DNS for common subdomain names.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The target domain to enumerate (e.g., example.com) | Yes |
| python | Python interpreter (assumes Python 2/3 is installed) | Yes |
| subbrute.py | The main script file from the cloned repository | Yes |

## Examples

### Basic Usage

```bash
python subbrute.py example.com
```

### Advanced Usage

Run from the subbrute directory: `cd subbrute && python subbrute.py example.com`. For verbose output, check tool documentation if flags are added.

## Expected Output

Subbrute v1.0 - DNS Subdomain Brute Forcer

Target: example.com

Valid Subdomains:
www.example.com
mail.example.com
admin.example.com
ftp.example.com

(Or 'No valid subdomains found' if none match.)

## Related

- [[procedures/Subdomain-Enumeration-Using-Subbrute]]
- [[tools/Subbrute]]

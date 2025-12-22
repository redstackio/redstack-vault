---
type: command
executor: bash
data: python3 sublist3r.py -b -d $_DOMAIN
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - reconnaissance
  - subdomain-enumeration
verified: true
validated: true
---

# sublist3r-bruteforce-enumeration

## Command

```bash
python3 sublist3r.py -b -d $_DOMAIN
```

## Description

This command runs Sublist3r with the brute-force module enabled to actively enumerate subdomains by testing a built-in wordlist against the target's DNS records. Use it when passive OSINT yields incomplete results, but note it generates more network traffic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -b | Enable brute-force mode using default wordlist | Yes |
| -d $_DOMAIN | Target domain to enumerate (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
python3 sublist3r.py -b -d example.com
```

### Save Output

```bash
python3 sublist3r.py -b -d example.com > subdomains_bruteforce.txt
```

## Expected Output

[-] Searching subdomains on https://crt.sh for example.com
mail.example.com
www.example.com
ftp.example.com
admin.example.com

Total subdomains found: 15

## Related

- [[procedures/Sublist3r-Subdomain-Enumeration]]
- [[tools/Sublist3r]]

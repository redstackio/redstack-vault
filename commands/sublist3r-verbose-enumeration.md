---
type: command
executor: bash
data: python3 sublist3r.py -v -d $_DOMAIN
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

# sublist3r-verbose-enumeration

## Command

```bash
python3 sublist3r.py -v -d $_DOMAIN
```

## Description

This command performs subdomain enumeration with verbose output, displaying results in real-time as they are discovered from default search engines and sources. Ideal for monitoring progress during long-running scans.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Enable verbose mode for real-time output | Yes |
| -d $_DOMAIN | Target domain to enumerate (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
python3 sublist3r.py -v -d example.com
```

### With Output Redirection

```bash
python3 sublist3r.py -v -d example.com | tee subdomains_verbose.txt
```

## Expected Output

INFO: Starting enumeration for example.com
[-] Enumerating using Google
api.example.com
blog.example.com
[-] Enumerating using Bing
shop.example.com

## Related

- [[procedures/Sublist3r-Subdomain-Enumeration]]
- [[tools/Sublist3r]]

---
type: command
executor: bash
data: python3 sublist3r.py -e $_ENGINES -d $_DOMAIN
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

# sublist3r-specific-engines-enumeration

## Command

```bash
python3 sublist3r.py -e $_ENGINES -d $_DOMAIN
```

## Description

This command limits subdomain enumeration to specific search engines or services, allowing focused queries to avoid rate limits or prioritize reliable sources like VirusTotal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -e $_ENGINES | Comma-separated list of engines (e.g., google,yahoo,virustotal) | Yes |
| -d $_DOMAIN | Target domain to enumerate (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
python3 sublist3r.py -e google,yahoo -d example.com
```

### With Multiple Engines

```bash
python3 sublist3r.py -e virustotal,netcraft,threatcrowd -d example.com > targeted_subdomains.txt
```

## Expected Output

[-] Enumerating using google for example.com
dev.example.com
test.example.com
[-] Enumerating using yahoo for example.com
mail.example.com

Total: 8 subdomains

## Related

- [[procedures/Sublist3r-Subdomain-Enumeration]]
- [[tools/Sublist3r]]

---
type: command
executor: bash
data: theharvester -b all -d $_TARGET_DOMAIN -f output.html
output: null
platforms:
  - Linux
tags:
  - reconnaissance
  - osint
verified: true
validated: true
---

# theHarvester Domain Reconnaissance All Sources

## Command

```bash
theharvester -b all -d $_TARGET_DOMAIN -f output.html
```

## Description

This command uses theHarvester to gather emails, subdomains, hosts, and IPs from multiple public sources for a target domain, enabling passive OSINT collection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -b all | Use all available sources (Google, Bing, etc.) | Yes |
| -d $_TARGET_DOMAIN | Target domain to harvest | Yes |
| -f output.html | Save results to HTML file | No |

## Examples

### Basic Usage

```bash
theharvester -b all -d example.com
```

### Advanced Usage (Limit Sources)

```bash
theharvester -b google,linkedin -d example.com -l 500
```

## Expected Output

Console summary and HTML report:

```
[*] Target: example.com
Emails found: 15
  user@example.com
Subdomains found: 5
  mail.example.com
Hosts found: 3
  192.168.1.1
```

## Related

- [[procedures/passive-reconnaissance-information-gathering]]
- [[tools/theHarvester]]

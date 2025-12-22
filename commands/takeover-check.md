---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: takeover -l subdomains.txt --output results.txt
tags:
  - takeover
  - vulnerability-scan
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.637Z'
verified: false
validated: true
submitted: true
---
# takeover-check

## Command

```bash
takeover -l subdomains.txt --output results.txt
```

## Description

This command scans a list of subdomains for takeover vulnerabilities by checking against known service fingerprints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Input file of subdomains | Yes |
| `--output` | Output file for results | Yes |

## Examples

### Basic Usage

```bash
takeover -l subdomains.txt --output results.txt
```

### Advanced Usage

```bash
takeover -l subdomains.txt --threads 50 --output results.txt
```

## Expected Output

Report file listing vulnerable subdomains, e.g., 'vex.weather.com: vulnerable to Heroku takeover'.

## Related

- [[Related Procedure: Detect-and-Exploit-Subdomain-Takeover]]

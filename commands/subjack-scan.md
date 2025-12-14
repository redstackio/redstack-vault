---
id: c2e3f4g5-h6i7-8902-efgh-5678901234
data: subjack -w subdomains.txt -t 100 -timeout 30 -o results.txt -ssl -v
tags:
  - subdomain-takeover
  - scanning
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:10.616Z'
verified: false
validated: true
submitted: true
---
# subjack-scan

## Command

```bash
subjack -w subdomains.txt -t 100 -timeout 30 -o results.txt -ssl -v
```

## Description

Scans a list of subdomains for takeover vulnerabilities by checking against fingerprints of popular cloud services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w subdomains.txt` | Input file of subdomains | Yes |
| `-t 100` | Number of threads | No |
| `-timeout 30` | Request timeout in seconds | No |
| `-o results.txt` | Output file | Yes |
| `-ssl` | Enable SSL checks | No |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
subjack -w subs.txt -o output.txt
```

### Advanced Usage

```bash
subjack -w subs.txt -t 200 -timeout 45 -o results.json -format json
```

## Expected Output

List of vulnerable subdomains, e.g., '[Vulnerable] subdomain.mozaws.net -> heroku'.

## Related

- [[Related Procedure|procedures/Discover-Dangling-DNS-Records]]

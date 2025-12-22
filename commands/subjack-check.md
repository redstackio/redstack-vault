---
data: subjack -w subdomains.txt -t 100 -o takeovers.txt -v
tags:
  - takeover
  - dns
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.501Z'
id: 3be38e3f-115f-42c1-9aea-c44fc761af15
verified: false
validated: true
submitted: true
---
# subjack-check

## Command

```bash
subjack -w subdomains.txt -t 100 -o takeovers.txt -v
```

## Description

Scans a list of subdomains for takeover vulnerabilities by checking fingerprints of cloud services like AWS, Heroku.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w` | Input wordlist file | Yes |
| `-t` | Threads | No |
| `-o` | Output file | Yes |
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
subjack -w subs.txt -o results.txt
```

### Advanced Usage

```bash
subjack -w subdomains.txt -t 200 -o takeovers.txt -v -ssl
```

## Expected Output

Console output and file with vulnerable subdomains, e.g., [Vulnerable] germany.openapi.starbucks.com - AWS.

## Related

- [[Related Procedure: Identify-Vulnerable-Subdomains-for-Takeover]]

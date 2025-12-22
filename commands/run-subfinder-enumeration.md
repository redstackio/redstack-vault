---
id: 0e58adfd-1f5b-4c64-b8ac-977860dcb368
name: run-subfinder-enumeration
type: command
executor: bash
data: subfinder -d $_DOMAIN -o $_OUTPUT_FILE -silent -t 50
output: null
created_at: '2023-04-06T03:56:25.499594+00:00'
updated_at: '2023-04-10T20:25:39.525193+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - recon
verified: true
validated: true
---

# run-subfinder-enumeration

## Command

```bash
subfinder -d $_DOMAIN -o $_OUTPUT_FILE -silent -t 50
```

## Description

This command runs Subfinder to enumerate subdomains for a specified domain, querying passive sources and writing unique results to an output file. Use it during reconnaissance to passively discover subdomains without alerting the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Target domain to enumerate (e.g., example.com) | Yes |
| -o $_OUTPUT_FILE | Path to output file for results (e.g., /tmp/subdomains.txt) | Yes |
| -silent | Suppress progress output for cleaner logs | No |
| -t 50 | Number of threads for concurrent queries (default 10, max 100) | No |

## Examples

### Basic Usage

```bash
subfinder -d example.com -o subdomains.txt
```

### Advanced Usage

With all sources and threading:

```bash
subfinder -d example.com -o subdomains.txt -all -t 100 -silent
```

## Expected Output

Console summary:

[INF] Enumerating subdomains for example.com
[INF] Found 45 subdomains

The output file contains lines like:

mail.example.com
www.example.com
api.example.com

## Related

- [[procedures/Subdomain-Enumeration-with-Subfinder]]
- [[tools/Subfinder]]

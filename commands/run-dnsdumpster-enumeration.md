---
id: 68ad17a0-a985-48ac-8980-1fb26023dc6d
name: run-dnsdumpster-enumeration
type: command
executor: bash
data: python dnsdumpster.py -d $_DOMAIN
output: null
created_at: '2023-04-06T03:56:25.739646+00:00'
updated_at: '2023-04-10T20:25:40.190549+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - enumeration
verified: true
validated: true
---

# run-dnsdumpster-enumeration

## Command

```bash
python dnsdumpster.py -d $_DOMAIN
```

## Description

This command runs the DNS Dumpster Python script to enumerate subdomains for the specified domain by querying public databases and search engines. It generates a CSV report with discovered subdomains and associated details. Run this after cloning the repository and navigating to the dnsdumpster directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d | Flag to specify the target domain | Yes |
| $_DOMAIN | The target domain name (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
python dnsdumpster.py -d example.com
```

### Advanced Usage

For verbose output (if supported by the script):

```bash
python dnsdumpster.py -d example.com -v
```

## Expected Output

Querying sources...
[Source 1]: Found X subdomains
[Source 2]: Found Y subdomains
Data written to example.com.csv

The CSV file contains columns like Domain, IP, Type, and Content.

## Related

- [[procedures/Subdomain-Enumeration-Using-DNS-Dumpster]]
- [[tools/DNS-Dumpster]]

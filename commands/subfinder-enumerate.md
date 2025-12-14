---
id: cmd-subfinder-enum
data: subfinder -d easycontactnow.com -all -o subdomains.txt
tags:
  - recon
  - dns
type: command
output: A file subdomains.txt listing discovered subdomains.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:24.056Z'
verified: false
validated: true
submitted: true
---
# subfinder-enumerate

## Command

```bash
subfinder -d easycontactnow.com -all -o subdomains.txt
```

## Description

This command uses the subfinder tool to perform comprehensive subdomain enumeration on a target domain, pulling from passive sources to identify potential attack surfaces like support.easycontactnow.com.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Target domain | Yes |
| `-all` | Use all available sources | No |
| `-o` | Output file | Yes |

## Examples

### Basic Usage

```bash
subfinder -d example.com -o subs.txt
```

### Advanced Usage

```bash
subfinder -d easycontactnow.com -all -t 50 -o subdomains.txt
```

## Expected Output

A text file with one subdomain per line, e.g., support.easycontactnow.com.

## Related

- [[Related Procedure: Enumerate-Subdomains-and-Identify-Dangling-CNAME]]

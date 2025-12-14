---
id: cmd-uuid-1
data: subfinder -d example.com -o subdomains.txt
tags:
  - recon
  - dns
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.222Z'
verified: false
validated: true
submitted: true
---
# subfinder-enumerate-subdomains

## Command

```bash
subfinder -d example.com -o subdomains.txt
```

## Description

This command uses Subfinder to enumerate subdomains of a target domain via passive sources like certificate transparency logs and search engines, useful for identifying potential attack surfaces in reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Target domain to enumerate | Yes |
| `-o` | Output file for subdomains | No (defaults to stdout) |

## Examples

### Basic Usage

```bash
subfinder -d 8x8.com -o subdomains.txt
```

### Advanced Usage

```bash
subfinder -d 8x8.com -all -o subdomains.txt
```

## Expected Output

A text file listing discovered subdomains, e.g., staging.8x8.com, api.8x8.com.

## Related

- [[Related Procedure: Identify Dangling DNS Records for Subdomain Takeover]]

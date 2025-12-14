---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: subfinder -d $DOMAIN -all -o $OUTPUT
tags:
  - recon
  - dns
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:18.226Z'
verified: false
validated: true
submitted: true
---
# subfinder-enumerate

## Command

```bash
subfinder -d uber.com -all -o subdomains.txt
```

## Description

Enumerates subdomains of a target domain using passive and active sources, ideal for identifying takeover candidates in reconnaissance phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d, --domain` | Target domain to enumerate | Yes |
| `-all` | Use all available sources | No |
| `-o, --output` | Output file for results | Yes |

## Examples

### Basic Usage

```bash
subfinder -d uber.com -o subdomains.txt
```

### Advanced Usage

```bash
subfinder -d uber.com -all -silent -o subdomains.txt
```

## Expected Output

A text file listing discovered subdomains, one per line, e.g., 'api.uber.com\nwww.uber.com'.

## Related

- [[commands/dig-cname-query]]
- [[procedures/Enumerate-Subdomains-for-Takeover]]

---
id: c4391d16-b30e-4054-b465-70efbad8c529
name: sublist3r-show-help
type: command
executor: bash
data: sublist3r -h
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - reconnaissance
  - osint
verified: true
validated: true
---

# sublist3r-show-help

## Command

```bash
sublist3r -h
```

## Description

Displays the help menu for Sublist3r, listing all available options, flags, and usage syntax. This is useful for verifying the tool's installation and reviewing parameters such as enabling brute-force enumeration or specifying search engines.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-h, --help` | Show the help message and exit | Yes |

## Examples

### Basic Usage

```bash
sublist3r -h
```

### Advanced Usage

No additional flags needed for help display.

## Expected Output

```
Usage: sublist3r [OPTIONS]

Options:
  -d, --domain TEXT   Specify domain name to enumerate subdomains
  -b, --bruteforce    Enable subdomain brute-force module
  -p, --ports <ports> Scan top ports of found subdomains
  -v, --verbose       Enable verbose mode
  -t, --threads TEXT  Number of threads to use (default: 10)
  -e, --engines TEXT  Specify engines
  -o, --output TEXT   Specify output file
  -n, --no-banner     Don't display the banner
  --help              Show this message and exit.
```

## Related

- [[commands/sublist3r-enumerate-subdomains]]
- [[procedures/Enumerate-Domain-Subdomains-using-OSINT]]

---
data: tko-subs -l subdomains.txt
tags:
  - takeover-check
  - dns
type: command
output: Status report for each subdomain's takeover eligibility
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.756Z'
id: 0ea03502-35c4-4897-9a97-dc21a80d8c72
verified: false
validated: true
submitted: true
---
# tko-subs-check-takeover

## Command

```bash
tko-subs -l subdomains.txt
```

## Description

This command checks a list of subdomains for takeover vulnerabilities by verifying if they resolve to dead cloud providers like Azure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Input file of subdomains | Yes |

## Examples

### Basic Usage

```bash
tko-subs -l subdomains.txt
```

### Advanced Usage

```bash
tko-subs -l subdomains.txt -v
```

## Expected Output

Console output like "svcardproxydevus.starbucks.com: vulnerable (dead Azure)".

## Related

- [[commands/subfinder-enumerate-subdomains]]
- [[procedures/Enumerate-and-Verify-Dead-Subdomains]]

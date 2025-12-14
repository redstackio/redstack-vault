---
id: cmd-001
data: dig +short @8.8.8.8 $SUBDOMAIN
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.197Z'
verified: false
validated: true
submitted: true
---
# dig-lookup

## Command

```bash
dig +short @8.8.8.8 $SUBDOMAIN
```

## Description

Performs a quick DNS lookup for a subdomain using Google's public resolver to retrieve IP or CNAME, useful for identifying dangling records in reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `@8.8.8.8` | Specifies Google DNS server | No |
| `$SUBDOMAIN` | Target subdomain (e.g., ███████.8x8.com) | Yes |
| `+short` | Outputs only the resolved record | No |

## Examples

### Basic Usage

```bash
dig +short @8.8.8.8 ███████.8x8.com
```

### Advanced Usage

```bash
dig +short +trace @8.8.8.8 8x8.com
```

## Expected Output

A single line with the IP address (e.g., 52.XX.XX.XX) or CNAME if it resolves; empty or error for dangling records.

## Related

- [[Related Procedure: Discover-Dangling-DNS-Records]]

---
data: dig $1 $2
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
updated_at: '2025-12-14T05:32:31.253Z'
id: 9fa6fb97-5136-4db0-bfd6-71d9db81bb72
verified: false
validated: true
submitted: true
---
# dig-dns-query

## Command

```bash
dig $1 $2
```

## Description

Queries DNS records for a domain, useful for identifying CNAME pointers in subdomain takeover reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $1 | Domain name (e.g., dev.rbk.money) | Yes |
| $2 | Record type (e.g., CNAME) | No (defaults to A) |

## Examples

### Basic Usage

```bash
dig dev.rbk.money CNAME
```

### Advanced Usage

```bash
dig dev.rbk.money +short CNAME
```

## Expected Output

DNS response with authority and answer sections, e.g., "dev.rbk.money. 3600 IN CNAME github.map.fastly.net."

## Related

- [[Related Procedure]]

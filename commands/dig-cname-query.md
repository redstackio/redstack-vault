---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: dig $SUBDOMAIN CNAME
tags:
  - dns
  - query
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:18.223Z'
verified: false
validated: true
submitted: true
---
# dig-cname-query

## Command

```bash
dig example.uber.com CNAME
```

## Description

Queries DNS for the CNAME record of a subdomain to check for dangling pointers to cloud services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `SUBDOMAIN` | The subdomain to query | Yes |
| `CNAME` | Specifies CNAME record type | Yes |

## Examples

### Basic Usage

```bash
dig example.uber.com CNAME
```

### Advanced Usage

```bash
dig +short example.uber.com CNAME
```

## Expected Output

DNS response like 'example.uber.com. 3600 IN CNAME dangling-app.herokuapp.com.' or NXDOMAIN if not set.

## Related

- [[commands/subfinder-enumerate]]
- [[procedures/Verify-Dangling-DNS-Record]]

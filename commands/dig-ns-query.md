---
id: cmd-uuid-004
data: dig example-subdomain.marketo.net CNAME
tags:
  - dns
  - query
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.556Z'
verified: false
validated: true
submitted: true
---
# dig-ns-query

## Command

```bash
dig example-subdomain.marketo.net CNAME
```

## Description

Performs a detailed DNS query for CNAME records on a specific subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `CNAME` | Record type | Yes |

## Examples

### Basic Usage

```bash
dig example-subdomain.marketo.net CNAME
```

### Advanced Usage

```bash
dig example-subdomain.marketo.net CNAME +trace
```

## Expected Output

Full DNS response showing CNAME or errors.

## Related

- [[commands/subjack-validate]]
- [[procedures/Validate-Dangling-DNS-for-Takeover]]

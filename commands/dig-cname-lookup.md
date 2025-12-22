---
id: cmd-uuid-2
data: dig ws.bimedb.com +short
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.768Z'
verified: false
validated: true
submitted: true
---
# dig-cname-lookup

## Command

```bash
dig ws.bimedb.com +short
```

## Description

This command queries DNS for the CNAME or A record of a subdomain to identify pointers to cloud services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+short` | Compact output | No |

## Examples

### Basic Usage

```bash
dig example.com +short
```

### Advanced Usage

```bash
dig @8.8.8.8 ws.bimedb.com CNAME
```

## Expected Output

Short DNS response, e.g., "ws-bimedb-com.s3.amazonaws.com.".

## Related

- [[Related Procedure: Enumerate-Subdomains-for-Takeover]]

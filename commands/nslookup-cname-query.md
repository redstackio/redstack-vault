---
id: cmd-uuid-nslookup-cname
data: nslookup -type=CNAME subdomain.target.com
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.829Z'
verified: false
validated: true
submitted: true
---
# nslookup-cname-query

## Command

```bash
nslookup -type=CNAME subdomain.target.com
```

## Description

Queries the DNS for the CNAME record of a subdomain to identify if it points to cloud services like AWS S3.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-type=CNAME` | Specifies query type for canonical name | Yes |
| `subdomain.target.com` | The subdomain to query | Yes |

## Examples

### Basic Usage

```bash
nslookup -type=CNAME suspected-sub.target.com
```

### Advanced Usage

```bash
nslookup -type=CNAME subdomain.target.com 8.8.8.8
```

## Expected Output

Server response with CNAME like 'subdomain.target.com canonical name = bucket.s3.amazonaws.com'.

## Related

- [[Related Procedure]]

---
id: cmd-uuid-001
data: dig @1.0.0.1 $1 $2 +short
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
updated_at: '2025-12-14T05:32:31.184Z'
verified: false
validated: true
submitted: true
---
# dig-query-dns

## Command

```bash
dig @1.0.0.1 max1.liveplan.com A +short
```

## Description

Queries a specified DNS resolver for A or CNAME records of a subdomain, used for reconnaissance to uncover misconfigurations like dangling CNAMEs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `@1.0.0.1` | DNS resolver IP (Cloudflare) | Yes |
| `max1.liveplan.com` | Target subdomain | Yes |
| `A` or `CNAME` | Record type | Yes |
| `+short` | Compact output | No |

## Examples

### Basic Usage

```bash
dig @1.0.0.1 max1.liveplan.com A +short
```

### Advanced Usage

```bash
dig @1.0.0.1 max1.liveplan.com CNAME +short
```

## Expected Output

IP address like 54.68.121.128 or CNAME ec2-54-68-121-128.us-west-2.compute.amazonaws.com.

## Related

- [[Related Procedure: Query-DNS-Records-for-Subdomain-Reconnaissance]]

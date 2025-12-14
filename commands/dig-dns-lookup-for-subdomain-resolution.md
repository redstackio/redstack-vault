---
data: dig 8ybhy85kld9zp9xf84x6.imgur.com
tags:
  - dns
  - recon
type: command
output: >-
  Shows CNAME to verify.squarespace.com. and multiple A records
  (198.185.159.177, 198.185.159.176, 198.49.23.176, 198.49.23.177); query time
  ~126 msec
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.481Z'
id: d9aadad1-45d3-443c-8eb3-c3ec915f1467
verified: false
validated: true
submitted: true
---
# dig DNS Lookup for Subdomain Resolution

## Command

```bash
dig 8ybhy85kld9zp9xf84x6.imgur.com
```

## Description

This command performs a DNS query to resolve the specified subdomain, revealing CNAME and A records to verify takeover status, such as pointing to Squarespace servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `8ybhy85kld9zp9xf84x6.imgur.com` | The subdomain to query | Yes |

## Examples

### Basic Usage

```bash
dig 8ybhy85kld9zp9xf84x6.imgur.com
```

### Advanced Usage

```bash
dig +short 8ybhy85kld9zp9xf84x6.imgur.com CNAME
```

## Expected Output

Detailed DNS response including authority section with CNAME to verify.squarespace.com and additional section with A records for Squarespace IPs, confirming the dangling or hijacked state.

## Related

- [[procedures/Claim-Subdomain-via-Squarespace]]
- [[procedures/Verify-Subdomain-Takeover]]

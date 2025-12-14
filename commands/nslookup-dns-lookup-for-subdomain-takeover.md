---
id: 123e4567-e89b-12d3-a456-426614174006
name: nslookup-dns-lookup-for-subdomain-takeover
type: command
executor: bash
data: '# nslookup saostatic.uber.com 8.8.8.8'
output: "saostatic.uber.com\tcanonical name = d3i4yxtzktqr9n.cloudfront.net."
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.857Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - dns
  - recon
verified: false
validated: true
submitted: true
---

# nslookup-dns-lookup-for-subdomain-takeover

## Command

```bash
# nslookup saostatic.uber.com 8.8.8.8
```

## Description

This command performs a DNS lookup on a target subdomain using a specified resolver to reveal CNAME records, helping identify subdomain takeover vulnerabilities where dangling pointers lead to unclaimed cloud resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| saostatic.uber.com | Target subdomain to query | Yes |
| 8.8.8.8 | DNS server (Google Public DNS for reliable resolution) | No (defaults to system) |

## Examples

### Basic Usage

```bash
nslookup saostatic.uber.com
```

### Advanced Usage

```bash
nslookup saostatic.uber.com 8.8.8.8 -type=CNAME
```

## Expected Output

Server response showing the canonical name (CNAME) record, e.g., 'saostatic.uber.com canonical name = d3i4yxtzktqr9n.cloudfront.net.', followed by IP addresses. If unclaimed, further verification shows cloud error pages.

## Related

- [[procedures/Perform-DNS-Lookup-for-Subdomain-Takeover-Discovery]]
- [[tools/nslookup]]

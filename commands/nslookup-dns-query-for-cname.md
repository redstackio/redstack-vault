---
id: cmd-nslookup-cname-query
data: nslookup saostatic.uber.com 8.8.8.8
tags:
  - dns
  - recon
type: command
output: |-
  Server:        8.8.8.8
  Address:       8.8.8.8#53

  Non-authoritative answer:
  saostatic.uber.com    canonical name = d3i4yxtzktqr9n.cloudfront.net.
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.881Z'
verified: false
validated: true
submitted: true
---
# nslookup DNS Query for CNAME

## Command

```bash
nslookup saostatic.uber.com 8.8.8.8
```

## Description

This command performs a DNS lookup on a subdomain using a public resolver to identify CNAME records pointing to cloud services, aiding in subdomain takeover detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| saostatic.uber.com | The target subdomain to query | Yes |
| 8.8.8.8 | DNS server (Google Public DNS) | No (defaults to system resolver) |

## Examples

### Basic Usage

```bash
nslookup saostatic.uber.com 8.8.8.8
```

### Advanced Usage

```bash
nslookup -type=CNAME example.com 8.8.8.8
```

## Expected Output

Description of what output to expect when the command runs successfully: Server response with canonical name (CNAME) if present, e.g., saostatic.uber.com canonical name = d3i4yxtzktqr9n.cloudfront.net.

## Related

- [[Related Procedure: Discover-Subdomain-Takeover-Via-DNS-Lookup]]

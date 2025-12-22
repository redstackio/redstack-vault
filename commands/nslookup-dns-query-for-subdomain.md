---
id: cmd-nslookup-subdomain
data: nslookup ping.ubnt.com 8.8.8.8
tags:
  - dns
  - recon
type: command
output: |-
  Server:        8.8.8.8
  Address:       8.8.8.8#53

  Non-authoritative answer:
  ping.ubnt.com   canonical name = dl.ubnt.com.
  dl.ubnt.com canonical name = d2cnv2pop2xy4v.cloudfront.net.
  Name:   d2cnv2pop2xy4v.cloudfront.net
  Address: 54.192.96.244
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.633Z'
verified: false
validated: true
submitted: true
---
# nslookup DNS Query for Subdomain

## Command

```bash
nslookup ping.ubnt.com 8.8.8.8
```

## Description

Performs a DNS lookup to resolve a hostname and identify CNAME records, useful for discovering dangling pointers in subdomain takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | The subdomain to query (e.g., ping.ubnt.com) | Yes |
| server | DNS resolver IP (e.g., 8.8.8.8 for Google's public DNS) | No (defaults to system resolver) |

## Examples

### Basic Usage

```bash
nslookup ping.ubnt.com
```

### Advanced Usage

```bash
nslookup -type=CNAME ping.ubnt.com 8.8.8.8
```

## Expected Output

Non-authoritative answer showing CNAME chain: ping.ubnt.com canonical name = dl.ubnt.com, dl.ubnt.com canonical name = d2cnv2pop2xy4v.cloudfront.net, and an IP address like 54.192.96.244. Look for cloud service indicators.

## Related

- [[procedures/Discover-Dangling-CNAME-for-Subdomain-Takeover]]

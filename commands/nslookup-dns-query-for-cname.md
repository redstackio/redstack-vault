---
id: cmd-nslookup-ubnt
data: nslookup ping.ubnt.com 8.8.8.8
tags:
  - dns
  - recon
type: command
output: "Server:        8.8.8.8\nAddress:       8.8.8.8#53\n\nNon-authoritative answer:\nping.ubnt.com\tcanonical name = dl.ubnt.com.\ndl.ubnt.com\tcanonical name = d2cnv2pop2xy4v.cloudfront.net.\nName:   d2cnv2pop2xy4v.cloudfront.net\nAddress: 54.192.96.244"
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:43.050Z'
verified: false
validated: true
submitted: true
---
# nslookup-dns-query-for-cname

## Command

```bash
nslookup ping.ubnt.com 8.8.8.8
```

## Description

Performs a DNS lookup on the specified subdomain using a public resolver to reveal CNAME records and IP addresses, useful for identifying cloud service pointers in takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ping.ubnt.com | Target domain/subdomain to resolve | Yes |
| 8.8.8.8 | DNS server IP (Google Public DNS) | No (defaults to system resolver) |

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

Non-authoritative answer showing the CNAME chain to Cloudfront and an IP address like 54.192.96.244.

## Related

- [[Related Procedure|procedures/DNS-Lookup-for-Subdomain-Enumeration]]

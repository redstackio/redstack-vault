---
data: nslookup engineering.zomato.com
tags:
  - dns
  - recon
type: command
output: |-
  Server: 192.168.188.2
  Address: 192.168.188.2
  Non-authoritative answer:
  engineering.zomato.com canonical name = domains.tumblr.com.
  Name: domains.tumblr.com
  Address: 66.6.42.22
  Name: domains.tumblr.com
  Address: 66.6.43.22
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.442Z'
id: 41c9ae38-07e5-416d-a697-3e125cec7d85
verified: false
validated: true
submitted: true
---
# nslookup-dns-query

## Command

```bash
nslookup engineering.zomato.com
```

## Description

This command performs a DNS lookup on the specified hostname to retrieve resolution details, including CNAME and A records, useful for identifying misconfigurations like subdomain takeovers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | The domain or subdomain to query (e.g., engineering.zomato.com) | Yes |

## Examples

### Basic Usage

```bash
nslookup engineering.zomato.com
```

### Advanced Usage

```bash
nslookup -type=CNAME engineering.zomato.com
```

## Expected Output

Description of what output to expect when the command runs successfully. For a misconfigured subdomain, it shows the CNAME to an external service and associated IPs, e.g., Server details, canonical name = domains.tumblr.com, and Addresses 66.6.42.22, 66.6.43.22.

## Related

- [[Related Procedure: Detect-Subdomain-Takeover-via-DNS-Lookup]]

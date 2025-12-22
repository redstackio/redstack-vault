---
id: d6a300a9-ac7b-4dc3-a222-915c832bc2db
name: assets-from-spf-basic-scan
type: command
executor: bash
data: |
  python assets_from_spf.py $_DOMAIN
output: null
created_at: '2020-07-24T17:11:28.247970+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
verified: true
validated: true
---

# assets-from-spf-basic-scan

## Command

```bash
python assets_from_spf.py $_DOMAIN
```

## Description

This command runs the assets-from-spf Python script to parse SPF DNS records for a given domain, extracting IP addresses, netblocks (CIDRs), and included domains. Use it during initial reconnaissance to uncover related network assets passively via DNS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain to query SPF records for (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
python assets_from_spf.py owasp.com
```

### Advanced Usage

For scripting, redirect output to a file:

```bash
python assets_from_spf.py owasp.com > spf_assets.txt
```

## Expected Output

The command outputs a list of discovered assets, such as:

```
IP: 192.0.2.1
CIDR: 192.0.2.0/24
Domain: partner.example.com
Include: include:_spf.google.com
```

Success is indicated by parsed SPF mechanisms without DNS resolution errors.

## Related

- [[procedures/Find-Domains-and-Netblocks-from-SPF-Records]]
- [[commands/assets-from-spf-with-asn-to-jq]]

---
data: dig subdomain.example.com
tags:
  - recon
  - dns
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 3609e7c2-0700-4141-9ec7-7a2cccdb5c12
created_at: '2025-12-11T06:10:30.490Z'
updated_at: '2025-12-11T06:10:30.490Z'
verified: false
validated: true
submitted: true
---
# dig-dns-lookup

## Command

```bash
dig subdomain.example.com
```

## Description

Performs a DNS lookup to retrieve records for a given subdomain, useful for identifying CNAMEs in subdomain takeover reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `subdomain.example.com` | The subdomain to query | Yes |

## Examples

### Basic Usage

```bash
dig devrel.roblox.com
```

### Advanced Usage

```bash
dig +short CNAME devrel.roblox.com
```

## Expected Output

DNS records including A, CNAME, etc., showing resolutions like CNAME to HubSpot.

## Related

- [[procedures/Identify-Dangling-CNAME-for-Subdomain-Takeover]]

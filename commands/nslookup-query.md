---
id: cmd-nslookup
data: nslookup kiosk.owox.com
tags:
  - dns
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.406Z'
verified: false
validated: true
submitted: true
---
# nslookup-query

## Command

```bash
nslookup kiosk.owox.com
```

## Description

Queries DNS servers for information on the target subdomain, helping verify misconfigurations for subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `kiosk.owox.com` | Target to resolve | Yes |

## Examples

### Basic Usage

```bash
nslookup kiosk.owox.com
```

### Advanced Usage

```bash
nslookup -type=CNAME kiosk.owox.com
```

## Expected Output

Server and non-authoritative answer sections with IP addresses or CNAMEs, flagging dangling records if pointed to unclaimed services.

## Related

- [[commands/dig-dns-lookup]]
- [[procedures/Verify-DNS-Misconfiguration]]

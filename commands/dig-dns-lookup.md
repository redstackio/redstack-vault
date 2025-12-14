---
id: cmd-dig-lookup
data: dig kiosk.owox.com
tags:
  - dns
  - reconnaissance
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.418Z'
verified: false
validated: true
submitted: true
---
# dig-dns-lookup

## Command

```bash
dig kiosk.owox.com
```

## Description

This command performs a DNS lookup on the specified subdomain to retrieve records, useful for identifying misconfigurations in subdomain takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `kiosk.owox.com` | The domain or subdomain to query | Yes |

## Examples

### Basic Usage

```bash
dig kiosk.owox.com
```

### Advanced Usage

```bash
dig +short kiosk.owox.com
```

## Expected Output

DNS response sections including QUESTION, ANSWER, AUTHORITY, and ADDITIONAL, showing CNAME or other records indicating potential takeover (e.g., unclaimed service pointer).

## Related

- [[commands/nslookup-query]]
- [[procedures/Reconnaissance-for-Subdomain-Takeover]]

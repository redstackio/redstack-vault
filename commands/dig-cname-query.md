---
data: dig +short landing.udemy.com CNAME
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:24.204Z'
id: dcde3ad6-363e-4c9a-b9ea-31b2c90f8ed2
verified: false
validated: true
submitted: true
---
# dig-cname-query

## Command

```bash
dig +short landing.udemy.com CNAME
```

## Description

This command uses the dig utility to query DNS for the CNAME record of a specific subdomain, helping identify dangling pointers to third-party services for subdomain takeover reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+short` | Limits output to essential record data only | No |
| `landing.udemy.com` | The target subdomain to query | Yes |
| `CNAME` | Specifies the record type to retrieve | Yes |

## Examples

### Basic Usage

```bash
dig +short landing.udemy.com CNAME
```

### Advanced Usage

```bash
dig landing.udemy.com CNAME
```

## Expected Output

"pages.unbounce.com." or similar CNAME value, indicating the pointed-to domain. If empty, no CNAME exists.

## Related

- [[Related Procedure]]

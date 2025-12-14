---
data: dig +short s00397nasv101-datacafe-cert.azurewebsites.net
tags:
  - dns
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:01.976Z'
id: 54982281-bf5f-4146-8081-8b51164c3d2b
verified: false
validated: true
submitted: true
---
# dig-nxdomain-check

## Command

```bash
dig +short s00397nasv101-datacafe-cert.azurewebsites.net
```

## Description

Performs a DNS lookup on a potential unclaimed resource to check for NXDOMAIN, confirming availability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+short` | Compact output | No |
| `domain` | Target resource | Yes |

## Examples

### Basic Usage

```bash
dig +short unclaimed.azurewebsites.net
```

### Advanced Usage

```bash
dig +short +tcp unclaimed.azurewebsites.net
```

## Expected Output

Empty or NXDOMAIN status message.

## Related

- [[commands/dig-cname-query]]

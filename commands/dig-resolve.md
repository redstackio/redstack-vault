---
id: c-dig-resolve
data: dig %s CNAME
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.485Z'
verified: false
validated: true
submitted: true
---
# dig-resolve

## Command

```bash
dig twitterflightschool.com CNAME
```

## Description

This command uses the dig utility to query DNS for CNAME records of a target domain, useful for identifying third-party integrations in reconnaissance phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `domain` | Target domain to query | Yes |
| `CNAME` | Record type to fetch | Yes |

## Examples

### Basic Usage

```bash
dig example.com CNAME
```

### Advanced Usage

```bash
dig +trace example.com
```

## Expected Output

DNS response with CNAME alias, e.g., "twitterflightschool.com. 3600 IN CNAME vendor.example.com."

## Related

- [[Related Procedure]]

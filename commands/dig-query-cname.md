---
id: 2f1bd55d-97b4-4b61-82f7-c72b1c13ff24
name: dig-query-cname
type: command
executor: bash
data: dig subdomain.owow.com CNAME +short
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:24.242Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - dns
  - recon
verified: false
validated: true
submitted: true
---

# dig-query-cname

## Command

```bash
dig subdomain.owow.com CNAME +short
```

## Description

This command uses dig to query the CNAME record for a specific subdomain, helping identify if it points to a third-party service that might be dangling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `subdomain.owow.com` | The subdomain to query | Yes |
| `CNAME` | Record type to query | Yes |
| `+short` | Output only the answer without extra details | No |

## Examples

### Basic Usage

```bash
dig app.owow.com CNAME
```

### Advanced Usage

```bash
dig app.owow.com CNAME +short +tcp
```

## Expected Output

Short response like "unused-service.herokuapp.com." indicating a potential dangling record.

## Related

- [[Related Procedure: Enumerate-and-Verify-Subdomain-Takeover]]

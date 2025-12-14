---
id: cmd-dns-enum
data: dnsenum zomato.com
tags:
  - dns
type: command
output: |-
  Host's addresses:
  zomato.com 52.77.124.190
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.241Z'
verified: false
validated: true
submitted: true
---
# dns-scan-enum

## Command

```bash
dnsenum zomato.com
```

## Description

Enumerates DNS records and subdomains for the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | Target domain | Yes |

## Examples

### Basic Usage

```bash
dnsenum zomato.com
```

## Expected Output

DNS records; may include subdomains.

## Related

- [[commands/aquatone-enumerate]]

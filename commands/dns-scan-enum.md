---
id: cmd-dns-enum-927413
data: dnsenum zomato.com
tags:
  - dns
type: command
output: |-
  Host's addresses:
  zomato.com 52.77.124.190
  Subdomains found: auth.zomato.com ...
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.628Z'
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

Enumerates DNS records and subdomains for the target, used in web testing for Zomato.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `zomato.com` | Target domain | Yes |

## Examples

### Basic Usage

```bash
dnsenum example.com
```

### Advanced Usage

```bash
dnsenum --enum -f dict.txt zomato.com
```

## Expected Output

DNS records and potential subdomains listed.

## Related

- [[Related Procedure: Web-Application-Testing-with-Burp-Suite-and-DNS-Scanner]]

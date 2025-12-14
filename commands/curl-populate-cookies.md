---
id: cmd-2
data: >-
  curl -c cookie.txt -b cookie.txt --connect-to
  evilsite.hax.invalid:80:127.0.0.1:9000 http://evilsite.hax.invalid/
tags:
  - curl
  - cookies
type: command
output: Malicious server response body
executor: bash
platforms:
  - Linux
  - Unix-like
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.105Z'
verified: false
validated: true
submitted: true
---
# curl-populate-cookies

## Command

```bash
curl -c cookie.txt -b cookie.txt --connect-to evilsite.hax.invalid:80:127.0.0.1:9000 http://evilsite.hax.invalid/
```

## Description

Fetches a URL via proxied connection, saving and loading cookies to/from cookie.txt to populate the jar with domain-wide excessive cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c cookie.txt` | Save cookies to file | Yes |
| `-b cookie.txt` | Load cookies from file | Yes |
| `--connect-to evilsite.hax.invalid:80:127.0.0.1:9000` | Redirect host:port to local | Yes |
| `http://evilsite.hax.invalid/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -c cookie.txt -b cookie.txt --connect-to evilsite.hax.invalid:80:127.0.0.1:9000 http://evilsite.hax.invalid/
```

## Expected Output

HTTP 200 response with server body; no errors, cookies saved to file.

## Related

- [[Related Procedure|procedures/Populate-Cookie-Jar-with-Domain-Cookies-Using-curl]]

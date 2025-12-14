---
id: cmd-curl-get-001
data: >-
  curl -X GET "https://www.localize.im/projects/[project ID]/languages/[Language
  ID]" -H "Cookie: session=your_session_cookie" -H "User-Agent: Mozilla/5.0"
tags:
  - web-request
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.014Z'
verified: false
validated: true
submitted: true
---
# curl-get-endpoint

## Command

```bash
curl -X GET "https://www.localize.im/projects/[project ID]/languages/[Language ID]" -H "Cookie: session=your_session_cookie" -H "User-Agent: Mozilla/5.0"
```

## Description

Sends a GET request to the Localize.im projects/languages endpoint to access and verify the target page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| URL | Target endpoint with IDs | Yes |
| `-H "Cookie: ..."` | Authentication session | Yes |
| `-H "User-Agent: ..."` | Mimic browser | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.localize.im/projects/123/languages/456" -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -s -o response.html -X GET "https://www.localize.im/projects/123/languages/456" -H "Cookie: session=abc123" -H "Referer: https://www.localize.im"
```

## Expected Output

HTML response body with project and language details, HTTP status 200.

## Related

- [[Related Procedure]]

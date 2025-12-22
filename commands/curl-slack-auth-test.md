---
id: 8ba69aa5-4667-4812-827d-4274c99582cd
name: curl-slack-auth-test
type: command
executor: bash
data: 'curl -sX POST "https://slack.com/api/auth.test?token=$_TOKEN&pretty=1"'
output: null
created_at: '2023-04-06T03:55:53.079104+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - SaaS
tags:
  - api
  - auth
  - slack
verified: true
validated: true
---

# curl-slack-auth-test

## Command

```bash
curl -sX POST "https://slack.com/api/auth.test?token=$_TOKEN&pretty=1"
```

## Description

Tests the validity of a Slack API token by querying the auth.test endpoint. Returns workspace and user details if valid, or an error if invalid. Use this as the first step in exploiting leaked tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TOKEN | The Slack API token (e.g., xoxp-...) | Yes |
| -s | Silent mode (suppress progress meter) | Built-in |
| -X POST | Specify POST method | Built-in |
| pretty=1 | Format JSON response for readability | No |

## Examples

### Basic Usage

```bash
curl -sX POST "https://slack.com/api/auth.test?token=xoxp-your-token-here&pretty=1"
```

### Advanced Usage

```bash
curl -sX POST "https://slack.com/api/auth.test?token=$_TOKEN" | jq '.'
```
(Uses jq to parse JSON if installed.)

## Expected Output

Successful response (JSON):
```
{
  "ok": true,
  "url": "https://example.slack.com",
  "team": "Example Team",
  "user": "attacker",
  "team_id": "T12345678",
  "user_id": "U12345678"
}
```
Invalid token:
```
{
  "ok": false,
  "error": "invalid_auth"
}
```

## Related

- [[procedures/Exploit-Leaked-Slack-API-Token]]
- [[commands/curl-slack-conversations-list]]

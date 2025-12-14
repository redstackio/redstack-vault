---
tags:
  - pagination
  - graphql
  - data-collection
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:48.066Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d4a37296-5011-472e-b1ed-70c8771b84ab
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Check-for-Pagination-in-Response

## Summary

This procedure analyzes the GraphQL response from the mod logs query to detect if additional pages exist and extract the endCursor for continued pagination.

## Description

Reddit's mod logs use cursor-based pagination in the GraphQL response. The 'hasNextPage' boolean and 'endCursor' string allow attackers to fetch complete datasets, revealing full historical moderator actions without interruption.

## Requirements

1. JSON response from initial GraphQL query
2. jq or JSON parser
3. Basic scripting knowledge for automation

## Defense

Defensive measures and detection strategies:

- Limit pagination depth per request to prevent bulk data exfiltration
- Audit for repeated queries with endCursor from non-mods

## Objectives

1. Determine completeness of retrieved data
2. Extract cursor for next query
3. Enable full log collection

## Instructions

### Step 1: Parse Response Fields

**Context**: Use jq to query the response for pagination indicators.

**Command** (jq):
```bash
curl ... | jq '.data.modLog.pageInfo.hasNextPage, .data.modLog.pageInfo.endCursor'
```

> Outputs true/false for hasNextPage and the cursor string if present.

### Step 2: Conditional Check

**Context**: Script a check to decide on further actions.

**Command** (bash snippet):
```bash
if [ "$(echo $response | jq '.data.modLog.pageInfo.hasNextPage')" = "true" ]; then
  cursor=$(echo $response | jq -r '.data.modLog.pageInfo.endCursor')
  echo "Next cursor: $cursor"
else
  echo "No more pages"
fi
```

> Sets variable for use in pagination loop.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- response-parsing
- pagination-check

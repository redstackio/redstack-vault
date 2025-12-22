---
tags:
  - information-disclosure
  - api
  - data-extraction
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/jq-parse-causes]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:02.050Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: b40909c6-77dd-4d6e-9038-101c206d6e72
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-Private-Causes-from-API-Response

## Summary

This procedure parses the JSON response from a user profile API to extract the 'causes' array, revealing private interest categories that should be hidden based on user privacy settings.

## Description

After querying the API, the response contains a 'data.user.causes' array with objects including 'entityName' and 'causeCategory' (e.g., EDUCATION). This data is not displayed on the web profile for private accounts but is fully exposed via API. Used in web environments to collect user interests for reconnaissance or privacy violation. Outcomes: Structured list of private causes.

## Requirements

1. API response JSON from previous procedure
2. JSON parsing tool like jq or manual inspection
3. Confirmation of profile privacy (e.g., via web view)

## Defense

Defensive measures and detection strategies:

- Strip sensitive fields from API responses based on user privacy flags
- Audit API endpoints for over-exposure of user data
- Implement data masking for non-authorized queries

## Objectives

1. Identify and extract 'causes' array
2. Document private data leakage
3. Validate impact on privacy

## Instructions

### Step 1: Save and Inspect Response

**Context**: Obtain the raw JSON response for parsing.

Save the API output to a file (e.g., response.json).

### Step 2: Parse Causes Array

**Context**: Extract specific fields from the JSON structure.

**Command** ([[commands/jq-parse-causes]]):
```bash
jq '.data.user.causes[] | {entityName: .entityName, causeCategory: .causeCategory}' response.json
```

> This filters the causes array. Expected output: List of cause objects, e.g., {"entityName": "Example", "causeCategory": "EDUCATION"}.

**Expected Output**: Parsed private causes not visible publicly.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/jq-parse-causes]]

## Tools Used


## Tags

- data-extraction
- json-parsing

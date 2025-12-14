---
id: proc-analyze-graphql-response
tags:
  - analysis
  - detection
  - enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:53.469Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Analyze Response for Private Program Detection

## Summary

This procedure parses GraphQL responses to interpret the remaining_reports value, identifying private programs based on specific indicators like a value of 1.

## Description

After querying the API, the response's _remaining_reports3zrc4S field must be examined: a value of 1 indicates a private program exists for the external team, while null or other values (e.g., 5 for public) suggest otherwise. This analysis reveals hidden program structures without direct access.

## Requirements

1. JSON responses from GraphQL queries
2. JSON parsing tool (e.g., jq or Python json module)
3. List of queried handles for correlation

## Defense

Defensive measures and detection strategies:

- Mask sensitive fields in API responses
- Add noise or randomization to report counts
- Audit response logs for pattern analysis attempts

## Objectives

1. Classify responses to detect private indicators
2. Compile list of confirmed private programs
3. Validate findings against public data

## Instructions

### Step 1: Parse JSON Response

**Context**: Extract the key field from the response.

Use jq to filter: `echo 'response_json' | jq '.data.query.me._remaining_reports3zrc4S'`

> Expected output: Numeric value or null.

### Step 2: Interpret Value

**Context**: Determine private program existence.

If value is 1, mark as private; if null, no private; other values may indicate public trials.

> Expected output: Binary classification (private/non-private).

### Step 3: Correlate and Report

**Context**: Aggregate results across handles.

Map findings back to original team handles and document exposed private programs.

> Expected output: Report listing private programs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- analysis
- detection

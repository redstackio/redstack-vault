---
id: p6f7g8h9-i0j1-2345-fghi-678901234567
tags:
  - data-leak
  - observation
  - validation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:32:28.834Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Observe-User-Information-Response

## Summary

This procedure inspects the API response from the IDOR endpoint to confirm exposure of sensitive user details like emails and names without proper authorization.

## Description

Upon successful request, the endpoint returns full personal information for the specified USER_ID, demonstrating the lack of access controls. This validation step confirms the vulnerability's exploitability and potential for data breach.

## Requirements

1. Successful GET request response
2. Ability to parse JSON output
3. Knowledge of expected user fields

## Defense

Defensive measures and detection strategies:

- Mask sensitive fields in unauthorized responses
- Implement data loss prevention (DLP) monitoring
- Alert on unexpected data access

## Objectives

1. Parse response for leaked data
2. Verify unauthorized access
3. Document impact

## Instructions

### Step 1: Inspect Response Body

**Context**: Examine the JSON payload.

View the response in browser dev tools or proxy.

> Look for fields like email, name. Expected output: User details visible.

### Step 2: Validate Data Accuracy

**Context**: Cross-check with known test users.

Compare returned info (e.g., normaluser@gmail.com) against created accounts.

> Confirms leak. Expected output: Matches test data.

### Step 3: Note Absence of Errors

**Context**: Check for permission denials.

Ensure no 403 or auth errors.

> Indicates IDOR success. Expected output: 200 OK without restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- data-leak
- observation
- validation

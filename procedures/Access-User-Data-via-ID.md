---
id: uuid-access-id-1
tags:
  - idor
  - data-access
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
updated_at: '2025-12-14T17:29:19.872Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access User Data via ID

## Summary

This procedure exploits the IDOR vulnerability by directly browsing to the API endpoint with an arbitrary user ID, retrieving sensitive registration data without authentication.

## Description

Targeting https://tmss.gsa.gov/tmssserver/api/public/customerregistration/{id}/userId/, this accesses private user info via direct object reference. Applies to web browsers on public internet; outcomes include exposure of emails, names, phones for any ID 0-4800.

## Requirements

1. Web browser
2. Knowledge of sequential ID range (0-4800)
3. Unauthenticated session

## Defense

Defensive measures and detection strategies:

- Enforce ownership checks on API calls
- Log and alert on IDOR patterns
- Deprecate public endpoints for sensitive data

## Objectives

1. Retrieve PII for a specific user
2. Validate lack of auth checks
3. Confirm JSON response structure

## Instructions

### Step 1: Browse to Endpoint

**Context**: Use browser to hit the API with a test ID like 4750.

Navigate to: https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/

> Browser displays raw JSON with user details; no login prompted.

### Step 2: Inspect Response

**Context**: Verify sensitive fields are exposed.

View source or use dev tools to parse JSON for email, phone, etc.

> Success if full name, address, secret questions appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[data-access]]

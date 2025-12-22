---
id: 55f122e3-94c3-4fa3-b8b7-7c1aea4b6493
name: Modify ID Parameter for IDOR
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.714Z'
updated_at: '2025-12-11T03:47:47.714Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Information Repositories]]'
sub_techniques: []
tags:
  - idor
  - parameter-manipulation
  - graphql
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Proxy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
---

# Modify ID Parameter for IDOR

## Summary

This procedure modifies the ID parameter in an intercepted GraphQL query to target another user's certification for IDOR exploitation.

## Description

In the captured request body, change the ID to one from another account, exploiting the lack of ownership validation. This enables unauthorized access and deletion, leaking data in responses.

## Requirements

1. Intercepted GraphQL request in [[tools/Burp-Proxy]].
2. Knowledge of target certification ID (from prior observation or leak).
3. Valid session cookies.

## Defense

Defensive measures and detection strategies:

- Implement strict ID ownership checks in queries.
- Monitor for anomalous ID modifications in logs.

## Objectives

1. Bypass authorization via ID tampering.
2. Target arbitrary user data.
3. Prepare for deletion execution.

## Instructions

### Step 1: Locate ID Parameter

**Context**: Identify the modifiable field.

In Burp, find the 'id' field in the GraphQL query body.

> Note the original value.

### Step 2: Change to Target ID

**Context**: Input arbitrary ID.

Replace the ID with one from the other user's certification.

> Ensure the query syntax remains intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Proxy]]

## Tags

- idor
- parameter-manipulation
- graphql

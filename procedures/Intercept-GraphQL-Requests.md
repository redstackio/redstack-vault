---
tags:
  - interception
  - graphql
  - api-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:25:53.402Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 314f40b1-4449-46e3-b13f-6452b246e482
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Intercept-GraphQL-Requests

## Summary

Capture POST requests to the GraphQL endpoint in a proxy tool to analyze authentication headers and payloads for modification.

## Description

GraphQL requests carry session tokens; intercepting them allows replay with custom queries. Target: /graphql on hackerone.com.

## Requirements

1. Proxied session with auth tokens
2. Burp Suite HTTP History tab
3. Knowledge of GraphQL structure

## Defense

Defensive measures and detection strategies:

- Rate-limit GraphQL queries per token
- Validate query types against user status
- Detect proxy-like delays in request timing

## Objectives

1. Isolate recent GraphQL POST requests
2. Extract tokens and base payloads
3. Prepare for replay

## Instructions

### Step 1: Filter History

**Context**: Locate relevant requests.

No command; In Burp, go to Proxy > HTTP History, filter URL contains "/graphql".

> Select the latest POST after login.

### Step 2: Inspect Request

**Context**: Verify auth elements.

No command; Examine headers: X-Auth-Token, Cookie; body: JSON query.

> Confirm no disabled status enforcement.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-capture
- token-extraction

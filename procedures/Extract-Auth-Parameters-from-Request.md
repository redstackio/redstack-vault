---
id: uuid-extract-params
tags:
  - parameter-extraction
  - auth-token
  - session
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:28:59.263Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-Auth-Parameters-from-Request

## Summary

Extract critical authentication parameters such as 'login' and 'uki' from intercepted Dashlane API requests to enable reuse in unauthorized queries.

## Description

The 'login' parameter is the user's email, and 'uki' is a unique session identifier. These must be preserved when modifying requests to maintain authentication while changing the teamId for IDOR exploitation.

## Requirements

1. Intercepted request in Burp
2. Basic JSON/URL-encoded parsing knowledge

## Defense

Defensive measures and detection strategies:

- Tokenize parameters with short expirations
- Validate parameter integrity with HMAC
- Audit for parameter reuse in anomalous contexts

## Objectives

1. Isolate login and uki values
2. Prepare for request tampering
3. Ensure session validity

## Instructions

### Step 1: Inspect Request Body

**Context**: Locate parameters in the captured request.

**Instructions**: In Burp Inspector, view the raw body and copy values for 'login' (e.g., user@example.com) and 'uki' (long token string).

> Store these securely for the next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- extraction
- auth

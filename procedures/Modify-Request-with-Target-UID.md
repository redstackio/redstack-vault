---
tags:
  - modification
  - tampering
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:28.977Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 1677f0c9-4db7-4abd-b376-582df99ddb49
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Request-with-Target-UID

## Summary

This procedure tampers with the intercepted API request in Burp Suite by replacing the 'uid' parameter with a target user's ID and altering the path, preparing it for IDOR exploitation to access unauthorized profiles.

## Description

The Chameleon API request body contains a JSON payload with 'uid' referencing the current user. By editing this to a target ID and appending a random string to the path (to simulate a unique profile), the request bypasses authorization checks. This step requires familiarity with HTTP request structures and JSON editing in a proxy tool.

## Requirements

1. Intercepted request in Burp Repeater
2. Extracted target userID
3. Basic knowledge of JSON and HTTP

## Defense

Defensive measures and detection strategies:

- Validate 'uid' against requester's session or JWT claims
- Sign requests with HMAC to detect tampering
- Log discrepancies between path parameters and body values

## Objectives

1. Update 'uid' to target value
2. Randomize path to avoid caching or duplicates
3. Ensure request remains syntactically valid

## Instructions

### Step 1: Edit UID in Body

**Context**: Replace the original 'uid' with the target's ID in the JSON payload.

In Burp Repeater, locate the 'uid' field in the request body and change it, e.g., from current to "uid":"40991562".

**Expected Output**: JSON updated without syntax errors.

### Step 2: Update Username

**Context**: Align the 'username' field with the target for consistency.

Modify 'username' to match the target, e.g., "username":"nochnoidozorh1".

**Expected Output**: Payload reflects target details.

### Step 3: Append Random Path

**Context**: Change the endpoint path to include a random string.

Edit the request line to POST /observe/v2/profiles/dawda (random value).

**Expected Output**: Path modified, request ready to send.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- modification
- tampering

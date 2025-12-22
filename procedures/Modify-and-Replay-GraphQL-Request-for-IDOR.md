---
tags:
  - idor
  - modification
  - deletion
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Data Destruction]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 52ee466f-645b-45fc-b82e-92771da09707
created_at: '2025-12-11T06:10:28.961Z'
updated_at: '2025-12-11T06:10:28.961Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1485]]'
---
# Modify and Replay GraphQL Request for IDOR

## Summary

This procedure modifies the captured GraphQL delete request by replacing the 'ids' parameter with a target's Spotlight ID and replays it to exploit the IDOR vulnerability, resulting in unauthorized content deletion.

## Description

Using the intercepted request, the ID is swapped with one from a shared Spotlight URL, bypassing ownership checks due to insufficient authorization. This achieves remote deletion without permission.

## Requirements
1. Captured delete request in Burp Suite.
2. Target Spotlight ID from a shared URL.
3. Active authenticated session.

## Defense

Defensive measures and detection strategies:
- Enforce ownership validation on all IDs in API requests.
- Rate limit delete operations and monitor for anomalies.

## Objectives
1. Modify request to target another user's content.
2. Execute the modified request.
3. Verify deletion of targeted content.

## Instructions

### Step 1: Edit Request Parameters

**Context**: Replace the ID in the request.

In Burp Suite Repeater, update the 'ids' array in the variables object with the target's ID.

> Ensure the storyType remains 'SPOTLIGHT_STORY'.

### Step 2: Forward Modified Request

**Context**: Send the altered request to the server.

Click 'Send' in Repeater to execute the mutation.

> The server deletes the content if IDOR is present.

## MITRE ATT&CK Mapping

### Tactics
- [[Impact]]

### Techniques
- [[Data Destruction]]

### Sub-Techniques

## Commands Used

## Tools Used
- [[tools/Burp-Suite]]

## Tags
- idor
- deletion

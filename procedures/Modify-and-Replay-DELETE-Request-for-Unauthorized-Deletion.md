---
tags:
  - tamper
  - replay
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/fabric-delete-team-member-modified]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.804Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 35754aa3-033c-44ce-8ee4-e433ee992751
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Modify-and-Replay-DELETE-Request-for-Unauthorized-Deletion

## Summary

This procedure modifies an intercepted HTTP DELETE request in Burp Proxy to change the target app_id and account_id, removing a user from an unauthorized Fabric.io application and exploiting the lack of access checks.

## Description

Using the legitimate request as a template, the attacker alters the account_id to point to a victim user (e.g., Alicemember) and the app_id to the victim app (VictimApp), while stripping the admin parameter. Replaying this request leverages the authenticated session to bypass app-specific authorization, resulting in unauthorized deletion. This demonstrates a classic IDOR-style vulnerability in the DELETE /accounts endpoint.

## Requirements

1. Intercepted legitimate request in Burp Proxy
2. Known victim app_id and account_id from setup
3. Active admin session from HackerApp

## Defense

Defensive measures and detection strategies:

- Validate requesting user's access to app_id on every DELETE
- Implement parameter binding and server-side authorization checks
- Monitor for parameter mismatches in logs (e.g., app_id not matching session)

## Objectives

1. Achieve unauthorized user deletion across apps
2. Confirm authorization bypass success
3. Minimize detection by mimicking legitimate requests

## Instructions

### Step 1: Edit Request Parameters

**Context**: Tamper with the intercepted request to target victim resources.

In Burp Repeater, change account_id to 54af48304d8f5b12ff0000fd (Alicemember), app_id to 54ad5e03a25bb8136b000002 (VictimApp), remove admin=true.

**Expected Output**: Modified request ready for replay.

### Step 2: Replay the Modified Request

**Context**: Send the tampered request to exploit the vulnerability.

Click Send in Burp Repeater.

**Command** ([[commands/fabric-delete-team-member-modified]]):

The modified request is:

```http
DELETE /accounts/54af48304d8f5b12ff0000fd?app_id=54ad5e03a25bb8136b000002 HTTP/1.1
Host: fabric.io
```

> This command deletes Alicemember from VictimApp without access. Expected output: 200 OK, no auth error.

### Step 3: Clear Interception

**Context**: Resume normal traffic flow post-exploit.

Turn off Intercept in Burp.

**Expected Output**: Session intact for further actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/fabric-delete-team-member-modified]]

## Tools Used

- [[tools/Burp-Proxy]]

## Tags

- tamper
- replay
- bypass

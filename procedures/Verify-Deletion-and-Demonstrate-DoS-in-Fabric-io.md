---
tags:
  - verify
  - dos
  - impact
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
updated_at: '2025-12-14T17:28:44.801Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 7a3f02a0-f55a-44b6-b42e-7c2b5d6d0a96
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Verify-Deletion-and-Demonstrate-DoS-in-Fabric-io

## Summary

This procedure confirms the success of unauthorized deletions in Fabric.io and escalates to denial-of-service by removing the last admin user, rendering the application inaccessible and blocking recovery options like password resets.

## Description

After modification and replay, log in as the victim admin to check the team list, verifying removal. To demonstrate DoS, repeat the tampering targeting the last admin (Aliceadmin), then attempt app access or password reset, which fails due to no remaining authorized users. This highlights the vulnerability's potential for operational disruption.

## Requirements

1. Successful prior deletion of a non-admin user
2. Access to victim admin credentials
3. Burp Proxy for repeated modifications

## Defense

Defensive measures and detection strategies:

- Require multi-admin setups and alert on last-admin deletions
- Block deletions without secondary confirmation for critical roles
- Audit logs for cross-app deletion attempts and correlate with user sessions

## Objectives

1. Validate unauthorized access impact
2. Show DoS potential by isolating app management
3. Assess recovery failure (e.g., no reset emails)

## Instructions

### Step 1: Verify Standard Deletion

**Context**: Confirm non-admin user removal from victim app.

Log in as Aliceadmin, go to VictimApp > Team.

**Expected Output**: Alicemember absent from list.

### Step 2: Target Last Admin for DoS

**Context**: Modify request to delete Aliceadmin, the sole remaining user.

In Burp, update account_id to 54aa4c616bb166b8f300134a, keep app_id as VictimApp, replay.

**Command** ([[commands/fabric-delete-team-member-modified]]):

Adapted modified request:

```http
DELETE /accounts/54aa4c616bb166b8f300134a?app_id=54ad5e03a25bb8136b000002 HTTP/1.1
Host: fabric.io
```

> This deletes the last admin. Expected output: Success response, but app now inaccessible.

### Step 3: Test App Inaccessibility

**Context**: Demonstrate DoS effects.

Attempt login to VictimApp or password reset; no email sent, access denied.

**Expected Output**: Error messages or failed operations confirming isolation.

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

- verify
- dos
- impact

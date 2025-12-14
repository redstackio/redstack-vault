---
id: proc-004
tags:
  - verification
  - deletion-confirmation
  - database-removal
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:29:36.892Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Account Access Removal]]'
---
# Verify-Account-Deletion

## Summary

This procedure confirms the successful deletion of the victim's NordVPN account from the database, validating the exploit's impact through access denial or error indicators.

## Description

Post-processing, attempt to interact with the account (e.g., login) or check for removal signs. The vulnerability results in permanent loss of access and data, as the support action directly removes records from the database. This targets the web login and database backend, confirming the broken access control's severity.

## Requirements

1. Victim's credentials (email/password) for testing
2. Completion of prior procedures
3. Access to verification tools like browser or external checks

## Defense

Defensive measures and detection strategies:

- Post-deletion recovery mechanisms, such as account restoration with proof of ownership
- Monitor for unusual deletion patterns and notify affected users via alternate channels
- Implement immutable audit logs for all account modifications to trace unauthorized actions

## Objectives

1. Confirm account removal and access loss
2. Measure the exploit's success
3. Highlight potential data loss for victims

## Instructions

### Step 1: Attempt Victim Login

**Context**: Test if the account still exists by simulating legitimate access.

No command required; browser action:

Navigate to https://ucp.nordvpn.com/login/ and enter the victim's email and password.

> Expect failure messages like "Account not found" or "Deleted," confirming removal.

### Step 2: Check Database Indicators

**Context**: Use external or visual confirmations of deletion.

No command required; review evidence:

If available, check screenshots or logs showing pre/post deletion states (e.g., account visible before, absent after).

> Visual confirmation via images like 'v1.png' and 'v2.png' indicates database purge.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Account Access Removal]] Account Access Removal

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[verification]]
- [[deletion-confirmation]]
- [[database-removal]]

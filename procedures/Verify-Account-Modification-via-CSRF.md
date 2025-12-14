---
id: p2q3r4s5-t6u7-8901-cdef-234567890123
name: Verify-Account-Modification-via-CSRF
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.286Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - verification
  - account-discovery
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Verify-Account-Modification-via-CSRF

## Summary

This procedure confirms the success of a CSRF attack by inspecting the victim's account details post-exploitation, ensuring the email and other fields have been altered as intended.

## Description

Following the execution of a CSRF PoC on a vulnerable web application, such as the DoD portal's email change form, this step involves re-accessing the account settings to validate modifications. It assumes the attacker has a way to view the account (e.g., via victim session or secondary access). The process highlights the vulnerability's impact and prepares for the next stage of takeover. No tools are needed beyond a browser; outcomes include confirmation of unauthorized changes without triggering alerts.

## Requirements

1. Active session or access to the victim's account page
2. Knowledge of original account details for comparison
3. Recent execution of the CSRF PoC

## Defense

Defensive measures and detection strategies:

- Log all account modifications with timestamps and IP checks
- Require re-authentication for sensitive changes like email updates
- Implement anomaly detection for rapid field alterations

## Objectives

1. Confirm email change to attacker-controlled address
2. Identify any additional modified fields
3. Validate no security interruptions occurred

## Instructions

### Step 1: Re-Authenticate if Needed

**Context**: Ensure access to the account details page.

Log back into the application using the victim's credentials if the session expired. Navigate to the account settings or profile page.

### Step 2: Inspect Updated Fields

**Context**: Check for changes against the baseline.

Refresh the page and review the email field and other profile details. Compare to pre-attack values (e.g., email now shows attacker@evil.com).

**Expected Output**: Altered fields visible in the UI.

### Step 3: Document Changes

**Context**: Record for chain progression.

Screenshot or note the new values to confirm success before proceeding to password reset.

**Expected Output**: Evidence of modification for reporting or further use.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[account-verification]]
- [[csrf-followup]]

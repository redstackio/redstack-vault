---
tags:
  - hackerone
  - invitation-sending
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/ruby-redact-pii]]'
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5d4ce5b3-1451-4976-a93f-3232b1d97d46
created_at: '2025-12-11T06:10:15.678Z'
updated_at: '2025-12-11T06:10:15.678Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1213]]'
---
# Send Collaboration Invitation on HackerOne

## Summary

This procedure sends an invitation to added collaborators on a HackerOne report, updating their status to pending and enabling GraphQL request capture for email leaks.

## Description

Sending the invite triggers backend processes but does not require acceptance for the vulnerability to be exploitable. This step is crucial for the subsequent traffic capture.

## Requirements

1. Report with added collaborators.
2. Access to send invitations.
3. No acceptance needed from target.

## Defense

Defensive measures and detection strategies:

- Track invitation rates and flag suspicious activity.
- Add delays or captchas to invitation processes.

## Objectives

1. Activate pending status for collaborators.
2. Prepare for sensitive data exposure in requests.
3. Advance the attack chain toward disclosure.

## Instructions

### Step 1: Review Collaborators

**Context**: Confirm the list before sending.

Check the added users in the report.

> Ensure targets are listed.

### Step 2: Send the Invite

**Context**: Dispatch the invitation.

Click the send button.

> Status changes to pending.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[hackerone]]
- [[invitation-sending]]

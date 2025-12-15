---
id: 123e4567-e89b-12d3-a456-426614174001
name: HackerOne-2FA-Bypass-via-Collaborator
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.444Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - 2fa-bypass
  - business-logic
  - authentication-bypass
  - hackerone
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# HackerOne-2FA-Bypass-via-Collaborator

## Summary

This procedure exploits a business logic error in the HackerOne platform where 2FA is enforced only for report submitters in mandatory programs, but not for invited collaborators, allowing unauthorized access to sensitive vulnerability reports.

## Description

The HackerOne platform requires 2FA for submitting reports in certain programs to protect sensitive vulnerability details from compromised credentials. However, the collaboration feature does not extend this enforcement to invitees. By submitting a report with a 2FA-enabled account and inviting a non-2FA account, the invitee can accept and access the report without 2FA verification. This bypasses the security control, exposing high-impact information like proof-of-concepts and affected systems. The attack requires no technical exploits, only account manipulation and platform navigation, making it accessible to intermediate users targeting HackerOne-hosted bug bounty programs.

## Requirements

1. Access to the HackerOne website (hackerone.com) with ability to register free accounts
2. Two distinct email addresses for account creation
3. A target program on HackerOne that mandates 2FA for reporters and enables collaborations
4. Basic web browser for manual interactions (no proxies or automation needed)

## Defense

Defensive measures and detection strategies:

- Enforce 2FA uniformly for all report participants, including collaborators, during invitation acceptance
- Implement invitation validation to check invitee's 2FA status before granting access
- Monitor for anomalous collaboration patterns, such as frequent invites from 2FA accounts to non-2FA ones
- Audit report access logs for non-2FA users in 2FA-required programs and revoke access if detected

## Objectives

1. Bypass 2FA requirements to access protected vulnerability reports
2. Demonstrate unauthorized exposure of sensitive security information
3. Highlight business logic flaws in access control enforcement

## Instructions

### Step 1: Create Dual Accounts

**Context**: Set up Account A (2FA-enabled) for submission and Account B (non-2FA) for bypass.

Manual steps: Visit hackerone.com, register Account A, log in, go to settings, enable 2FA (e.g., via authenticator app). Register Account B separately without enabling 2FA.

> Verify by logging into each: Account A should prompt 2FA on login; Account B should not.

### Step 2: Identify Target Program

**Context**: Locate a program with 2FA mandate and collaboration support to ensure the flaw applies.

Manual steps: Log in as Account A, search for programs, review each program's policy page for "2FA required" and confirm collaboration invites are allowed.

> Expected: Policy text confirming 2FA for reporters; no restrictions on collaborator 2FA.

### Step 3: Initiate Report and Invite

**Context**: Start report creation to embed the collaborator invitation.

Manual steps: With Account A, select the program, click "New Report," enter placeholder vulnerability details, and add Account B's email/username in the collaborators section.

> Expected: No errors on adding collaborator; invitation ready for submission.

### Step 4: Submit Report

**Context**: Trigger submission to enforce 2FA on the primary account and send the invite.

Manual steps: Complete the report form, submit, and authenticate with Account A's 2FA code.

> Expected: Success message; email/notification sent to Account B.

### Step 5: Confirm Invitation Delivery

**Context**: Ensure the non-2FA account receives the access grant.

Manual steps: Check Account B's email or HackerOne dashboard for the invitation.

> Expected: Link to accept collaboration without 2FA prompt.

### Step 6: Accept and Verify Access

**Context**: Gain and confirm unauthorized read access to sensitive content.

Manual steps: Log in as Account B, click accept, navigate to the report page.

> Expected: Full view of report details (e.g., vulnerability narrative, attachments) without 2FA.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[2fa-bypass]]
- [[business-logic]]
- [[authentication-bypass]]
- [[hackerone]]

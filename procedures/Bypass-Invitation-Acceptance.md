---
id: p2b3c4d5-e6f7-8901-bcde-f23456789012
name: Bypass-Invitation-Acceptance
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:42.488Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - auth-bypass
  - invitation-bypass
platforms:
  - Web
tools:
  - '[[tools/Google-Authenticator]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Bypass-Invitation-Acceptance

## Summary

This procedure exploits the unverified 2FA state to accept private program invitations on HackerOne, gaining unauthorized access to sensitive program details and participant lists without completing proper verification.

## Description

With unlinked 2FA enabled, the platform's invitation acceptance process does not re-enforce 2FA validation. An attacker navigates to the dashboard, locates an invitation, and accepts it directly, bypassing the intended security logic. This targets the HackerOne web interface and results in disclosure of private data. Prerequisites include an unlinked 2FA setup and pending invitations.

## Requirements

1. Unlinked 2FA already enabled on the account
2. Pending program invitation in HackerOne dashboard
3. Browser access to HackerOne

## Defense

Defensive measures and detection strategies:

- Implement invitation acceptance gates that require fresh 2FA code entry
- Monitor for acceptances from accounts with recent 2FA changes
- Audit access logs for private program views without full auth trails

## Objectives

1. Accept invitations without 2FA re-verification
2. Access private program dashboards and participant info
3. Confirm information disclosure vulnerability

## Instructions

### Step 1: Navigate to Invitation

**Context**: Locate the program invitation in the dashboard using the unverified 2FA session.

Log in to HackerOne and go to the invitations section or click the provided invitation link.

> The dashboard loads normally with 2FA considered active.

### Step 2: Accept Invitation

**Context**: Click accept to bypass verification and gain access.

Select the invitation and click the 'Accept' button. No additional 2FA prompt appears due to the misconfiguration.

> Success grants immediate view of program details and full list of participating hackers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Authenticator]]

## Tags

- [[auth-bypass]]
- [[invitation-bypass]]

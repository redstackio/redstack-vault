---
id: p3c4d5e6-f7g8-9012-cdef-345678901234
name: Manipulate-2FA-for-Duplicate-Access
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:42.478Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Information Repositories]]'
sub_techniques: []
tags:
  - 2fa-manipulation
  - information-disclosure
platforms:
  - Web
tools:
  - '[[tools/Google-Authenticator]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---

# Manipulate-2FA-for-Duplicate-Access

## Summary

This procedure disables and re-enables 2FA on HackerOne to trigger duplicate program invitations, allowing repeated unauthorized access to private data and confirming the system's failure to track prior acceptances.

## Description

By toggling 2FA off and on again (now linking via email), the platform resets invitation tracking, sending duplicates. Accepting these re-grants access without re-verification. This targets the 2FA and invitation subsystems in the web app, leading to persistent information disclosure. Requires prior unlinked 2FA and accepted invitations.

## Requirements

1. Previously enabled (unlinked) 2FA
2. Email access linked to the HackerOne account
3. Prior accepted invitation for testing duplicates

## Defense

Defensive measures and detection strategies:

- Track invitation states persistently across 2FA changes
- Rate-limit invitation sends and require manual approval for duplicates
- Detect rapid 2FA disable/enable patterns via logging

## Objectives

1. Trigger duplicate invitations through 2FA manipulation
2. Re-accept to disclose the same private information
3. Validate repeatable bypass without verification

## Instructions

### Step 1: Disable 2FA

**Context**: Turn off 2FA to reset the authentication state.

In HackerOne settings > Security, select to disable 2FA and confirm with current code.

> 2FA status changes to disabled, potentially resetting linked processes.

### Step 2: Re-enable 2FA with Email Linkage

**Context**: Re-activate 2FA, linking via email to trigger system re-invites.

Re-enter settings, enable 2FA, and use Google Authenticator codes while ensuring email is associated. Complete setup.

> This step causes the system to treat the account as newly verified, sending duplicate invitations.

### Step 3: Check and Accept Duplicates

**Context**: Verify duplicates and re-access data.

Monitor email for new invitation notices to the same programs. Click links and accept to confirm access.

> Duplicate acceptance reveals the same private program data and participants, proving the flaw.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Authenticator]]

## Tags

- [[2fa-manipulation]]
- [[information-disclosure]]

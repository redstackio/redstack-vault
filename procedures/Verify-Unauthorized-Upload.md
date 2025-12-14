---
tags:
  - verification
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:13.640Z'
sub_techniques: []
id: 9fb07eb5-dc01-40f2-b657-fb3aa3dd0a98
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Unauthorized-Upload

## Summary

This procedure confirms the success of the access bypass by reloading the target scoping form from the owner account and checking for the unauthorized attachment in the review section.

## Description

After the upload from the second account, switch back to the owner session and refresh the form. The vulnerability allows the attachment to appear without further authorization, proving data integrity compromise. This step validates the business logic error.

## Requirements

1. Owner account session
2. URL of the target scoping form
3. Recent upload from unauthorized account

## Defense

Defensive measures and detection strategies:

- Real-time attachment notifications to form owners
- Audit logs for cross-user attachments
- Immutable attachment records with provenance tracking

## Objectives

1. Observe the unauthorized file in the form
2. Confirm bypass impact on data integrity
3. Document evidence of the vulnerability

## Instructions

### Step 1: Switch to Owner Account

**Context**: Restore the original session.

**Command** (Manual):

Log out of second account and log back into owner account.

> Ensures viewing from authorized perspective.

### Step 2: Reload Form and Check Attachments

**Context**: Inspect the review section for new files.

**Command** (Manual Navigation):

Navigate to the scoping form URL and refresh the page, then go to review/submit.

> Look for the uploaded file (e.g., 'does not have a option to change his own permission.png').

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[hackerone]]

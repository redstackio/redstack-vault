---
id: proc-004
tags:
  - authorization-bypass
  - 2fa-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:48.535Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Report-via-Embedded-Form-Bypass

## Summary

This procedure exploits the embedded submission form to create and submit a vulnerability report, bypassing 2FA, blacklists, rate limits, and abuse checks via improper authorization.

## Description

The embedded endpoint (/uuid/embedded_submissions/new) invokes Interactors::Reports::Create.interact_without_authorization, skipping methods like can_create_report? and can_create_draft? that validate mfa_required_at, blacklisted_reporters, and limits. This allows unauthorized submissions to programs like Parrot Sec. Expected outcome: Report accepted without standard protections (CVSS 5.0).

## Requirements

1. Embedded form URL from prior procedure
2. HackerOne account (2FA disabled)
3. Test report details (title, description, attachments if needed)

## Defense

Defensive measures and detection strategies:

- Align embedded form authorization with standard interact methods
- Add explicit ACL checks in interact_without_authorization
- Audit submissions from embedded endpoints separately

## Objectives

1. Bypass 2FA and submit report successfully
2. Evade blacklists and rate limits
3. Demonstrate unauthorized access impact

## Instructions

### Step 1: Access Embedded Form

**Context**: Load the vulnerable endpoint.

Navigate to the embedded URL (e.g., https://hackerone.com/0a1e1f11-257e-4b46-b949-c7151212ffbb/embedded_submissions/new).

> Form loads without 2FA prompt.

### Step 2: Fill Report Details

**Context**: Prepare content to trigger creation.

Enter title (e.g., 'Test Bypass'), description, and any attachments.

> Fields accept input without validation errors.

### Step 3: Submit Report

**Context**: Execute submission to bypass checks.

Click submit; the interact_without_authorization skips ACL.

> Success: 'Report submitted' confirmation, report visible in program.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authorization-bypass
- 2fa-bypass

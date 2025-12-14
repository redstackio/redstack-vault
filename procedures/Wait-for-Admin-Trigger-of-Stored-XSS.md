---
tags:
  - xss-trigger
  - admin-context
type: procedure
tools:
  - '[[tools/xsshunter]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:20.212Z'
sub_techniques: []
id: 5405d72b-6a4f-4235-9ace-4c44ee31ef0f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Wait-for-Admin-Trigger-of-Stored-XSS

## Summary

This passive procedure waits for an administrator to access the infected user record, triggering the stored XSS payload in a high-privilege context.

## Description

After storage, the payload remains dormant until rendered in admin interfaces like /phnx/driver.aspx or /admin/OrgUnitList.aspx. This blind aspect relies on admin activity; requires monitoring setup. Outcomes include JS execution stealing admin cookies and exposing backend details.

## Requirements

1. Payload successfully stored
2. Admin panel access patterns known (e.g., user search)
3. Patience for trigger (may take hours/days)

## Defense

Defensive measures and detection strategies:

- Escape HTML in admin views using libraries like HtmlEncoder
- Role-based rendering to avoid user input in admin contexts
- Monitor for unexpected JS execution in logs

## Objectives

1. Achieve execution in privileged session
2. Leverage admin view for impact
3. Exfiltrate sensitive session data

## Instructions

### Step 1: Identify Potential Triggers

**Context**: Understand admin workflows that view user records.

**Instructions**: Research or infer admin URLs from source (e.g., user edit pages). No action; prepare for monitoring.

> Research step. Expected output: List of likely trigger paths.

### Step 2: Passive Monitoring Setup

**Context**: Position for detection of trigger without intervention.

**Instructions**: Ensure XSS Hunter is armed to capture any firing.

> Tool configuration. Expected output: Monitoring active.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/xsshunter]]

## Tags

- [[xss-trigger]]
- [[admin-context]]

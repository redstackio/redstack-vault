---
tags:
  - persistence
  - save-config
  - concrete-cms
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:35.378Z'
sub_techniques: []
id: b434bbf0-e5ed-4616-adcb-8c7d8fa38465
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Configuration-in-Concrete-CMS

## Summary

This procedure covers submitting the form to store the injected XSS payload persistently in the Concrete CMS database.

## Description

Without output escaping, the payload is saved raw into the configuration table, ensuring it renders as HTML/JS in the target view. This creates a stored vulnerability exploitable by any visitor, leading to session hijacking or phishing.

## Requirements

1. Payload already entered in the configuration field
2. Valid session to submit admin forms
3. No client-side validation blocking submission

## Defense

Defensive measures and detection strategies:

- Server-side input validation before database writes
- Audit logs for configuration changes with payload scanning
- Regular database scans for malicious patterns

## Objectives

1. Persist the payload without errors
2. Confirm storage for later triggering
3. Enable broad impact across users

## Instructions

### Step 1: Submit the Form

**Context**: Finalize the injection by saving to backend.

Click the 'Save' or 'Update Settings' button on the configuration page.

> A success message appears, and the payload is now stored in the CMS database.

### Step 2: Verify Save (Optional)

**Context**: Check if the change took effect without triggering.

Refresh the configuration page to see the payload reflected in the field.

> The input shows the malicious content, confirming persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Persistence]]
- [[save-config]]

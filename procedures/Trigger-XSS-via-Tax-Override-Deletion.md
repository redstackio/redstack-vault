---
id: proc-trigger-xss-deletion
tags:
  - xss
  - execution
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.824Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Tax-Override-Deletion

## Summary

This procedure triggers XSS execution by deleting a tax override linked to a malicious collection, exploiting unsanitized reflection of the collection name in the delete confirmation UI.

## Description

During the deletion of a 'Rest of World' tax override, Shopify renders the associated collection name without proper escaping, allowing the stored XSS payload to execute in the admin's browser. This leads to arbitrary JavaScript running with admin privileges, enabling session theft, keylogging, or data exfiltration. The attack relies on prior setup; browser context makes it stealthy.

## Requirements

1. Active tax override with malicious collection assigned
2. Admin browser session
3. Payload designed for onerror or similar events

## Defense

Defensive measures and detection strategies:

- Escape HTML in all delete confirmation dialogs
- Implement JS sandboxing or strict CSP in admin panels
- Monitor browser console for unexpected script execution via logging

## Objectives

1. Initiate delete action to reflect payload
2. Execute JavaScript in admin context
3. Demonstrate potential for account compromise

## Instructions

### Step 1: Locate Override

**Context**: Find the target override in settings.

Go to Settings > Taxes and duties > Tax overrides. Identify the 'Rest of World' entry.

### Step 2: Initiate Deletion

**Context**: Trigger the delete UI to process the collection name.

Click the recycle bin icon next to the override for 'Delete Entire Override'.

### Step 3: Confirm and Execute

**Context**: The confirmation step renders the unsanitized name, firing the payload.

Click 'Delete' in the confirmation dialog. Observe the prompt (e.g., prompt(7)) as in xss.png and delete.png.

> Payload executes due to lack of escaping; replace prompt(7) with more malicious code like document.cookie exfil for real impact.

**Expected Output**: JavaScript alert or action confirms success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[shopify]]

---
tags:
  - xss
  - reflected-xss
  - delete-trigger
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4994d54d-5386-4fc9-8e23-5dbf5bb783cb
created_at: '2025-12-14T17:28:45.037Z'
updated_at: '2025-12-14T17:28:45.038Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Delete-Override

## Summary

This procedure triggers the reflected XSS by deleting the tax override, causing the malicious collection name to be unsafely reflected in the confirmation UI and executing arbitrary JavaScript.

## Description

In Shopify's admin, initiating deletion of the override via the recycle bin icon renders the collection name in a dialog or error message without output encoding. The payload breaks out, executing JS in the admin's session context. This can lead to alerts, cookie theft, or further exploits. Requires the prior override setup; outcome is immediate JS execution.

## Requirements

1. Active tax override with malicious collection
2. Admin access to taxes settings
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Apply HTML entity encoding to user inputs in all UI renders
- Implement JS event handlers with safe attribute quoting
- Log and alert on JS errors or prompt executions in admin

## Objectives

1. Force reflection of unsanitized input
2. Achieve JS execution in high-privilege context
3. Enable follow-on attacks like session theft

## Instructions

### Step 1: Locate the Override

**Context**: Identify the target for deletion.

In Settings > Taxes > Rest of World, find the override linked to the malicious collection.

### Step 2: Initiate Deletion

**Context**: Click the delete action to trigger reflection.

Click the recycle bin icon next to the override to select 'Delete Entire Override'.

> This action queries and displays the collection name in the UI, reflecting `'><IMG SRC=x onerror=prompt(7)>` without escaping, causing the IMG tag to load (fail), and execute prompt(7).

### Step 3: Observe Execution

**Context**: Confirm the payload fires.

A prompt dialog should appear with '7', indicating successful XSS. Inspect the page source or console for the injected element.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[shopify]]
- [[ui-trigger]]

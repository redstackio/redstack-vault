---
id: proc-005
tags:
  - verification
  - impact-check
type: procedure
tools:
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:36.191Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify Kaspersky Feature Disabling Impact

## Summary

This procedure checks Kaspersky settings post-exploit to confirm that Anti-Banner and Private Browsing features have been disabled through the hijacked command interface.

## Description

After the malicious page executes, it uses the intercepted interface to send disable commands to Kaspersky's backend. Verification involves reopening settings to observe changes, demonstrating control over AV functionality and potential for further manipulations like blocklist additions or RCE.

## Requirements

1. Exploit executed successfully in previous steps
2. Access to Kaspersky settings
3. No immediate AV alerts blocking verification

## Defense

Defensive measures and detection strategies:

- Enable real-time logging in Kaspersky for command interface access
- Alert on feature state changes without user interaction
- Periodic scans for unauthorized AV modifications

## Objectives

1. Confirm disabling of protections
2. Validate namespace access success
3. Assess potential for escalated impacts like RCE

## Instructions

### Step 1: Reopen Settings

**Context**: Access configuration to check statuses.

Launch Kaspersky settings via tray icon or menu.

> Expected: Interface opens normally.

### Step 2: Inspect Features

**Context**: Review Web protection toggles.

Navigate to Anti-Banner and Private Browsing; note if disabled.

> Expected: Features off; logs may show command execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer]]

## Tags

- [[verification]]
- [[impact-check]]

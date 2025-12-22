---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - xss
  - execution
  - session-theft
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.419Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Admin-Activity

## Summary

This procedure triggers the stored XSS by having an admin generate an activity log entry, executing the injected JavaScript to steal session data and enable takeover.

## Description

When an admin performs actions like updating settings, Shopify logs the activity including the staff name, rendering it unsanitized. The payload executes in the admin's browser, allowing cookie access (e.g., via document.cookie) and potential exfiltration. Prerequisites: injected payload; outcomes: arbitrary code execution in high-privilege context.

## Requirements

1. Admin user with action-performing capabilities.
2. Stored payload in a staff name.
3. Monitoring for execution (e.g., alert or beacon).

## Defense

Defensive measures and detection strategies:

- Output encode all dynamic content in logs.
- Browser-based XSS auditors or extensions.
- Log and alert on JavaScript errors in admin sessions.

## Objectives

1. Render the malicious name in admin view.
2. Execute JavaScript for data collection.
3. Achieve session hijacking or account control.

## Instructions

### Step 1: Admin Login and Action

**Context**: Simulate or induce admin activity to create a log entry.

No specific command; admin logs in and updates store settings (e.g., change theme).

> Activity log generates, displaying the staff name.

### Step 2: Observe Execution

**Context**: Confirm XSS fires in the admin's browser.

No specific command; check for alert(2) or inspect network for exfil requests.

> Payload executes, e.g., stealing cookies via XMLHttpRequest to attacker server.

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

- xss-trigger
- admin-takeover
- cookie-theft

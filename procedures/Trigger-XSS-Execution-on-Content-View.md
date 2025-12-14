---
id: proc-stripo-xss-trigger-001
tags:
  - xss
  - execution
  - web
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
updated_at: '2025-12-14T03:15:30.751Z'
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
# Trigger-XSS-Execution-on-Content-View

## Summary

This procedure demonstrates how to trigger the stored XSS payload on the Stripo platform by having users view the injected content, causing JavaScript execution in their authenticated session for potential data collection.

## Description

After payload injection, viewing the stored content (e.g., an email template) renders the unsanitized input, executing the script in the browser's context. This affects any authenticated user accessing the page, enabling attacks like cookie theft. The procedure assumes the payload is already stored and focuses on delivery and confirmation of execution.

## Requirements

1. Stored payload from prior injection
2. Ability to share or access the affected content
3. Attacker-controlled endpoint for data reception

## Defense

Defensive measures and detection strategies:

- Output encoding for all rendered user content
- Browser-based XSS auditors or extensions
- Logging of unexpected script executions or outbound requests

## Objectives

1. Execute JavaScript in victim browser
2. Capture session data or perform actions
3. Validate impact through exfiltration

## Instructions

### Step 1: Deliver Content to Victim

**Context**: Share the vulnerable content to induce viewing.

Send a link to the affected email template or page via email or direct access on the platform.

### Step 2: Monitor for Execution

**Context**: Watch for the payload to run when the victim loads the page.

As the victim authenticates and views, the script executes. Use a payload that sends data to your server, e.g., via fetch or image src.

### Step 3: Confirm Exfiltration

**Context**: Verify data receipt to measure success.

Check server logs for incoming requests containing cookies or other data from the victim's session.

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

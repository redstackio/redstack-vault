---
id: proc-fanfootage-trigger-xss
tags:
  - xss
  - execution-trigger
  - session-theft
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.309Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Profile-View

## Summary

This procedure covers viewing the profile page post-upload to trigger the reflected XSS payload in FanFootage, resulting in JavaScript execution within the browser context for potential client-side attacks.

## Description

After upload, the Paperclip-handled filename is echoed unsanitized into the profile HTML (e.g., as alt text or src attribute), parsing the injected SVG and executing onload. This enables attacks like cookie theft (e.g., alert(document.cookie)) in the viewer's session. Tested in Firefox for execution; Chrome may block via XSS auditor. Outcomes include confirmed payload trigger and awareness of browser differences.

## Requirements

1. Successful upload from previous steps
2. Access to view the target profile (self or induced victim view)
3. Browser without strict XSS filtering (e.g., Firefox)

## Defense

Defensive measures and detection strategies:

- Apply output encoding to all user-controlled data in HTML (e.g., Rails' sanitize helper)
- Deploy browser-based protections like CSP and XSS filters
- Log and alert on anomalous JavaScript errors or unexpected onload events

## Objectives

1. Render the profile page to parse the malicious filename
2. Execute the injected JavaScript payload
3. Validate impact, such as alert or data exfiltration

## Instructions

### Step 1: Navigate to Profile View

**Context**: Load the page where the filename is reflected to initiate parsing.

After upload, go to the profile view page (e.g., /profile or /users/:id). If self-profile, refresh; for victim, share link to induce view.

> Expected: Page loads with image; inspect source to see raw filename insertion.

### Step 2: Observe Execution

**Context**: Monitor for payload trigger in the browser.

Watch for the alert(1) popup or check console for errors. In dev tools, verify SVG element injection and onload firing.

> Expected: JavaScript executes; in Firefox, alert shows; Chrome may log block.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[execution-trigger]]

---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
tags:
  - xss
  - self-xss
  - submission
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
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
updated_at: '2025-12-13T23:52:25.298Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Review-to-Trigger-Self-XSS

## Summary

This procedure completes the review form and submits it, causing the injected payload to reflect unsanitized and execute as self-XSS in the attacker's browser.

## Description

The final step in the chain submits the form with the malicious email, relying on the app's lack of server-side escaping. Target: Shopify review endpoint. Prerequisites: Payload injected. Impact: JS execution (alert) in submitter's session; potential stored if emails displayed publicly.

## Requirements

1. All form fields completed with payload in email
2. Valid store session
3. No CAPTCHA or additional checks

## Defense

Defensive measures and detection strategies:

- Escape HTML/JS in all reflected fields server-side
- Review app configurations to avoid public email display
- Monitor for XSS payloads in submission logs

## Objectives

1. Trigger payload reflection
2. Execute JS in browser
3. Validate self-XSS success

## Instructions

### Step 1: Complete Form Fields

**Context**: Fill required inputs to enable submission.

Enter a name, select a rating (e.g., 5 stars), and add neutral review text like 'Test review'.

### Step 2: Submit the Form

**Context**: Send data to server for processing and reflection.

Click the 'Submit Review' button. Observe the response page or confirmation where the email is echoed back.

> The payload executes immediately, showing an alert(1); the review is stored but only affects the attacker unless templates expose emails.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- xss
- self-xss
- submission

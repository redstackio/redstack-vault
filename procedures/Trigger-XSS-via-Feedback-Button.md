---
id: proc-uuid-4
tags:
  - xss
  - trigger-execution
  - javascript
type: procedure
tools:
  - '[[tools/Microsoft-Edge]]'
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.719Z'
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
# Trigger-XSS-via-Feedback-Button

## Summary

This procedure activates the stored XSS by interacting with the feedback button, causing the malicious JavaScript to execute in the browser.

## Description

Upon clicking "Condividi il tuo feedback", the unsanitized query parameter is processed, injecting and executing the payload (alert(1)) in the victim's session. This demonstrates arbitrary JS execution, potentially leading to cookie theft or phishing. The trigger relies on the page's feedback functionality mishandling the stored input.

## Requirements

1. Loaded page from previous step in vulnerable browser
2. Visible feedback button on the page
3. User interaction capability

## Defense

Defensive measures and detection strategies:

- Escape all outputs in event handlers and DOM insertions
- Implement client-side validation for feedback interactions
- Log and alert on JavaScript errors or unexpected popups

## Objectives

1. Execute the stored payload
2. Confirm XSS success via alert
3. Highlight potential for broader attacks like data exfiltration

## Instructions

### Step 1: Locate Feedback Element

**Context**: Identify the trigger point on the loaded page.

Scroll to the bottom or search for "Condividi il tuo feedback".

> The button/link should be in the page footer.

### Step 2: Interact to Trigger

**Context**: Perform the action that processes the stored payload.

Click the feedback button.

> This causes the JavaScript alert(1) to pop up, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Microsoft-Edge]]
- [[tools/Internet-Explorer]]

## Tags

- [[xss]]
- [[trigger-execution]]

---
id: proc-uuid-3
tags:
  - dom-xss
  - javascript-execution
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-13T23:52:24.816Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Malicious-Payload-via-Form

## Summary

This procedure triggers form submission in the clickjacking setup, exploiting the DOM XSS by inserting unsanitized user input into innerHTML, leading to arbitrary JavaScript execution in the victim's browser.

## Description

Clicking the decoy button submits the form, invoking JavaScript on the target site that replaces placeholders like '{{triager}}' and '{{username}}' in document.body.innerHTML with the tainted values from the form. Without escaping, this parses and executes embedded <script> tags. The attack requires user interaction but demonstrates potential for session hijacking or data theft in authenticated contexts; here, it's low-impact on a public site.

## Requirements

1. Populated form fields with payload from prior interaction
2. Active iframe in the PoC
3. No authentication on target

## Defense

Defensive measures and detection strategies:

- Sanitize inputs using textContent or DOM APIs instead of innerHTML
- Escape special characters in replacements (e.g., via encodeURIComponent)
- Implement CSP to block inline scripts

## Objectives

1. Submit form to trigger vulnerable handler
2. Execute injected JavaScript payload
3. Observe impact like alert popup

## Instructions

### Step 1: Trigger Submission

**Context**: Click the 'Make friends!' button to submit the hidden form.

No command; perform click action on the PoC button.

> The click propagates to the iframe's submit button, calling the JS handler.

### Step 2: Observe Execution

**Context**: Monitor for JavaScript execution in the browser.

Watch for the alert('XSS') popup or console logs.

> Expected: Arbitrary code runs in the site's origin context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[dom-xss]]
- [[javascript-execution]]

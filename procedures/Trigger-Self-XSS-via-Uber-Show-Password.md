---
tags:
  - xss
  - self-xss
  - uber
  - trigger
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
updated_at: '2025-12-14T03:15:47.283Z'
sub_techniques: []
id: 25d73f90-5867-4492-9323-4b54c55c93f0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Self-XSS-via-Uber-Show-Password

## Summary

This procedure submits the form with the injected payload and uses the 'show password' feature to reveal and execute the unsanitized XSS, resulting in JavaScript execution within the attacker's browser only.

## Description

After injecting the payload, proceed by clicking 'Continue' or 'Submit' on the form. Then, click the 'show password' button to display the new password in plain text, which lacks proper encoding and triggers the XSS on mouseover (e.g., via the img tag). This self-XSS executes only in the user's session, such as prompting the document domain, with no cross-user impact. Targeted at Uber's form, the outcome is confirmed payload execution.

## Requirements

1. Payload injected in the form
2. Form submission capability
3. Mouse interaction for trigger

## Defense

Defensive measures and detection strategies:

- HTML entity encoding when displaying passwords
- Disable or sanitize 'show password' output
- Browser CSP to block inline scripts

## Objectives

1. Execute the XSS payload
2. Verify self-execution without broader impact
3. Demonstrate vulnerability proof-of-concept

## Instructions

### Step 1: Submit Form

**Context**: Advance to the display phase.

Click the 'Continue' or 'Reset Password' button to process the input.

> The form may show a confirmation or error, but the password value persists.

### Step 2: Toggle Show Password

**Context**: Reveal the unsanitized payload.

Click the 'show password' eye icon to display the field in plain text.

> The payload renders as HTML, injecting the img tag.

### Step 3: Trigger Execution

**Context**: Interact to fire the event.

Hover the mouse over the revealed password area.

> A prompt appears showing 'partners.uber.com', confirming XSS execution.

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
- [[self-xss]]
- [[uber]]
- [[trigger]]

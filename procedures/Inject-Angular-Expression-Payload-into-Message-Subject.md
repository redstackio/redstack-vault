---
tags:
  - xss
  - injection
  - angular
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
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f0997a36-f42c-423f-8c64-7a3b2a7ecb2d
created_at: '2025-12-13T23:55:20.666Z'
updated_at: '2025-12-13T23:55:20.666Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Angular Expression Payload into Message Subject

## Summary

This procedure demonstrates injecting a malicious Angular expression into the Subject field of a FetLife private message, storing it for execution on the recipient's browser without triggering server-side filters.

## Description

Targeting FetLife's onsite chat feature, this step involves crafting and sending a message where the Subject field contains Angular syntax (e.g., `{{constructor.constructor('alert(1)')()}}`) that bypasses basic input validation. The payload is stored in the application's database and rendered unsafely in the recipient's Angular view, leading to JavaScript execution. This requires an authenticated session and a target recipient. Outcomes include successful payload delivery, enabling potential session hijacking or data theft.

## Requirements

1. Authenticated FetLife session
2. Target recipient account (e.g., a controlled test account)
3. Knowledge of Angular expression payloads for XSS

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs server-side to strip or escape Angular directives
- Employ strict CSP headers to block inline script execution
- Log and alert on suspicious patterns in message subjects, such as double curly braces

## Objectives

1. Deliver a stored payload via the vulnerable Subject field
2. Ensure the injection persists without modification
3. Prepare for client-side execution in the victim's context

## Instructions

### Step 1: Compose the Malicious Message

**Context**: Prepare the payload in the Subject field to exploit Angular's expression evaluation.

In the new conversation form, enter a payload like `{{constructor.constructor('alert("XSS")')()}}` into the Subject field. Add innocuous body text to the message to avoid suspicion.

### Step 2: Send the Message

**Context**: Submit the message to store the payload in the backend.

Select a recipient and click "Send." Verify in your sent messages that the subject appears with the payload intact.

> Server acceptance without errors indicates successful injection.

### Step 3: Confirm Storage

**Context**: Check that the payload is retrievable and unmodified.

Log in as the recipient or use another session to view the inbox, ensuring the subject displays the raw expression without evaluation yet.

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
- [[injection]]
- [[angular]]

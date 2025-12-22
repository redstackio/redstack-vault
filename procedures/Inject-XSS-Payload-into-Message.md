---
tags:
  - xss-injection
  - payload-injection
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
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
updated_at: '2025-12-14T03:46:37.181Z'
sub_techniques: []
id: 3a87b76c-400e-4ed6-a60b-195ef1b52f21
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Message

## Summary

This procedure injects a JavaScript payload into the project message content field on TopCoder Connect, exploiting the lack of sanitization to store malicious code that executes on victim views.

## Description

The message content input does not properly escape HTML or JavaScript, allowing tags like <script> to be stored and rendered. A simple payload like <script>alert('XSS')</script> tests execution; advanced payloads can exfiltrate data. This targets the POST submission to the messages endpoint. Outcome is payload persistence until viewed post-approval.

## Requirements

1. Access to project messages interface
2. Knowledge of basic JavaScript for payloads
3. Browser developer tools for testing

## Defense

Defensive measures and detection strategies:

- Apply HTML entity encoding to user inputs
- Strip or block script tags during storage
- Scan messages for known XSS patterns

## Objectives

1. Submit unsanitized JavaScript
2. Store payload in the database
3. Await victim interaction for execution

## Instructions

### Step 1: Prepare Payload

**Context**: Craft a test XSS payload.

Use <script>alert('XSS')</script> for proof-of-concept.

> For production, replace alert with data exfiltration, e.g., document.cookie to a server.

### Step 2: Submit Message

**Context**: Enter and post the payload.

In the messages form, add a random title and the payload as content, then submit.

> Verify submission succeeds without client-side blocking.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- xss-injection
- payload-injection

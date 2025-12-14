---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
name: Trigger-and-Detect-Blind-XSS-Execution
tags:
  - xss
  - execution
  - detection
type: procedure
tools:
  - '[[tools/Custom-Blind-XSS-Application]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.076Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Detect-Blind-XSS-Execution

## Summary

This procedure monitors for the execution of the injected blind XSS payload when an admin views the tainted review, allowing arbitrary JavaScript in the admin's browser for data exfiltration or further attacks.

## Description

Once injected, the payload remains dormant until an admin accesses the review in their portal (e.g., https://app.pullrequest.com/admin-portal). Reflection occurs without encoding in elements like <div id="feedback-types-content">, triggering onerror to eval base64 code that callbacks to the attacker's server. This enables collection of admin session data or navigation to sensitive pages.

## Requirements

1. Running blind XSS detection server
2. Patience for admin interaction (may take hours/days)
3. Access to logs on attacker server

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected user content in admin interfaces
- Use strict XSS filters and output encoding (e.g., OWASP guidelines)
- Alert on anomalous JavaScript execution in browser consoles

## Objectives

1. Confirm payload execution in admin context
2. Receive callback for proof-of-concept
3. Assess impact (e.g., session theft potential)

## Instructions

### Step 1: Monitor Detection Server

**Context**: Wait for admin to trigger the view.

Use [[tools/Custom-Blind-XSS-Application]] hosted at attacker domain.

> Logs incoming requests; decode base64 from id attribute.

### Step 2: Analyze Callback

**Context**: Verify execution details.

Check server logs for payload data, e.g., alert or XHR to sensitive endpoints.

> Expected: HTTP GET/POST to attacker server with execution confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] Command and Scripting Interpreter: JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Blind-XSS-Application]]

## Tags

- [[xss]]
- [[Execution]]

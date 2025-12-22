---
tags:
  - xss
  - stored-xss
  - shopify
  - judge.me
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2d958ca0-c310-4aaa-91db-a4e0e60e8a4b
created_at: '2025-12-14T03:16:19.930Z'
updated_at: '2025-12-14T03:16:19.930Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Edit-Question-to-Trigger-XSS

## Summary

This procedure triggers the stored XSS by editing the question in the Shopify admin via Judge.me, where the product name is reflected unsafely, executing the payload in the admin's authenticated session.

## Description

The core exploitation occurs in the Judge.me admin interface for managing questions. When an admin edits a question linked to the malicious product, the app renders the product name directly into the HTML without escaping, leading to JavaScript execution. This can steal admin cookies (e.g., by modifying the payload to send document.cookie to an attacker server) or perform other actions like keylogging. Requires admin access or social engineering to prompt an admin to edit.

## Requirements

1. Shopify admin credentials
2. Submitted question referencing the malicious product
3. Judge.me app access in admin panel

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) to all dynamic content in admin views
- Use Content Security Policy (CSP) to restrict inline scripts and eval
- Implement session monitoring and anomaly detection for unexpected JavaScript prompts in admin

## Objectives

1. Cause reflection of the unsanitized product name
2. Execute JavaScript in the admin browser context
3. Enable data exfiltration or session hijacking

## Instructions

### Step 1: Access Admin Questions

**Context**: Log in as admin and navigate to the Judge.me question management.

Go to Shopify admin > Apps > Judge.me Product Reviews > Questions to view pending or existing questions.

### Step 2: Initiate Edit

**Context**: Select and edit the target question to load the vulnerable interface.

Find the question tied to the malicious product, click the edit button. The editing view will immediately reflect the product name, triggering the XSS payload (e.g., a prompt with document.domain).

> If the payload is '<img src=x onerror=prompt(document.domain)>', a alert box will pop up confirming execution in the admin domain.

### Step 3: Validate Execution

**Context**: Observe and modify payload for impact assessment.

Check browser console for errors or execution; for real attacks, replace prompt with fetch to exfiltrate data like session tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[stored-xss]]
- [[shopify]]
- [[judge.me]]

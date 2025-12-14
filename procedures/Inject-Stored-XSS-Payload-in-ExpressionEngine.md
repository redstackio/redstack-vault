---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - xss
  - stored-xss
  - injection
  - expressionengine
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.227Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-ExpressionEngine

## Summary

This procedure exploits insufficient input sanitization in ExpressionEngine to inject a stored XSS payload into user-submittable fields like comments or entries, allowing the script to be persistently rendered and executed for subsequent visitors.

## Description

In vulnerable versions of ExpressionEngine, certain form inputs fail to properly sanitize or encode user-supplied data before storing it in the database. An attacker can submit JavaScript payloads that, when displayed to other users, execute in their browser context. This can lead to session hijacking, credential theft, or further exploitation. The procedure assumes access to a public-facing form and relies on the payload evading basic filters.

## Requirements

1. Access to a vulnerable ExpressionEngine instance with user input forms (e.g., comments enabled)
2. Basic knowledge of JavaScript payloads and HTML encoding
3. Network connectivity to submit and observe the payload

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., htmlspecialchars in PHP)
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in database-stored content

## Objectives

1. Persist malicious JavaScript in the application's data store
2. Ensure payload executes without alteration in user views
3. Enable follow-on attacks like data exfiltration

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a form field in ExpressionEngine that accepts and stores user input without proper sanitization, such as a blog comment or custom field.

Navigate to a comment-enabled page and inspect the form using browser developer tools.

### Step 2: Craft and Submit Payload

**Context**: Create a simple test payload to confirm storage and execution, escalating to more complex ones for exploitation.

Submit the following payload in the input field:

```html
<script>alert('Stored XSS in ExpressionEngine');</script>
```

> This payload is stored in the database. Upon submission, view the page source as another user to confirm it's rendered unescaped.

### Step 3: Verify Storage and Rendering

**Context**: Confirm the payload is stored and displayed without encoding.

Load the affected page in an incognito browser session and check for the alert triggering on load.

> Expected output: JavaScript alert pops up, indicating successful storage and execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection

---
id: proc-mixmax-xss-injection
tags:
  - xss
  - stored-xss
  - injection
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
updated_at: '2025-12-14T03:16:25.096Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Script-into-Mixmax-Contact-Name

## Summary

This procedure exploits a stored XSS vulnerability in the contact names field on compose.mixmax.com by injecting a malicious JavaScript payload. The payload is stored in the backend and executes in the browser of any user who views the affected contact, potentially leading to session hijacking, data exfiltration, or further attacks.

## Description

The vulnerability stems from insufficient input sanitization or escaping of contact names, allowing attackers with account access to inject scripts. Discovered in 2017 and reported via HackerOne, it affects the compose.mixmax.com interface. In an attack scenario, an authenticated user creates a contact with an XSS payload in the name field. When other users (or the attacker in a self-view) access the contacts, the unsanitized name renders the script, executing it in their context. Expected outcomes include arbitrary code execution, such as alerting, cookie theft, or phishing overlays. Prerequisites include a Mixmax account and basic web knowledge.

## Requirements

1. Authenticated session to compose.mixmax.com
2. Web browser with JavaScript enabled
3. Knowledge of XSS payloads (e.g., via OWASP resources)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for all user inputs
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript execution in browser logs or WAF alerts

## Objectives

1. Inject and persist malicious script in contact data
2. Trigger execution in victim browsers
3. Achieve arbitrary JavaScript execution for further exploitation

## Instructions

### Step 1: Authenticate and Navigate to Contact Creation

**Context**: Log in to establish a session and access the contact management interface.

Navigate to https://compose.mixmax.com and sign in with valid credentials. Then, go to the contacts section and select 'Add New Contact'.

### Step 2: Inject XSS Payload

**Context**: Enter the malicious payload in the name field to bypass sanitization.

In the 'Name' field, input a payload such as:

```html
<script>alert('Stored XSS Executed');</script>
```

Fill other fields minimally (e.g., email with a dummy value) and save the contact.

> This stores the script server-side without execution at injection time.

### Step 3: Trigger Execution

**Context**: View the contact to render the unsanitized name and execute the script.

Return to the contacts list or search for the injected contact. The name will render, executing the script in the current browser session.

> Successful execution appears as an alert dialog or console log; in real attacks, replace with data-exfiltrating code like sending cookies to an attacker-controlled server.

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
- stored-xss
- web-exploit

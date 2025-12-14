---
tags:
  - xss
  - stored-xss
  - blind-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-submit-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.562Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: e1245394-7053-4823-9174-c52cfac93428
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Stored-Blind-XSS-in-Contact-Form

## Summary

This procedure exploits a stored blind XSS vulnerability in a web contact form by injecting a malicious JavaScript payload into the message field, which is stored unsanitized and sent to a backend middleware server for admin processing, potentially leading to session hijacking or data exfiltration.

## Description

In the context of the Mapbox contact form at www.mapbox.com/contact, user input in the message field is not properly escaped before being forwarded to a middleware server. An attacker submits a payload like `<script>alert('XSS')</script>` or a more advanced one (e.g., using a beacon to exfiltrate cookies). The payload is stored blindly (no immediate execution feedback) and executes when an administrator views the message in their dashboard or email client. This can compromise admin sessions, steal sensitive data, or perform further attacks. The vulnerability was reported on HackerOne, earning a $750 bounty, and fixed by implementing proper escaping.

## Requirements

1. Public access to the target website (e.g., www.mapbox.com/contact)
2. Basic HTTP client like curl or a web browser for form submission
3. Knowledge of XSS payloads (e.g., JavaScript for alerts or data theft)

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output escaping (e.g., using HTML entity encoding) on all user inputs before storage or transmission
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous form submissions or JavaScript in logs
- Employ Web Application Firewalls (WAF) to detect XSS patterns

## Objectives

1. Inject and store a malicious XSS payload without detection
2. Achieve JavaScript execution in the context of an admin user
3. Compromise sessions or collect sensitive information from admins

## Instructions

### Step 1: Prepare the Target Endpoint

**Context**: Identify the contact form endpoint, typically a POST to /contact, and craft a payload that evades basic filters (e.g., <script>alert(document.cookie)</script> for cookie theft).

No command needed; review the form via browser dev tools to confirm fields (name, email, message).

### Step 2: Submit the Malicious Payload

**Context**: Use an HTTP POST request to submit the form with the XSS payload in the message field, simulating a legitimate contact submission.

**Command** ([[commands/curl-submit-xss-payload]]):
```bash
curl -X POST https://www.mapbox.com/contact \
  -d "name=TestUser" \
  -d "email=test@example.com" \
  -d "message=<script>alert('XSS')</script>" \
  -d "submit=Send"
```

> This command sends the form data, injecting the payload. Expected output is a success response (e.g., 200 OK or redirect). The payload is stored and forwarded to the middleware server without sanitization.

### Step 3: Verify Execution (Blind)

**Context**: Since it's blind XSS, monitor external callbacks (e.g., if payload includes an img src to attacker-controlled server) or wait for admin interaction confirmation via report.

No command; use tools like Burp Collaborator for beacon verification if advanced payload used.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[blind-xss]]
- [[web]]

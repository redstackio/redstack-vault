---
id: proc-uuid-3
tags:
  - csrf
  - xss
  - poc
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:35.938Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Create-and-Test-CSRF-PoC-for-XSS-Trigger

## Summary

This procedure generates an HTML-based proof-of-concept that auto-submits a forged POST request with an XSS payload, exploiting CSRF to trigger JavaScript execution in the victim's authenticated session.

## Description

The PoC simulates a malicious webpage that the victim visits, automatically forging the vulnerable POST without their knowledge. It uses hidden forms and JavaScript for submission, bypassing interactions. This chains CSRF with XSS for impacts like cookie theft. Requires prior identification of the endpoint and payload.

## Requirements

1. Valid XSS payload and vulnerable endpoint details
2. Burp Suite for PoC generation
3. Hosting capability for the malicious HTML

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and validate referer/origin headers
- Use HTTPS and HSTS to prevent MITM
- Detect auto-submissions via behavioral analysis in WAF

## Objectives

1. Forge POST request from external domain
2. Trigger XSS execution silently
3. Achieve session access or data exfiltration

## Instructions

### Step 1: Generate HTML Form

**Context**: Create a basic HTML structure with a form targeting the vulnerable endpoint.

Use Burp's 'Generate CSRF PoC' feature:

In Burp Repeater, right-click the request and select 'Engagement tools > Generate CSRF PoC' to create the HTML with hidden fields for 'answer' containing the encoded payload.

> Expected output: HTML file with <form method="POST" action="https://target/redacted"> and input for answer.

### Step 2: Add Auto-Submission Script

**Context**: Enhance the PoC to submit without user input using JavaScript.

Edit the HTML to include:

<script>document.forms[0].submit(); history.pushState({}, '', location.href);</script>

> Expected output: Form auto-submits on load, with URL unchanged to avoid suspicion.

### Step 3: Test and Deploy

**Context**: Verify the PoC triggers XSS when visited by an authenticated user.

Host the HTML and access while proxied through Burp:

Observe the POST in Burp and confirm XSS alert in the target's response.

> Expected output: Successful POST from external site, followed by JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[xss]]
- [[poc]]

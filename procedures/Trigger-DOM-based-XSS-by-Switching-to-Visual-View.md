---
id: proc-938683-step4
tags:
  - xss-trigger
  - javascript-execution
  - dom-manipulation
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.665Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger DOM-based XSS by Switching to Visual View

## Summary

This procedure finalizes the XSS attack by returning to visual mode in the Froala editor, causing the injected HTML to parse and execute JavaScript for cookie theft and potential account takeover.

## Description

The DOM-based nature of this vulnerability stems from Froala's failure to escape srcdoc attributes during view transitions, allowing script execution in the browser context. Impact includes stealing session cookies (non-HttpOnly), DOM rewriting for fake forms, and session hijacking. Validate by observing JS alerts or network requests.

## Requirements

1. Malicious payload injected in code view from prior step
2. Active editor session in lemlist
3. Attacker server for exfiltration (optional for proof-of-concept)

## Defense

Defensive measures and detection strategies:

- Set HttpOnly flags on session cookies to prevent JS access
- Use strict DOMPurify or similar for HTML sanitization in editors
- Detect XSS via browser security logs or WAF rules on anomalous JS

## Objectives

1. Execute arbitrary JS in lemlist domain context
2. Exfiltrate session cookies for takeover
3. Demonstrate impact like alert or data leak

## Instructions

### Step 1: Switch Back to Visual View

**Context**: Render the HTML to trigger parsing and execution.

Click the visual view toggle button to exit code mode.

> Froala parses the content, rendering the iframe and firing the onerror event.

### Step 2: Validate Execution

**Context**: Confirm XSS and assess impact.

Observe the alert popup (for test payload) or check network tab for exfiltration. For takeover, use stolen cookies in a new session.

> JS runs; cookies can be inspected via document.cookie in console.

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

- xss-trigger
- cookie-theft

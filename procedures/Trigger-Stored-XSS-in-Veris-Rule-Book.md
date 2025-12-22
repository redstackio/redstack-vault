---
id: proc-002
tags:
  - xss
  - stored-xss
  - execution
  - veris
  - cookie-theft
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.739Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-Veris-Rule-Book

## Summary

This procedure triggers the execution of stored XSS payloads by accessing the View Rule Book feature in the Veris application, where unsanitized group details are reflected, leading to JavaScript execution in the attacker's or victim's browser for data exfiltration like cookie theft.

## Description

After payloads are stored via the Edit Group Details form, the View Rule Book section retrieves and displays this data without proper escaping, causing the JavaScript to execute in the browser's context. This can reveal sensitive information such as session cookies or domain details, enabling further attacks like account takeover. The procedure focuses on the reflection and execution phase, assuming prior injection, and is effective against any user viewing the Rule Book, making it a persistent threat.

## Requirements

1. Prior successful injection of payloads into group details
2. Access to the View Rule Book feature, potentially as an admin or any viewer
3. Web browser to observe execution

## Defense

Defensive measures and detection strategies:

- Sanitize all output in dynamic content displays like the Rule Book using HTML entity encoding
- Implement strict CSP headers to block unsafe-inline scripts
- Log and alert on JavaScript errors or unexpected popups in the application
- Conduct regular input/output validation audits

## Objectives

1. Reflect stored payloads to trigger execution
2. Capture and exfiltrate browser data like cookies
3. Confirm vulnerability impact through observable effects

## Instructions

### Step 1: Navigate to View Rule Book

**Context**: Load the feature that reflects the stored group data.

Manually access the 'View Rule Book' section in the Veris app.

> Expected: Page loads with embedded group details.

### Step 2: Render the Content

**Context**: Force the browser to parse and execute the reflected HTML/JS.

Simply view the page; no interaction needed for auto-executing payloads.

> For testing, ensure the browser allows popups. Expected: Payloads trigger on load.

### Step 3: Validate Execution

**Context**: Observe and capture the results of JS execution.

Look for alert dialogs displaying `document.domain` or `document.cookie`.

> In a real attack, replace alerts with exfiltration to an attacker-controlled server, e.g., via `fetch()`. Expected: Sensitive data exposed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]
- [[tools/Google-Chrome]]

## Tags

- xss
- stored-xss
- veris
- execution

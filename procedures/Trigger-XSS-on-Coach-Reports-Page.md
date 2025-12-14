---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - execution
  - collection
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
updated_at: '2025-12-14T03:16:08.079Z'
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
# Trigger-XSS-on-Coach-Reports-Page

## Summary

This procedure triggers the execution of the persisted XSS payload by accessing the coach reports grid, where the malicious class name is rendered, leading to arbitrary JavaScript execution in the victim's browser.

## Description

Once the malicious class is created, navigating to the coach reports page causes the backend to fetch and render class data in HTML or JSON, inserting the unsanitized payload into a script context. This allows breakout and execution of injected code, such as alerts or more sophisticated payloads for session hijacking. The vulnerability stems from improper escaping as detailed in resources on preventing XSS in JSON responses.

## Requirements

1. Access to the coach reports feature (requires coach role or equivalent permissions)
2. The malicious class already created from prior procedure
3. Web browser to load the reports page

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before rendering in HTML/JSON (e.g., encode quotes and script delimiters)
- Use strict CSP headers to block unsafe-inline scripts
- Log and alert on JavaScript errors or unexpected onload events in reports

## Objectives

1. Render the persisted payload to execute JavaScript
2. Demonstrate impact through alert or data exfiltration
3. Collect sensitive information from the victim's session

## Instructions

### Step 1: Navigate to Reports

**Context**: Access the specific coach reports endpoint where class data is rendered.

Log in with a coach account and go to https://www.khanacademy.org/coach/reports/grid?force=1. Ensure the malicious class is visible in the grid view.

### Step 2: Observe Execution

**Context**: Load the page to trigger rendering of the class name, executing the payload.

The page will automatically fetch and display the reports grid. The payload `'</script>"><img src=x onerror=alert(0)>` will execute, popping an alert(0) dialog.

> Success is indicated by the alert firing immediately upon page load, confirming client-side JavaScript execution.

### Step 3: Validate Impact

**Context**: Inspect the page to confirm the vulnerability and potential for escalation.

Use browser developer tools (F12) to inspect the rendered HTML. Look for the injected `<img>` tag in the script context and test escalating payloads, e.g., replacing alert(0) with `alert(document.cookie)` to exfiltrate cookies.

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
- [[Collection]]

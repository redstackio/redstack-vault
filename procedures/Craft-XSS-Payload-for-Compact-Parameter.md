---
id: proc-craft-xss-payload-compact
tags:
  - xss
  - payload-crafting
  - javascript
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
updated_at: '2025-12-13T23:52:38.880Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payload-for-Compact-Parameter

## Summary

This procedure details the creation of a reflected XSS payload targeting the 'compact' parameter in Revive Adserver's admin search, enabling JavaScript injection to steal session data.

## Description

The vulnerability allows payloads to close the input tag and inject a script due to unescaped HTML output. A basic payload like compact=1'><script>alert(document.cookie)</script> exploits this by terminating the value attribute early and executing code in the browser context. This can be extended for more advanced actions like sending cookies to an attacker-controlled server.

## Requirements

1. Knowledge of HTML attribute injection techniques
2. Access to a test instance of Revive Adserver 5.5.2
3. Web browser with developer console for payload testing

## Defense

Defensive measures and detection strategies:

- Enforce strict output encoding in templates using context-aware escaping
- Monitor for unusual JavaScript execution via browser security tools
- Implement Web Application Firewall (WAF) rules to block common XSS patterns

## Objectives

1. Develop a functional payload that executes JavaScript
2. Test payload reflection without causing errors
3. Ensure payload evades basic filters if present

## Instructions

### Step 1: Design Basic Payload

**Context**: Create a payload to break out of the input value and inject a script tag.

Construct the payload: compact=1'><script>alert(document.cookie)</script>. The '1'' closes the value, > closes the tag, and <script> injects executable code.

> Test by appending to a local URL parameter; expect an alert with cookies on page load.

### Step 2: Test and Refine Payload

**Context**: Validate the payload in a controlled environment to confirm execution.

Navigate to http://localhost/www/admin/admin-search.php?compact=1'><script>alert('XSS')</script> in a browser. Open the console to verify script runs and no syntax errors occur.

> Refinements may include URL encoding (%27 for ') if needed, ensuring cross-browser compatibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-crafting]]

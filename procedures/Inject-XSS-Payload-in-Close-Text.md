---
tags:
  - xss
  - payload-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 20de9cde-f2f8-4b8c-bf3e-f8e11c7a56a0
created_at: '2025-12-14T03:16:14.378Z'
updated_at: '2025-12-14T03:16:14.378Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Close-Text

## Summary

This procedure injects a crafted XSS payload into the 'Close text' parameter of the Revive Adserver Invocation Code form, exploiting insufficient sanitization to reflect JavaScript back to the user.

## Description

The Close text field in the Invocation Code section fails to properly escape user input, allowing HTML and JavaScript tags to be reflected unsanitized. The payload `[Close]something'/><script>alert(1);</script><span class='1'` breaks out of the attribute context and injects a script tag. This occurs in the web interface of Revive Adserver, targeting authenticated users.

## Requirements

1. Access to the Invocation Code page
2. Web browser without aggressive XSS protections
3. Understanding of HTML attribute breakout techniques

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding)
- Deploy Content Security Policy (CSP) to block inline scripts
- Use WAF rules to detect common XSS payloads

## Objectives

1. Submit payload to trigger reflection
2. Bypass basic protections in the application
3. Set up for JavaScript execution

## Instructions

### Step 1: Locate Close Text Field

**Context**: Identify the vulnerable input field in the form.

In the Invocation Code interface, find the 'Close text' parameter field.

### Step 2: Craft and Enter Payload

**Context**: Input the breakout payload to inject script.

Enter the following into the Close text field:

`[Close]something'/><script>alert(1);</script><span class='1' `

Click submit or generate the code.

**Expected Output**: The form processes, and the payload is echoed back in the output without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[injection]]

---
tags:
  - xss
  - recon
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b8842b68-dc7b-4638-bfa5-bba24ae5dbca
created_at: '2025-12-11T06:06:04.854Z'
updated_at: '2025-12-11T06:06:04.854Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Discover Character Normalization Issue

## Summary

This procedure involves identifying character normalization vulnerabilities in web applications, specifically where special characters like '＜' are converted to '<' without proper escaping, enabling potential XSS attacks.

## Description

In this attack scenario, the Rockstar Games Social Club Message system normalizes '＜' to '<' and fails to escape it properly, allowing attackers to inject HTML tags. This is tested by sending probe messages and inspecting the rendered output. The expected outcome is confirmation of the vulnerability for further exploitation.

## Requirements

1. Access to the target web application's message system
2. A web browser with developer tools for inspecting HTML
3. Basic knowledge of HTML and character encoding

## Defense

Defensive measures and detection strategies:

- Implement proper input sanitization and output escaping for all user-generated content
- Use content security policy (CSP) to restrict script execution
- Monitor for unusual character patterns in user inputs

## Objectives

1. Confirm character normalization behavior
2. Verify lack of escaping for normalized characters
3. Document findings for payload crafting

## Instructions

### Step 1: Send Probe Message

**Context**: Send a message containing the '＜' character to observe normalization.

Compose and send a message with content like 'Test ＜ character' via the Social Club interface.

> Expect the '＜' to render as '<' in the HTML.

### Step 2: Inspect Rendered Output

**Context**: Use browser tools to check if the normalized '<' is escaped.

View the message in the browser, open developer tools, and inspect the element containing the message.

> Look for unescaped '<' in the HTML source, indicating vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss]]
- [[web-vulnerability]]

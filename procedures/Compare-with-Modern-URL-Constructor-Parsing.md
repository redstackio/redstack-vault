---
tags:
  - crlf-injection
  - modern-parsing
  - node-js
type: procedure
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/parse-modern-url]]'
verified: false
platforms:
  - Node.js
  - JavaScript
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.495Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7d05969e-9413-4329-8d24-e75b120cc8e7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Compare-with-Modern-URL-Constructor-Parsing

## Summary

This procedure compares parsing results between legacy and modern Node.js URL handling to validate the CRLF injection vulnerability and its whitelist bypass impact.

## Description

Modern URL constructor processes the full string without CRLF termination, revealing 'test1.com\r\ntest2.com' in .hostname, unlike the legacy parser. This comparison confirms the flaw in applications relying on old APIs, potentially allowing website compromise via unauthorized host access. Target: Node.js environments. Prerequisites: POC URL and legacy parse results. Expected outcome: Clear demonstration of parsing discrepancy.

## Requirements

1. Node.js supporting URL constructor (v10+)
2. POC URL from crafting step
3. Console for output comparison

## Defense

Defensive measures and detection strategies:

- Enforce modern URL parsing in code reviews
- Detect CRLF in logs for anomalous URLs
- Use secure URL validation to prevent injections

## Objectives

1. Validate legacy parser vulnerability
2. Show secure alternative handling
3. Educate on migration to prevent bypasses

## Instructions

### Step 1: Parse with Modern URL Constructor

**Context**: Instantiate new URL to parse and extract hostname, contrasting with legacy behavior.

**Command** ([[commands/parse-modern-url]]):
```javascript
const modernUrl = new URL(poc_url);
console.log(modernUrl.hostname);
```

> Creates a URL object from poc_url and logs .hostname, outputting the full injected string. Expected output: 'test1.com\r\ntest2.com', proving no early termination.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/parse-modern-url]]

## Tools Used


## Tags

- [[crlf-injection]]
- [[modern-parsing]]

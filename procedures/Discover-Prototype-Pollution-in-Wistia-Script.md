---
tags:
  - prototype-pollution
  - web-vuln
type: procedure
tools:
  - '[[tools/Browser-Console]]'
  - '[[tools/Browser]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/check-object-prototype]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e592a59e-3e45-497e-88ee-a24f4d0792d7
created_at: '2025-12-13T23:56:20.402Z'
updated_at: '2025-12-13T23:56:20.402Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Prototype Pollution in Wistia Script

## Summary

This procedure involves analyzing the Wistia embed script (E-v1.js) to identify a prototype pollution vulnerability exploitable via manipulated URL query parameters.

## Description

The script parses location.href and document.referrer without proper validation, allowing arbitrary properties to be added to Object.prototype. This is discovered by examining the script's initialization code and testing with crafted URLs.

## Requirements

1. Access to a web browser with developer tools
2. Target page with Wistia embed
3. Basic JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Implement strict URL parsing validation
- Monitor for unusual query parameters in logs

## Objectives

1. Identify vulnerable URL parsing
2. Confirm potential for prototype pollution
3. Document root cause for further exploitation

## Instructions

### Step 1: Analyze Script Code

**Context**: Examine the E-v1.js script for parsing functions.

**Command** ([[commands/check-object-prototype]]):
```javascript
Object.prototype
```

> Use this in the browser console after loading the script to inspect the prototype.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/check-object-prototype]]

## Tools Used

- [[tools/Browser-Console]]

## Tags

- [[prototype-pollution]]
- [[web-vuln]]

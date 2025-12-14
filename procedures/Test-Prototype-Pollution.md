---
tags:
  - prototype-pollution
  - testing
type: procedure
tools:
  - '[[tools/Browser]]'
  - '[[tools/Browser-Console]]'
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
id: a26e9dd9-cbfe-4cc8-b932-0cf6cf83e596
created_at: '2025-12-13T23:56:20.400Z'
updated_at: '2025-12-13T23:56:20.400Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Prototype Pollution

## Summary

This procedure tests for prototype pollution by visiting a crafted URL and verifying added properties in the Object prototype.

## Description

By appending query parameters like ?__proto__[ggg]=aaa to the URL, the script adds properties to Object.prototype, which can be checked in the browser console.

## Requirements

1. Web browser
2. Access to target URL
3. Developer console

## Defense

Defensive measures and detection strategies:

- Sanitize query parameters
- Use Object.create(null) for parsed objects

## Objectives

1. Confirm pollution via URL
2. Verify new property addition
3. Prepare for exploitation

## Instructions

### Step 1: Visit Crafted URL

**Context**: Load the page with polluting parameters.

Visit: https://www.hackerone.com/blog/scaling-security-startup-unicorn?__proto__[ggg]=aaa

### Step 2: Check Prototype

**Context**: Inspect Object.prototype.

**Command** ([[commands/check-object-prototype]]):
```javascript
Object.prototype
```

> Expected to show added 'ggg' property.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/check-object-prototype]]

## Tools Used

- [[tools/Browser]]

## Tags

- [[prototype-pollution]]
- [[testing]]

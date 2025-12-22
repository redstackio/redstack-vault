---
tags:
  - xss
  - reflected-xss
type: procedure
tools:
  - '[[tools/Burp]]'
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
id: d431eabd-d35d-4350-931c-b54a34947b41
created_at: '2025-12-13T23:56:20.379Z'
updated_at: '2025-12-13T23:56:20.379Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Discover Reflected XSS in Guvo Cookie

## Summary

This procedure identifies a reflected XSS vulnerability by setting the guvo cookie and observing its unescaped reflection in Yelp page HTML.

## Description

The guvo cookie value is reflected without proper escaping in JavaScript contexts like window.ySitRepParams and window.yelp.guv on pages such as www.yelp.com and biz.yelp.com/login, allowing arbitrary JavaScript execution.

## Requirements

1. Access to Yelp.com domains
2. Proxy tool like Burp for request interception
3. Browser for testing

## Defense

Defensive measures and detection strategies:

- Implement proper input sanitization and output encoding for cookie values
- Monitor for unusual cookie values in logs

## Objectives

1. Confirm XSS vulnerability
2. Observe reflection points
3. Prepare for payload injection

## Instructions

### Step 1: Set Guvo Cookie and Observe Reflection

**Context**: Use Burp to set the guvo cookie and inspect responses.

Intercept a request to www.yelp.com, add the guvo cookie with a test value, and check the response HTML for unescaped reflection.

> Expected: Unescaped guvo value in window.ySitRepParams.

### Step 2: Test on Login Page

**Context**: Repeat on biz.yelp.com/login.

Set guvo and load the page, inspect for reflection in window.yelp.guv.

> Expected: Confirmation of XSS on sensitive pages.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp]]

## Tags

- xss
- reflected-xss

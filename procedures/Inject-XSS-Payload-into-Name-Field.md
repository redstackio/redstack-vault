---
tags:
  - xss
  - stored-xss
  - javascript
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
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: c88e2d27-be32-44ba-845d-76a99c182b56
created_at: '2025-12-14T03:46:38.270Z'
updated_at: '2025-12-14T03:46:38.270Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Name Field

## Summary

Injects a stored XSS payload into the name field of the Localize team member invitation form, exploiting insufficient sanitization.

## Description

During the add team member process, the name field lacks proper input sanitization, allowing injection of JavaScript that is stored and later rendered in the victim's browser when they join the team. The payload `</script><svg onload=alert(document.domain)>` closes an existing script tag and uses an SVG onload to execute code, alerting the document domain and disrupting functionality like logout.

## Requirements

1. Open add team member form
2. Knowledge of XSS payloads targeting script contexts
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user inputs in name fields (e.g., HTML entity encoding)
- Implement Content Security Policy (CSP) to block inline scripts and SVG execution
- Validate invitation payloads server-side before storage

## Objectives

1. Store malicious JavaScript in the team member name
2. Ensure payload survives storage and rendering
3. Prepare for victim-side execution

## Instructions

### Step 1: Enter Payload in Name Field

**Context**: Target the vulnerable name input to inject the XSS.

Action:

In the name field, type: `</script><svg onload=alert(document.domain)>`

> This payload is designed for contexts where script tags may be present; it breaks out and executes on load. Do not proceed to submit yet; verify the field accepts it without stripping.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- javascript
- injection

---
id: uuid-5
tags:
  - js-execution
  - token-theft
  - xsrf
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:50.048Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-XSS-Payload-to-Steal-XSRF-Token

## Summary

This procedure observes the execution of the injected XSS payload in the email source view, resulting in the theft of the XSRF token via document.cookie alert.

## Description

When the email HTML is rendered, the onload event in the payload triggers JavaScript, alerting the browser's cookies, which include the sensitive XSRF token used for CSRF protection.

## Requirements

1. Email source viewed in executable context
2. Browser with cookie access
3. Payload designed to target document.cookie

## Defense

Defensive measures and detection strategies:

- Use HttpOnly flags on sensitive cookies like XSRF tokens
- Implement token rotation and validation
- Monitor for cookie access anomalies

## Objectives

1. Trigger JS execution
2. Capture and extract the XSRF token
3. Enable potential CSRF exploitation

## Instructions

### Step 1: Render and Observe

**Context**: Allow the source view to load fully.

Passive observation.

> Upon loading the source, the payload should automatically execute, popping an alert with cookie contents.

### Step 2: Extract Token

**Context**: Identify and copy the token from the alert.

Manual extraction.

> In the alert dialog, locate the XSRF token (e.g., a string like 'xsrf_token=abc123') and copy it for use in CSRF attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[theft]]

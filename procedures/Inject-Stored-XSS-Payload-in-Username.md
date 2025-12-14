---
id: proc-uuid-3
name: Inject-Stored-XSS-Payload-in-Username
tags:
  - stored-xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.576Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Username

## Summary

This procedure injects a stored XSS payload into username fields after bypassing validation, storing it server-side for execution when profiles are viewed by victims.

## Description

Exploiting lack of server-side sanitization, the payload closes HTML tags and injects an onerror image to run JS. Targets alphanumeric-only validation that's client-side, allowing HTML/JS storage and reflection in profile views for cookie theft.

## Requirements

1. Bypassed validation on form
2. Authenticated access
3. Payload: `"><img src onerror=confirm(document.cookie)>`

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with HTML entity encoding
- Validate and escape outputs in templates
- Detect JS execution via browser monitoring

## Objectives

1. Store executable JS in user data
2. Trigger on profile view
3. Steal session data

## Instructions

### Step 1: Enter Payload in Fields

**Context**: Fill form with malicious input.

In 'new username' and 'confirm username', input `"><img src onerror=confirm(document.cookie)>`.

> Ensures matching for submission.

### Step 2: Submit and Verify

**Context**: Store payload and test execution.

Click 'Submit'; view profile to confirm alert with cookies.

> Payload reflected unescaped, executing JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- stored-xss
- payload-injection

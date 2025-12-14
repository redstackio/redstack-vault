---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - payload-injection
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.657Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-into-Group-Name

## Summary

This procedure details injecting a malicious JavaScript payload into the Name field of a User Group in Concrete CMS, exploiting lack of input sanitization to store XSS for later execution in search results.

## Description

The vulnerability stems from improper sanitization in the User Groups/Group Details form in Concrete CMS 8.2.0 RC2. By editing a group and inserting a payload like `locals" onclick=alert('XSS!') "'>`, the attacker stores executable JavaScript. This executes when admins search and view results, potentially hijacking sessions. Target environment is web-based CMS; outcomes include payload persistence without errors.

## Requirements

1. Authenticated session with edit permissions for User Groups
2. Access to the Edit Group form via the CMS UI
3. Knowledge of XSS payloads tailored to the context (e.g., onclick for link triggers)

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs on storage and output (e.g., use htmlspecialchars in PHP)
- Implement Content Security Policy (CSP) to block inline JavaScript execution
- Log and monitor form submissions for suspicious patterns like script tags or onclick attributes

## Objectives

1. Bypass input validation to store JavaScript in the database
2. Ensure payload survives form submission
3. Set up for execution in admin views

## Instructions

### Step 1: Open Edit Group Form

**Context**: Initiate editing to access the Name field.

Click dropdown on group and select 'Edit Group'.

> Form loads with editable fields. Expected output: Name input ready.

### Step 2: Enter XSS Payload

**Context**: Inject the malicious string to break out of context.

In Name field: `locals" onclick=alert('XSS!') "'>`.

> Payload crafts a broken quote and onclick handler. Expected output: No client-side block.

### Step 3: Submit Form

**Context**: Store the payload persistently.

Click 'Update Group'.

> Server processes and saves. Expected output: Success message, group updated.

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

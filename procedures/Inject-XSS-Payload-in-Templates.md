---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
name: Inject-XSS-Payload-in-Templates
tags:
  - xss
  - injection
  - stored-xss
  - infogram
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
updated_at: '2025-12-14T03:16:14.280Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Templates

## Summary

This procedure details the injection of a malicious JavaScript payload into Infogram's template input fields, leveraging insufficient sanitization to store the payload server-side for later execution. It is used in XSS exploitation to target authenticated users viewing the templates.

## Description

Infogram's templates allow user inputs that are persisted without proper escaping, enabling stored XSS. The attack scenario involves an authenticated attacker creating a template with an embedded script, such as an img tag with an onerror handler. When victims load the template, the script executes in their browser, potentially exfiltrating session data. Prerequisites are template editing access; outcomes include persistent payload storage.

## Requirements

1. Authenticated session in Infogram with template creation rights
2. Knowledge of vulnerable input fields from prior reconnaissance
3. Web browser for payload testing

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding or allowlists
- Use output encoding when rendering template data in HTML/JS contexts
- Implement rate limiting on template creations and audit logs for suspicious payloads

## Objectives

1. Store malicious JavaScript in a template
2. Ensure payload persists without triggering server-side filters
3. Prepare for execution on template viewing

## Instructions

### Step 1: Prepare Payload

**Context**: Craft a simple, evasive XSS payload to test injection.

Use the payload `'><img src=x onerror=prompt(0);>'` which breaks out of HTML context and executes JS on error.

### Step 2: Inject into Template

**Context**: Enter the payload in a vulnerable field and save.

In the template editor, paste the payload into the title or description field. Click save and capture the template's URL or ID.

### Step 3: Validate Storage

**Context**: Confirm the payload is stored unaltered.

Reload the template edit page and inspect the field value; it should show the raw payload without modifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[stored-xss]]
- [[infogram]]

---
id: proc-create-malicious-author
tags:
  - xss
  - payload-injection
  - author-profile
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
updated_at: '2025-12-13T23:52:20.819Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Author-Profile

## Summary

This procedure injects a stored XSS payload into the author name field of CMS Airship, exploiting lack of escaping in Twig rendering to store malicious JavaScript for later execution.

## Description

The vulnerability stems from the author name not being properly escaped when rendered in the edit page HTML via sprintf() without Twig auto-escape. By submitting `<script>alert(1)</script>` as the name, the payload is stored and output unescaped (e.g., as value='<script>alert(1)</script>'), leading to execution on page load. This targets authenticated users viewing author details, with potential for session theft.

## Requirements

1. Authenticated session in CMS Airship
2. Access to /bridge/author/new endpoint
3. Web browser for form interaction

## Defense

Defensive measures and detection strategies:

- Apply proper HTML entity encoding to user inputs in templates
- Implement Content-Security-Policy (CSP) to block inline scripts
- Sanitize and validate all form inputs server-side

## Objectives

1. Store malicious JavaScript in author profile
2. Ensure payload persists without immediate detection
3. Prepare for triggering in admin context

## Instructions

### Step 1: Navigate to Author Creation

**Context**: Access the form to input author details.

From the dashboard, go to http://localhost:8080/bridge/author/new.

> Expected: Form loads with name field.

### Step 2: Submit Malicious Payload

**Context**: Inject the XSS payload into the name field.

Enter `<script>alert(1)</script>` as the author name and submit the form.

> Expected: Author created; payload stored in database without escaping.

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
- payload-injection
- author-profile

---
id: proc-001
tags:
  - xss
  - stored-xss
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
updated_at: '2025-12-14T03:16:25.480Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Group-with-XSS-Payload

## Summary

This procedure involves creating a group in the wis.pr application using a malicious name containing an XSS payload, which is stored without sanitization and later reflected in sharing pages.

## Description

In the wis.pr application, group names are user-controlled and inserted directly into HTML meta tags (e.g., twitter:description) on sharing pages without proper escaping. By crafting a group name with a script tag, an attacker stores the payload server-side. When a victim visits the sharing URL, the payload executes in their browser context, allowing arbitrary JavaScript. This targets authenticated users with group creation access and impacts any visitor to the public sharing page.

## Requirements

1. Valid wis.pr user account with group creation permissions
2. Web browser for accessing the application
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement output encoding for user input in HTML contexts (e.g., escape quotes and script tags)
- Use Content Security Policy (CSP) to block inline scripts
- Sanitize group names on input with allowlists for characters
- Monitor for anomalous JavaScript execution in browser logs

## Objectives

1. Store malicious JavaScript in application metadata
2. Prepare for payload delivery via public URLs
3. Enable client-side execution for impact

## Instructions

### Step 1: Access Group Creation

**Context**: Log in and navigate to create a new group to inject the payload.

Log in to wis.pr and go to the groups section. Click 'Create New Group'.

### Step 2: Inject Payload

**Context**: Enter the malicious name to store the XSS.

In the group name field, input: `Test>"<script>alert('test');</script>`. Fill any other required fields and submit.

> This payload breaks out of the meta tag attribute by closing quotes and injecting a script tag, which executes on page load.

**Expected Output**: Group created; verify by checking the group list for the exact name.

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
- [[stored-xss]]

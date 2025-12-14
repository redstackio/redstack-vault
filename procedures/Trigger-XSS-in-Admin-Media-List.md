---
tags:
  - xss
  - admin-compromise
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
updated_at: '2025-12-14T17:31:52.534Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: 33c0fd1c-32eb-4f1f-8594-022c602b2e89
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Admin-Media-List

## Summary

Triggers the stored XSS payload by having an admin view and interact with the malicious attachment in the WordPress admin dashboard's Media list.

## Description

Navigate to Dashboard > Media (list mode); filename renders unescaped, executing JS on click. Leads to alert or code execution in admin context.

## Requirements

1. Malicious attachment created
2. Admin access to dashboard
3. Default list view enabled

## Defense

Defensive measures and detection strategies:

- HTML-escape all admin displays
- Enable grid view or sanitization plugins
- Train admins on suspicious media
- Monitor JS errors in browser console

## Objectives

1. Execute payload in admin session
2. Steal cookies or escalate
3. Compromise site

## Instructions

### Step 1: Access Admin Media

**Context**: Admin logs in and goes to Media.

**Command**:
```bash
# No command; browser navigation: https://site/wp-admin/upload.php
```

> Views list; XSS triggers on interaction.

### Step 2: Interact with Attachment

**Context**: Click the malicious file.

**Command**:
```bash
# JS executes: alert('xss')
```

> Payload runs.

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
- admin-compromise

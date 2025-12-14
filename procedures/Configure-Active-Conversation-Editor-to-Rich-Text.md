---
id: proc-configure-rich-text-editor
tags:
  - xss
  - configuration
  - concrete-cms
type: procedure
tools:
  - '[[tools/TinyMCE-Editor]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:53.595Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure Active Conversation Editor to Rich Text

## Summary

This procedure enables the Rich Text editor in Concrete CMS Conversations module, allowing raw HTML input via TinyMCE Source mode, which is a prerequisite for injecting unsanitized script payloads in Stored XSS attacks.

## Description

In Concrete CMS, the Conversations module handles comments and messages. By default, it may use a safer editor, but setting it to Rich Text activates TinyMCE with a Source button, permitting direct HTML insertion including <script> tags. These are stored without sanitization in the database, leading to persistent XSS. This setup affects blog comments and is exploitable by any user posting comments. Target environment: Concrete CMS 8.5.2a1 on PHP/Apache with MySQL.

## Requirements

1. Administrative access to Concrete CMS dashboard
2. Conversations module enabled with blog comments active
3. Web browser access to the admin interface

## Defense

Defensive measures and detection strategies:

- Disable Rich Text editor or enforce HTML sanitization in Conversations settings
- Implement content security policy (CSP) to block external script loading
- Monitor database for suspicious HTML in comment fields

## Objectives

1. Enable vulnerable editor configuration for payload injection
2. Prepare the target for Stored XSS exploitation
3. Ensure persistence of malicious content

## Instructions

### Step 1: Access Admin Settings

**Context**: Log in as admin and navigate to Conversations configuration to enable Rich Text mode.

No command required; use the web UI:

- Go to Dashboard > System & Settings > Conversations > Settings
- Set "Active Conversation Editor" to "Rich Text"
- Save changes

> This updates the editor globally for comments, enabling TinyMCE Source mode without sanitization.

### Step 2: Verify Configuration

**Context**: Confirm the change by accessing a comment form.

No command; inspect the editor:

- Open a blog post with comments
- Check if the editor shows a "Source" button

> Expected: Source button visible, allowing HTML input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/TinyMCE-Editor]]

## Tags

- [[xss]]
- [[configuration]]

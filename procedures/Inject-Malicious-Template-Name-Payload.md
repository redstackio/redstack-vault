---
tags:
  - xss
  - payload-injection
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.634Z'
sub_techniques: []
id: a661bda0-78f8-467f-ab25-0949b47a4e9d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Template-Name-Payload

## Summary

This procedure injects a JavaScript payload into a PHP file's Template Name comment, exploiting the lack of escaping in wp-admin/theme-editor.php to store XSS for later execution.

## Description

Template names are parsed from PHP comments using get_file_description() and output unescaped in HTML <li><a> tags. By adding a comment like /* Template Name: <script>confirm(document.cookie);</script> */, the script executes when the file link is clicked, potentially stealing admin cookies.

## Requirements

1. Loaded PHP file in theme editor
2. Knowledge of XSS payloads (e.g., confirm dialog for testing)
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Sanitize all outputs in admin pages with esc_html() or htmlspecialchars()
- Scan theme files for suspicious comments using security tools

## Objectives

1. Embed executable JavaScript in the template name
2. Maintain file validity
3. Enable stored XSS persistence

## Instructions

### Step 1: Add Payload Comment

**Context**: Insert the malicious comment at the file's top.

Edit the textarea to add: /* Template Name: <script>confirm(document.cookie);</script> */

> The comment appears in the editor; preview if available shows no immediate execution.

### Step 2: Validate Syntax

**Context**: Ensure PHP remains parsable.

Check for syntax errors in the editor.

> No errors; file is ready for update.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- xss
- payload-injection

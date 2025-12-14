---
id: proc-disable-wptexturize
tags:
  - wordpress
  - filter-bypass
  - xss-prereq
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/disable-wptexturize-filter]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.112Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Disable-WPTexturize-Filter

## Summary

This procedure disables the WordPress wptexturize filter to prevent automatic text processing and escaping of content, enabling the injection of raw HTML and JavaScript payloads in forms like ticket subjects without interference.

## Description

In WordPress, the wptexturize filter automatically converts certain characters (e.g., quotes, dashes) to HTML entities, which can neutralize XSS payloads. By adding a filter hook to return false for run_wptexturize, this processing is skipped, allowing unescaped input. This is a prerequisite for exploiting vulnerabilities like stored XSS in plugins such as SupportFlow, where subjects are output without additional escaping. The change applies site-wide until removed and requires access to theme files or plugin code.

## Requirements

1. Access to edit the active theme's functions.php file (via FTP, file manager, or WordPress editor).
2. WordPress administrative privileges or file system access.
3. Active WordPress installation (tested on versions compatible with SupportFlow).

## Defense

Defensive measures and detection strategies:

- Monitor functions.php modifications via file integrity monitoring (e.g., WordPress security plugins like Wordfence).
- Enable WordPress debugging to log filter changes.
- Use plugin auditing tools to detect unauthorized hooks.

## Objectives

1. Bypass automatic text escaping to allow raw payload injection.
2. Prepare the environment for XSS exploitation without altering core WordPress behavior permanently.
3. Ensure payloads like <script> tags remain intact in stored content.

## Instructions

### Step 1: Add Filter Hook to Functions.php

**Context**: Locate and edit the functions.php file of the active theme to insert the filter disablement code, which will prevent wptexturize from running on subsequent content processing.

**Command** ([[commands/disable-wptexturize-filter]]):
```php
add_filter( 'run_wptexturize', '__return_false' );
```

> This PHP function adds a filter that always returns false for the run_wptexturize hook, skipping texturization globally. Expected output: No console or log output; verify by testing a form input with raw HTML (e.g., enter "<script>" and check if it remains unescaped).

### Step 2: Apply and Verify Changes

**Context**: Save the file and reload the WordPress admin or frontend to activate the filter change, then test in a non-critical form to confirm raw input acceptance.

**Command** (Manual verification, no command):

> Refresh the page and submit a test ticket or post with HTML entities. If the raw code persists in the database (view via phpMyAdmin), the disablement succeeded.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/disable-wptexturize-filter]]

## Tools Used


## Tags

- wordpress
- filter-bypass
- xss-prereq

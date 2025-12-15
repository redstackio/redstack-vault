---
id: p5e6f7g8-h9i0-1234-efgh-5678901234
tags:
  - wordpress
  - lfi
  - rce
  - php
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:30:47.345Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Hijack Execution Flow]]'
---
# Execute-PHP-Shell-via-WordPress-Post-Meta-Inclusion

## Summary

This procedure sets the _wp_page_template post meta to the uploaded shell's path, causing WordPress to include and execute the PHP code during post rendering for RCE.

## Description

WordPress uses _wp_page_template meta to load custom theme templates via include(). Without path validation, setting it to an arbitrary file like /wp-content/themes/current-theme/shell.txt executes the PHP as the web server user, chaining with a known LFI vulnerability in template handling.

## Requirements

1. PHP shell uploaded to theme
2. Edit access to posts/pages
3. Published post for rendering

## Defense

Defensive measures and detection strategies:

- Validate _wp_page_template against allowed templates
- Disable custom fields or use plugins to restrict
- Monitor includes and post meta changes

## Objectives

1. Trigger arbitrary file inclusion
2. Execute uploaded PHP code
3. Achieve server-side RCE

## Instructions

### Step 1: Edit Post

**Context**: Select or create a post to modify meta.

Go to Posts > Edit on an existing post or create new.

### Step 2: Set Post Meta

**Context**: Configure inclusion of the shell.

In custom fields, add '_wp_page_template' with value '/wp-content/themes/current-theme/shell.txt'. Save the post.

> WordPress will include the file on render.

### Step 3: Trigger Execution

**Context**: Load the post to run the code.

View or publish the post in the frontend.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Hijack Execution Flow]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- lfi
- rce
- php

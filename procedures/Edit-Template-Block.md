---
tags:
  - xss
  - editor
  - summernote
type: procedure
tools:
  - '[[tools/Summernote-JS]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ab6c2855-f4c6-4537-8513-a14083fe66f2
created_at: '2025-12-13T23:55:20.632Z'
updated_at: '2025-12-13T23:55:20.632Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Edit-Template-Block

## Summary

This procedure modifies a content block in the Judge.me email template editor, accessing the vulnerable Summernote JS interface for payload insertion.

## Description

The template editor uses Summernote JS, a WYSIWYG library with a bug allowing unsafe JavaScript in links. Editing a block enables HTML manipulation without adequate escaping, facilitating stored XSS. This targets Shopify-integrated apps and assumes prior template creation.

## Requirements

1. Open email template in edit mode
2. Browser with JavaScript enabled
3. Judge.me app access

## Defense

Defensive measures and detection strategies:

- Patch Summernote JS to the latest version or use sanitized alternatives
- Implement server-side validation for all template inputs
- Monitor editor interactions for suspicious HTML patterns

## Objectives

1. Enter edit mode on a template block
2. Expose the WYSIWYG toolbar
3. Prepare for link insertion

## Instructions

### Step 1: Select and Edit Block

**Context**: Activate the editable area.

No command required; UI interaction:

- Click on a text or body block to enter edit mode.

> Expected output: Cursor appears, toolbar with link insert option shows.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Summernote-JS]]

## Tags

- [[xss]]
- [[editor]]
- [[summernote]]

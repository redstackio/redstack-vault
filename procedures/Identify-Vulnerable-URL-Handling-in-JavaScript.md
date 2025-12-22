---
tags:
  - url-validation
  - xss
  - javascript
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Client Configurations]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 96f5e471-0054-4e22-a050-ffc11963f63b
created_at: '2025-12-14T03:47:23.554Z'
updated_at: '2025-12-14T03:47:23.554Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Client Configurations]]'
---
# Identify Vulnerable URL Handling in JavaScript

## Summary

This procedure examines the Evernote client JavaScript to pinpoint the URL validation flaw in the 'after-save-note' view, confirming the reflected XSS opportunity via substring checking.

## Description

In `renderWithContext()`, the 'after-save-note' case invokes `renderAfterSaveNoteView()`, which redirects to `ionUrl` after a weak check (`ionUrl.indexOf('https://www.evernote.com/') !== -1`). This allows bypass with `javascript:alert(...)//https://www.evernote.com/`. The scenario targets web developers analyzing client-side code for security issues.

## Requirements

1. Beautified `main.68d4af6d45d9dcaab6e6.js` from previous procedure
2. Code editor with search functionality
3. Understanding of JavaScript redirection and string methods

## Defense

Defensive measures and detection strategies:

- Validate URLs with strict prefix matching (e.g., startsWith)
- Sanitize all user-controlled redirects
- Static analysis tools to detect weak validations

## Objectives

1. Locate the renderAfterSaveNoteView function
2. Confirm substring-based check vulnerability
3. Document the bypass technique

## Instructions

### Step 1: Search for View Switch

**Context**: Find the rendering logic entry point.

In the beautified JS, search for 'renderWithContext' and examine the switch on 'this.view'.

> Identify the 'after-save-note' case leading to ionUrl assignment.

### Step 2: Analyze Validation Logic

**Context**: Verify the insecure check.

Look for `window.location.href = ionUrl` and the preceding `indexOf(J.baseUrl)`. Note J.baseUrl is 'https://www.evernote.com/'.

> Confirm it checks for substring presence, not prefix, enabling protocol bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Client Configurations]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-validation]]
- [[xss]]
- [[JavaScript]]

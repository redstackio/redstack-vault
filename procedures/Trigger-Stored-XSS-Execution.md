---
tags:
  - xss
  - execution
  - cookie-theft
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.629Z'
sub_techniques: []
id: 69f871a1-dea4-443c-b9bd-3243ed75479a
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-Execution

## Summary

This procedure triggers the stored XSS by clicking the file link in the theme editor, causing the unescaped template name to execute JavaScript in the admin context.

## Description

The vulnerability stems from echoing $file_description without escaping in theme-editor.php. Clicking the link reloads the page, parses the comment, and injects the script into HTML, running it client-side for actions like cookie exfiltration.

## Requirements

1. Updated file with payload
2. Admin panel session active
3. Browser JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Apply patches or escape outputs in core WordPress files
- Monitor for JavaScript alerts or network requests from admin pages

## Objectives

1. Execute the injected script
2. Demonstrate impact (e.g., cookie access)
3. Enable further attacks like session hijacking

## Instructions

### Step 1: Interact with File Link

**Context**: Cause the unescaped output to render.

In the file list, click the link for the edited file (e.g., back-compat.php).

> The page reloads, and the script executes, showing a confirm dialog with document.cookie.

### Step 2: Observe Execution

**Context**: Validate XSS impact.

Check browser console or dialog for payload output.

> Alert/confirm pops up; potential for data theft via network requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- xss
- execution
- cookie-theft

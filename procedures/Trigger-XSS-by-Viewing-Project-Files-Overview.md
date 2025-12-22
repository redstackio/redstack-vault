---
id: proc-uuid-4
tags:
  - xss-trigger
  - files-overview
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.331Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Trigger-XSS-by-Viewing-Project-Files-Overview

## Summary

This procedure triggers the stored XSS by navigating to the project's Files overview in a browser and clicking the malicious wiki submodule directory, executing the JavaScript payload.

## Description

Once the javascript: payload is stored in .gitmodules, any user viewing the project's tree at /tree/master and clicking the 'wiki' directory will have the JS executed in their session context. This can lead to alert popups, cookie theft, or API token exfiltration. No server-side commands are needed; it's purely client-side exploitation.

## Requirements

1. Victim browser session on GitLab
2. Access to the project Files overview
3. Malicious .gitmodules already pushed

## Defense

Defensive measures and detection strategies:

- Escape or strip javascript: schemes in UI rendering of submodule URLs
- Implement Content Security Policy (CSP) to block inline JS execution
- Monitor browser console errors and unexpected alerts in user sessions

## Objectives

1. Execute arbitrary JS in victim browser
2. Steal session data or API tokens
3. Impersonate users via stolen credentials

## Instructions

### Step 1: Navigate to Files Overview

**Context**: Load the project tree view where submodules are displayed.

No command; browser action:

> Visit https://gitlab.com/user/project/tree/master in a web browser.

### Step 2: Interact with Wiki Directory

**Context**: Click the wiki directory to process the malicious URL.

No command; browser action:

> Click on the 'wiki' directory link. Expected output: JavaScript alert('XSS') executes.

> For advanced payloads, replace alert with code to exfiltrate document.cookie or fetch API endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[files-overview]]
- [[javascript-execution]]

---
tags:
  - html-file
  - poc-assembly
  - csrf
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:57.136Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 609f9586-5f33-41f3-aced-7af80d5c9ef4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create and Save CSRF HTML File

## Summary

This procedure assembles the generated CSRF PoC code into a standalone HTML file named Csrf.html, ready for delivery to the victim.

## Description

The HTML file contains a form that auto-submits the deactivation POST using the victim's session. No tools are needed beyond a text editor; the file mimics a legitimate page to evade suspicion. Expected outcome: a functional exploit file that triggers on load.

## Requirements

1. Copied HTML from Burp PoC generator
2. Text editor (e.g., Notepad, VS Code)
3. Local file system access

## Defense

Defensive measures and detection strategies:

- Educate users on phishing attachments and unknown HTML files
- Browser extensions to block auto-submits

## Objectives

1. Create deliverable PoC file
2. Verify file integrity
3. Prepare for social engineering delivery

## Instructions

### Step 1: Paste HTML Code

**Context**: Transfer the PoC into a new file.

1. Open a text editor
2. Paste the full HTML code from Burp
3. Ensure <html><body> structure with form and script intact

> Code example snippet: <form action="https://www.evernote.com/secure/CloseAccount.action?accountAction=deactivateAccount&json=true" method="post"><input type="hidden" name="password" value=""> ... <script>document.forms[0].submit();</script></form>

### Step 2: Save and Test File

**Context**: Name and validate the file without executing on live account.

1. Save as Csrf.html
2. Open in browser (use incognito, no Evernote login) to check auto-submit
3. Close immediately to avoid issues

> File size ~1KB; no errors in console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- html-file
- poc-assembly
- csrf

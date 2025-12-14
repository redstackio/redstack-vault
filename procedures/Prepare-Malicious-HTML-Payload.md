---
tags:
  - xss
  - payload-prep
  - html
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 845c04fe-0d2b-49b3-82ce-7dbf72c3aac5
created_at: '2025-12-14T00:11:09.529Z'
updated_at: '2025-12-14T00:11:09.529Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-Malicious-HTML-Payload

## Summary

This procedure involves creating and copying a simple HTML payload to the clipboard, setting up for injection into the Nextcloud Text app to demonstrate self-XSS.

## Description

In the context of the Nextcloud Text app vulnerability, the attacker prepares a basic HTML string like '<h1>html</h1>' that, when pasted, will be inserted via innerHTML, bypassing plaintext expectations. This step requires no tools and is performed manually in a browser environment. Prerequisites include access to a text editor or direct clipboard manipulation. The outcome is a ready payload that can lead to HTML rendering and potential XSS if escalated with JavaScript.

## Requirements

1. Web browser with clipboard access
2. Basic knowledge of HTML
3. Access to any text input for copying

## Defense

Defensive measures and detection strategies:

- Educate users on avoiding suspicious pastes
- Monitor clipboard interactions in web apps (client-side logging)

## Objectives

1. Create a testable HTML payload
2. Copy it to clipboard without errors
3. Prepare for injection step

## Instructions

### Step 1: Create and Copy Payload

**Context**: This step assembles the HTML string and places it on the clipboard for the subsequent injection.

Manually select and copy the following text:

```
<h1>html</h1>
```

> This payload uses a heading tag to visibly demonstrate rendering changes. For real attacks, include <script>alert('XSS')</script> to execute JavaScript.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-prep]]

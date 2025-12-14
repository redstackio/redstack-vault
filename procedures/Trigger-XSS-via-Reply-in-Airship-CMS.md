---
id: proc-uuid-3
tags:
  - xss-trigger
  - javascript-execution
  - airship-cms
  - reply-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.045Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Reply-in-Airship-CMS

## Summary

This procedure triggers the persistent XSS payload in Airship CMS by clicking the 'Reply' button on a malicious comment, causing the unencoded name to be inserted into the DOM and executing arbitrary JavaScript in the victim's browser.

## Description

The /static/Hull/comments.js file contains the window.replyTo function, which reads the comment author's name from the DOM (e.g., .author element) and inserts it unencoded into the #reply-to element for the reply form. This re-insertion executes the payload, such as alert(1) or more advanced scripts to add admins. Victims (e.g., site moderators) trigger it naturally, leading to session hijacking or privilege escalation in the web environment.

## Requirements

1. Access to the blog post with the malicious comment visible
2. Victim user session (any authenticated or anonymous user clicking reply)
3. Payload already injected and CSP disabled

## Defense

Defensive measures and detection strategies:

- Encode all DOM insertions in JavaScript (e.g., use textContent or escapeHTML)
- Implement client-side validation and sanitization in comments.js
- Log and alert on suspicious JavaScript errors or executions in browser consoles

## Objectives

1. Execute injected JavaScript in victim context
2. Perform arbitrary actions like admin addition
3. Achieve full application access via escalation

## Instructions

### Step 1: Locate Malicious Comment

**Context**: Identify the comment with the injected payload as a victim user.

Navigate to the blog post and scroll to the comments section.

> Inspect the comment to confirm the author's name contains the payload in the DOM.

### Step 2: Click Reply to Trigger

**Context**: Interact with the comment to invoke the vulnerable replyTo function.

Click the 'Reply' button next to the malicious comment.

> Expected: Payload executes immediately; e.g., alert(1) pops up. For escalation, replace alert with script to submit a form adding a new admin, such as `document.getElementById('admin-form').submit();`.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[javascript-execution]]

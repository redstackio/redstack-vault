---
id: proc-trigger-xss-collabora-session
tags:
  - xss
  - collabora
  - javascript-execution
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:39.541Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Collabora-Editing-Session

## Summary

This procedure opens the shared document in Collabora Online and waits for the victim to join, triggering the stored XSS payload from the username when the collaborative user interface renders it.

## Description

In Collabora Online's collaborative editing mode, user display names are shown in the interface without proper sanitization, leading to XSS execution. The attacker opens the document first, and upon the victim's join, the payload executes in their browser, potentially allowing access to session data or further attacks within the Nextcloud context.

## Requirements

1. Access to the shared document
2. Victim must open the document for editing
3. Browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs, especially display names, before rendering in HTML/JS contexts
- Implement strict CSP headers in Collabora to block unsafe scripts
- Monitor for XSS-related alerts or errors in application logs and browser consoles

## Objectives

1. Execute arbitrary JavaScript in the victim's browser
2. Achieve code execution within the collaborative session context
3. Enable follow-on attacks like session theft

## Instructions

### Step 1: Open Document as Attacker

**Context**: Initiate the collaborative session from the attacker's side.

In Nextcloud Files, click to open the document in Collabora Online.

> Expected: Editor loads; collaborative mode active.

### Step 2: Wait for Victim Join

**Context**: Monitor for the victim's participation to trigger rendering.

Keep the session open and notify the victim to join (e.g., via chat or email).

> Expected: Victim opens the document; user list updates.

### Step 3: Observe Execution

**Context**: Confirm the payload fires in the victim's view.

Instruct the victim to interact with the editor; the payload should execute automatically upon user name display.

> Expected: Alert dialog or console error indicating JS execution (e.g., alert showing parent location).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[collabora]]
- [[javascript-execution]]

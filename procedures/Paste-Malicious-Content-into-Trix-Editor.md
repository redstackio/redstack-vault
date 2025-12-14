---
tags:
  - xss
  - paste-exploit
  - trix-editor
type: procedure
tools:
  - '[[tools/Trix-Editor]]'
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 7a1f7413-7952-4360-bfca-f71b81e31e83
created_at: '2025-12-13T23:55:06.220Z'
updated_at: '2025-12-13T23:55:06.220Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Paste-Malicious-Content-into-Trix-Editor

## Summary

This procedure involves copying the malicious div from the demo and pasting it into a vulnerable Trix editor instance, exploiting the lack of sanitization to store the XSS payload as an attachment.

## Description

Targeting applications like Basecamp that use Trix 2.1.1, pasting the content inserts the data-trix-attachment without validating the embedded img tag's onerror attribute. This stores the payload persistently. Requires an active editor session. Outcome: Payload embedded, ready for rendering and execution upon view or interaction.

## Requirements

1. Access to a Trix editor field in the target app (e.g., Basecamp compose box)
2. Copied malicious content from the generation step
3. User-level permissions to paste content

## Defense

Defensive measures and detection strategies:

- Sanitize pasted attachments server-side before storage
- Use DOMPurify or similar libraries for client-side HTML filtering
- Log and review paste events for suspicious data-trix-attachment patterns

## Objectives

1. Successfully embed the malicious img tag in the editor
2. Store the payload without triggering immediate errors
3. Enable subsequent rendering to execute the script

## Instructions

### Step 1: Navigate to Target Editor

**Context**: Open a form or note in the application where Trix is used for rich text input.

For Basecamp, create a new message or edit an existing one with a Trix field.

**Expected Output**: Empty or existing Trix editor instance ready for input.

### Step 2: Paste the Content

**Context**: Insert the clipboard content to bypass sanitization.

Position cursor in the editor and paste (Ctrl+V). The div's data-trix-attachment is processed, embedding the img.

**Expected Output**: Visual representation of an attachment or broken image in the editor; inspect element to confirm img tag presence.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Trix-Editor]]
- [[tools/Browser]]

## Tags

- [[xss]]
- [[paste-exploit]]

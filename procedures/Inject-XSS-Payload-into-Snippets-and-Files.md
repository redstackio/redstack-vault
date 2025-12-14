---
id: proc-uuid-3
tags:
  - xss
  - snippets
  - files
  - upload
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
updated_at: '2025-12-14T03:15:47.438Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Snippets and Files

## Summary

This procedure stores the XSS payload in Slack snippets and files exploiting weak sanitization in the /files section for persistent execution.

## Description

Snippets in Slack support various formats including HTML where user content is stored without stripping JavaScript attributes. By setting format to HTML entering payload and adding a comment the content renders in /files and can execute on main page views. Requires snippet creation access. Outcome: Payload in files ready for victim interaction.

## Requirements

1. Permissions to create and comment on snippets in Slack
2. Access to /files section
3. Consistent payload syntax

## Defense

Defensive measures and detection strategies:

- Restrict snippet formats to plain text or sanitized HTML only
- Scan uploads for SVG and script-like patterns pre-storage
- Implement file rendering in isolated iframes with sandboxing

## Objectives

1. Create snippet with payload as HTML content
2. Add payload in snippet comment
3. Verify storage in /files

## Instructions

### Step 1: Create Snippet with Payload

**Context**: Go to snippet creation select HTML format and input payload.

Manually enter in snippet editor:

```html
<img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)>
```

> Set format to HTML or any permissive type to allow rendering.

### Step 2: Add Comment and Finalize

**Context**: Attach a comment with payload then click create.

Manually add comment:

```html
<img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)>
```

Click Create snippet.

> Expected output: Snippet listed in /files with embedded payload.

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
- [[snippets]]

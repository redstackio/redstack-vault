---
id: proc-inject-iframe-stripo
tags:
  - injection
  - iframe
  - csp-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.493Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Inject-Malicious-Iframe-into-Template

## Summary

This procedure inserts an iframe tag sourcing from the malicious Firebase page into the Stripo template's HTML, exploiting the CSP frame-src wildcard to bypass restrictions.

## Description

The Stripo editor's lack of iframe sanitization allows direct HTML insertion. The payload uses a protocol-relative URL (//) to load the Firebase-hosted malicious content. This step assumes an open template from prior access and targets the web editor; successful injection enables execution upon preview or save.

## Requirements

1. Active Stripo template editor session
2. Deployed Firebase URL from previous step
3. Browser developer tools for HTML inspection

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP with specific frame-src allowlists (e.g., only stripo-app.firebaseapp.com)
- Sanitize HTML inputs to strip or escape iframe tags
- Log and alert on iframe insertions in editor sessions

## Objectives

1. Embed iframe without triggering client-side validation
2. Ensure src matches CSP-allowed wildcard
3. Prepare for load triggering

## Instructions

### Step 1: Open HTML Source in Editor

**Context**: Switch to raw HTML mode to edit content.

In Stripo editor, toggle to HTML view.

> Expected: Source code editor appears.

### Step 2: Insert Iframe Payload

**Context**: Add the iframe tag to the body or desired section.

Insert:

```html
<iframe src="//hackerone-jm.firebaseapp.com"></iframe>
```

> Expected: Tag added; no immediate errors.

### Step 3: Save Draft

**Context**: Persist changes without full preview.

Click save; inspect for persistence.

> Expected: Template updates; iframe remains in source.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- injection
- iframe
- csp-bypass

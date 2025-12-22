---
id: proc-uuid-001
name: Create-and-Inject-Malicious-Note-in-Simplenote
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.359Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - injection
  - markdown
platforms:
  - Web
tools:
  - '[[tools/DOMPurify]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Create-and-Inject-Malicious-Note-in-Simplenote

## Summary

This procedure outlines logging into Simplenote, creating a new note with Markdown enabled, and injecting a crafted SVG payload to exploit the Markdown parser's sanitization weaknesses, setting up for stored XSS.

## Description

In the context of Simplenote's web application at app.simplenote.com, this procedure targets the note creation feature where Markdown rendering is optional. By enabling Markdown and inserting an SVG element with a malicious <animate> attribute using a javascript: URI, the parser fails to sanitize the xlink:href animation properly. This leads to potential XSS when rendered. Prerequisites include a valid account; outcomes include payload insertion ready for publishing. The payload is adapted from DOMPurify bypass examples.

## Requirements

1. Authenticated access to app.simplenote.com
2. Modern web browser supporting SVG and JavaScript
3. Reference to DOMPurify for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict SVG sanitization using libraries like DOMPurify with custom hooks for animate attributes
- Validate and escape all user inputs in Markdown parsers
- Monitor for anomalous JavaScript execution in note rendering logs

## Objectives

1. Establish initial access and prepare the injection vector
2. Bypass client-side input validation for SVG elements
3. Position payload for persistent storage and execution

## Instructions

### Step 1: Authenticate and Create Note

**Context**: Log in to gain access to note creation and enable Markdown to allow HTML-like SVG injection.

No specific command; use the web UI to log in at app.simplenote.com, click 'New Note', and toggle 'Markdown Formatted' in settings.

> Successful login redirects to the dashboard; new note opens with Markdown active.

### Step 2: Insert SVG Payload

**Context**: Paste the crafted payload to inject the XSS vector via the Markdown editor.

Use the following payload in the edit window:

```html
<div id="137"><svg><a xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="?"><circle r="400"></circle><animate attributeName="xlink:href" begin="0" from="javascript:alert(document.domain)" to="&" /></a>//\\["'\\`-->\\]]></div>
```

> Payload inserts as text; save the note to persist it temporarily.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/DOMPurify]]

## Tags

- [[xss]]
- [[injection]]
- [[markdown]]

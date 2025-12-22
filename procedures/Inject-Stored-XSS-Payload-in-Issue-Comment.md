---
tags:
  - xss
  - stored-xss
  - payload-injection
  - gitlab
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
updated_at: '2025-12-13T23:52:34.047Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 56dceb58-5480-4cc4-84b5-4049a5780ac9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Issue-Comment

## Summary

This procedure injects a crafted XSS payload into a GitLab issue comment, exploiting bypasses in SyntaxHighlightFilter (server-side) and gl-emoji (frontend) to store executable JavaScript.

## Description

The payload breaks out of the <pre> tag structure via unsanitized data-sourcepos attribute in SyntaxHighlightFilter, then injects into gl-emoji's data-name attribute to evade v-safe-html directive, allowing onload JavaScript execution. This stored XSS affects all viewers of the issue or note pages, enabling session theft or client-side attacks. It requires comment privileges and targets GitLab versions with the flawed rendering.

## Requirements

1. Open issue with comment field
2. Knowledge of payload structure for bypasses
3. Browser developer tools for testing (optional)

## Defense

Defensive measures and detection strategies:

- Upgrade to patched GitLab versions (post-14.4.2)
- Implement input validation and output encoding for comments
- Scan comments for suspicious HTML patterns using WAF or custom filters

## Objectives

1. Store malicious payload in GitLab database via comment submission
2. Bypass dual sanitization layers for HTML/JS injection
3. Prepare for execution on page render

## Instructions

### Step 1: Craft and Paste Payload

**Context**: Enter the payload in the comment Markdown field to exploit attribute injection.

**Command** (UI action with payload):

Paste into comment box:

```html
<pre data-sourcepos=" href=\"x\"></pre><gl-emoji data-name='\"x=\"y\" onload=\"alert(document.location.href)\"' data-unicode-version='x'>abc</gl-emoji><pre x=\""><code></code></pre>
```

> The payload uses escaped quotes to break out and inject onload handler; submit the comment.

### Step 2: Submit and Verify Storage

**Context**: Confirm the payload is saved without full sanitization.

**Command** (UI action):

Click "Comment" or "Submit" button.

> Comment posts; inspect the rendered HTML source to see partial payload persistence (e.g., gl-emoji with data-name).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- payload-injection
- gitlab

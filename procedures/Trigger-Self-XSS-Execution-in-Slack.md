---
tags:
  - self-xss
  - execution
  - slack
type: procedure
tools:
  - '[[tools/Slack-Self-XSS-Demonstration-Video]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.787Z'
sub_techniques: []
id: 92a1cb90-d843-46c7-9d86-6d339ef59cdd
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Self-XSS-Execution-in-Slack

## Summary

This procedure triggers the rendering of the formatted post, causing the self-XSS payload to execute JavaScript in the user's browser.

## Description

Upon rendering the code-formatted post, Slack's client-side engine fails to escape the SVG onload attribute, executing the alert in the current browser session. This affects primarily Firefox and is self-contained, with no persistence or cross-user impact. The target is the web-based post preview or editor render.

## Requirements

1. Formatted payload in the post editor
2. Browser supporting SVG rendering (e.g., Firefox)
3. Active session without interruptions

## Defense

Defensive measures and detection strategies:

- Implement strict HTML escaping in all rendered content
- Browser-level protections like XSS auditors

## Objectives

1. Cause payload execution via rendering
2. Verify alert popup as proof-of-concept
3. Limit impact to self-session

## Instructions

### Step 1: Render the Post

**Context**: Allow or force the post to render to activate the onload event.

No command required; perform the following UI interaction:

The formatted post renders automatically in the editor or preview; observe the execution.

> An alert box with the domain name pops up, confirming JavaScript execution. In Firefox, this triggers reliably; check browser console for errors if no alert appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Slack-Self-XSS-Demonstration-Video]]

## Tags

- [[self-xss]]
- [[Execution]]

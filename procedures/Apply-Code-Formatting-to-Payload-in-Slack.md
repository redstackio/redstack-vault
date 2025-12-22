---
tags:
  - code-formatting
  - xss
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
updated_at: '2025-12-14T03:15:31.792Z'
sub_techniques: []
id: 72c1b24c-c185-40b2-b944-7744664711ef
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Apply-Code-Formatting-to-Payload-in-Slack

## Summary

This procedure applies code formatting to the XSS payload in the Slack editor, which fails to properly escape HTML and enables execution.

## Description

By highlighting the payload and selecting the code formatting option (<>), the content is marked as code but not sanitized for HTML/JS. This targets the vulnerability in Slack's rendering engine on the web platform. The outcome is the payload prepared for execution upon render, limited to self-impact.

## Requirements

1. Payload entered in the post editor
2. Visible formatting toolbar
3. Mouse or keyboard selection capability

## Defense

Defensive measures and detection strategies:

- Sanitize code blocks to escape HTML entities
- Audit formatting applications for malicious patterns

## Objectives

1. Format the payload to trigger the sanitization bypass
2. Maintain payload functionality
3. Prepare for rendering without errors

## Instructions

### Step 1: Format the Text

**Context**: Use the toolbar to apply code styling to the selected payload.

No command required; perform the following UI interaction:

Highlight the payload text, then click the code formatting symbol (<>) on the left side toolbar.

> The text is reformatted as code (monospace), and a preview may show it unchanged. Success is confirmed by the visual formatting change.

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

- [[code-formatting]]
- [[xss]]

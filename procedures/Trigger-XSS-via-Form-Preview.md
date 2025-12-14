---
id: proc-uuid-4
tags:
  - xss
  - execution
  - preview
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.939Z'
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
# Trigger-XSS-via-Form-Preview

## Summary

This procedure triggers the execution of the injected XSS payload by rendering the form preview in the Judge.me settings.

## Description

After injection, the success message is rendered unsanitized in the preview iframe or modal. The payload's img tag with onerror attribute executes JavaScript, popping an alert with the document domain. This confirms the vulnerability and demonstrates potential for further exploitation like cookie theft or keylogging in victim sessions.

## Requirements

1. Payload already injected in success message field
2. Active browser session in Judge.me settings
3. JavaScript execution enabled

## Defense

Defensive measures and detection strategies:

- Escape HTML in all preview renders
- Monitor for unexpected JavaScript errors or alerts in admin consoles
- Use sandboxed iframes for previews with restricted script execution

## Objectives

1. Render the form to activate the payload
2. Observe JavaScript execution
3. Validate impact on current session

## Instructions

### Step 1: Initiate Preview

**Context**: Use the built-in preview function to render the configured form.

Click the 'Preview' button adjacent to the form settings.

> Expected: A preview window or modal opens, displaying the review form with the success message embedded.

### Step 2: Observe Execution

**Context**: Confirm the payload triggers during render.

Watch for the alert dialog to appear, showing the domain.

> Expected: Alert box with 'document.domain' value; script executes silently otherwise.

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
- [[Execution]]
- [[preview]]

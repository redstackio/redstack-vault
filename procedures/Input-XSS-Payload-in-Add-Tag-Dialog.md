---
tags:
  - xss
  - payload-injection
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
updated_at: '2025-12-14T03:47:12.845Z'
sub_techniques: []
id: 32518b3b-ec9e-46c1-bd00-af1777483d4a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Input-XSS-Payload-in-Add-Tag-Dialog

## Summary

This procedure focuses on locating the add tag dialog on an XVIDEOS video page and inserting a JavaScript payload to test for reflection without sanitization, as part of exploiting the self-stored XSS vulnerability.

## Description

The add tag feature on XVIDEOS video pages allows user input for suggesting tags, which is stored and reflected in a dialog box. By entering a payload like `<script>alert(1)</script>`, the procedure tests if the input is executed upon later submission. This is a self-XSS scenario, affecting only the tester's browser, with root cause in lack of input escaping.

## Requirements

1. Loaded XVIDEOS video page from prior access
2. Web browser developer tools (optional, for inspection)
3. Basic knowledge of HTML/JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user inputs using libraries like DOMPurify
- Validate tag inputs server-side to block script tags
- Log and alert on suspicious input patterns in dialogs

## Objectives

1. Identify and open the add tag dialog
2. Inject unsanitized JavaScript payload
3. Prepare for submission without triggering premature errors

## Instructions

### Step 1: Locate Add Tag Feature

**Context**: Find the UI element for adding or suggesting tags on the video page.

Scroll to the tags section and click on 'Add Tag' or 'Suggest Tag' to open the dialog.

> The dialog should appear as a popup or inline form with an input field.

### Step 2: Enter Payload

**Context**: Insert the test payload into the input field to exploit the lack of sanitization.

Type or paste `<script>alert(1)</script>` into the text input.

> Ensure no auto-complete or filters interfere; the payload should be visible in the field.

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
- [[injection]]

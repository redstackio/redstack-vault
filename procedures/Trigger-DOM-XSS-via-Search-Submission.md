---
tags:
  - xss-execution
  - dom-reflection
  - trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: e3ccab97-f510-4e56-bf93-ebd89c0c868a
created_at: '2025-12-14T03:47:18.454Z'
updated_at: '2025-12-14T03:47:18.454Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-DOM-XSS-via-Search-Submission

## Summary

This procedure submits the search query containing the malicious payload, causing it to be reflected into the DOM and execute JavaScript in the browser, confirming the XSS vulnerability.

## Description

Upon submission, Nextcloud processes the input and inserts it into the page DOM without escaping, allowing the payload to run in the user's browser context. This can lead to actions like alerting messages or stealing document.cookie. The attack is client-side only, requiring user interaction, and impacts session data visibility.

## Requirements

1. Payload already injected in search field
2. Active browser session
3. No CSP blocking inline scripts

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP headers to block inline JavaScript
- Use DOMPurify or similar libraries for sanitization
- Detect via browser dev tools or WAF rules on script patterns

## Objectives

1. Cause payload reflection in the DOM
2. Execute JavaScript for impact demonstration
3. Validate vulnerability for reporting

## Instructions

### Step 1: Submit Search

**Context**: Initiate the reflection process by triggering the search handler.

Press Enter key or click the submit button in the search dialogue.

> The page updates, inserting the input into DOM elements like result lists.

### Step 2: Observe Execution

**Context**: Confirm script runs in the browser.

Watch for alert popups or check browser console for errors/logs from the payload.

> If successful, JavaScript executes, e.g., displaying cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[browser]]


---
tags:
  - xss-injection
  - payload
type: procedure
tools:
  - '[[tools/hexo-admin]]'
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
updated_at: '2025-12-14T17:29:09.707Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2e59e8d0-88f7-4a63-bcc2-d9f15d7d4560
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Post-Content

## Summary

This procedure exploits the unsanitized post content field in hexo-admin to inject JavaScript payloads that execute immediately and persist.

## Description

The post editor renders content without escaping HTML/JS, allowing closure-breaking payloads like img onerror to trigger alerts or steal data. This stored XSS affects all viewers of the published post, enabling session hijacking or phishing.

## Requirements

1. Open post editor in hexo-admin
2. Knowledge of basic XSS payloads
3. Local browser for testing execution

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with libraries like DOMPurify
- Escape HTML in content rendering
- Scan posts for script tags pre-publish

## Objectives

1. Insert payload to break out of context and execute JS
2. Confirm immediate execution in editor
3. Ensure payload survives saving without alteration

## Instructions

### Step 1: Enter Payload in Content Field

**Context**: Append the XSS string to any existing content to test injection.

No command; UI input.

> In the content textarea, add: `><img src=x onerror=alert("XSS")>` or `><img src=x onerror=alert(document.domain)>`. This breaks out of any surrounding tags.

### Step 2: Trigger and Verify

**Context**: Observe execution to confirm vulnerability.

No command; browser observation.

> As you type or switch focus, an alert popup should appear, proving JS execution in the editor context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/hexo-admin]]

## Tags

- javascript
- injection

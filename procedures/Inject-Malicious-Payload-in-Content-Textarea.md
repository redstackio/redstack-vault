---
tags:
  - xss
  - stored-xss
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
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 23869430-29b0-42d1-b040-4318fe0438b3
created_at: '2025-12-14T00:11:16.163Z'
updated_at: '2025-12-14T00:11:16.163Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-in-Content-Textarea

## Summary

This procedure injects a malicious HTML payload into the portal content textarea of the Return Magic app, exploiting the lack of sanitization to store executable JavaScript for later triggering in victim sessions.

## Description

The content editor allows raw HTML input without escaping or filtering, enabling stored XSS. The payload uses an onerror handler on a broken image tag to execute alert(2) as a proof-of-concept, but could be escalated to steal cookies, perform CSRF, or exfiltrate data. Once saved, it affects all users viewing the portal pages.

## Requirements

1. Access to Portal > Content editor in Return Magic
2. Knowledge of basic HTML/JavaScript
3. Active Shopify admin session

## Defense

Defensive measures and detection strategies:

- Implement HTML sanitization libraries (e.g., DOMPurify) on input
- Deploy Content Security Policy (CSP) to block inline scripts
- Scan stored content for suspicious tags like <img onerror>
- Log and review content changes in app settings

## Objectives

1. Store unsanitized malicious script in the database
2. Ensure payload persists across sessions
3. Enable execution in other users' browsers

## Instructions

### Step 1: Activate Code Editor

**Context**: Switch to raw HTML mode for injection.

In the content textarea, click the Code icon (</>) to enable HTML editing.

### Step 2: Insert Payload

**Context**: Add the malicious script disguised as content.

Type or paste: `Test <img src=x onerror=alert(2)>` into the textarea.

### Step 3: Save Changes

**Context**: Persist the injection.

Click the Save button to store the content without validation.

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
- [[stored-xss]]
- [[payload-injection]]

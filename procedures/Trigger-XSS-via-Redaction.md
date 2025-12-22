---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - xss
  - redaction
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.813Z'
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
# Trigger-XSS-via-Redaction

## Summary

This procedure triggers the stored XSS by viewing the public comment as an unauthorized user, causing the ReferenceRedactorFilter to unencode and inject the payload as executable HTML/JS.

## Description

Load the public issue page with the unauthorized account. The filter detects the inaccessible private link, extracts the encoded content from 'data-original', and inserts it without sanitization, executing the JS. Targets GitLab markdown rendering in issues/comments. Requires the injected comment; outcome is immediate JS execution like alert(1).

## Requirements

1. Unauthorized session active
2. Public issue with malicious comment
3. Browser capable of JS execution

## Defense

Defensive measures and detection strategies:

- Re-encode or sanitize redacted content in ReferenceRedactorFilter
- Log redaction events and anomalous JS injections
- Deploy strict CSP without 'unsafe-inline'

## Objectives

1. Activate redaction to unescape the payload
2. Execute arbitrary JS in the viewer's context
3. Confirm XSS for further exploitation

## Instructions

### Step 1: Load Public Issue

**Context**: Access the page containing the injected comment.

**Command** (UI Action):
Navigate to the public project's issue URL.

> Expected: Page renders with redacted link.

### Step 2: Observe Execution

**Context**: The filter processes on render, injecting the payload.

**Command** (UI Action):
Refresh the page if needed; watch for JS alert.

> Expected: `<img onerror=alert(1) src=x>` executes, showing alert dialog. Technical: Filter unescapes during redaction for inaccessible refs.

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
- [[redaction]]

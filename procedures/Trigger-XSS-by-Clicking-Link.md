---
id: 123e4567-e89b-12d3-a456-426614174005
name: Trigger-XSS-by-Clicking-Link
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.873Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - javascript
  - execution
commands: []
platforms:
  - Web
tools:
  - '[[tools/GitLab]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-XSS-by-Clicking-Link

## Summary

This procedure executes the XSS payload by interacting with the injected HTML element on the GitLab ZenTao issue page, running arbitrary JavaScript in the victim's browser.

## Description

Clicking the large injected image or link, which uses a javascript: URL, bypasses any remaining protections and executes code like alert(document.cookie), enabling account takeover or exfiltration on instances without strict CSP.

## Requirements

1. Loaded issue page with injected content
2. User interaction (click)
3. Browser without blocking javascript: schemes

## Defense

Defensive measures and detection strategies:

- Strict CSP disallowing unsafe-inline and javascript: URLs
- Sanitize and encode all rendered fields from external APIs
- User training on suspicious links in integrations

## Objectives

1. Execute JavaScript in GitLab context
2. Access victim session data
3. Perform actions like token generation or key addition

## Instructions

### Step 1: Identify Injected Element

**Context**: Locate the malicious link or image in the breadcrumb.

No command; inspect page for large <img> or <a> with javascript: URL.

> Payload example: <a href="javascript:alert('XSS')">Click me</a>

### Step 2: Interact to Execute

**Context**: Trigger the payload.

No command; click the element using mouse.

> Expected: JavaScript runs, e.g., alert pops or console executes payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitLab]]

## Tags

- [[xss]]
- [[JavaScript]]
- [[Execution]]

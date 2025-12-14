---
id: proc-zaption-inject-xss-001
tags:
  - xss
  - injection
  - web
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
updated_at: '2025-12-14T03:15:27.019Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Zaption Gallery Title

## Summary

This procedure demonstrates how to exploit the lack of input sanitization in Zaption's gallery title field to store a malicious JavaScript payload, which can later be triggered in various UI components for arbitrary code execution.

## Description

In Zaption's gallery feature, user-supplied titles for videos or tours are stored without proper escaping. By editing an existing item's title with an HTML-breaking payload, attackers can inject JavaScript that executes when the title is rendered in search suggestions, results, or listings. This stored XSS affects all users interacting with the gallery, enabling client-side attacks like session theft. Prerequisites include an authenticated account with edit permissions on gallery items; no advanced tools are needed beyond a web browser.

## Requirements

1. Authenticated Zaption user account with gallery edit access
2. Web browser for navigation and editing
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization and output encoding (e.g., HTML entity encoding) for all user-supplied fields rendered in HTML/JS contexts
- Use Content Security Policy (CSP) to restrict inline scripts and unsafe eval
- Monitor for anomalous JavaScript execution in browser logs or via WAF rules detecting common XSS patterns

## Objectives

1. Persist malicious JavaScript in a gallery title
2. Ensure payload survives storage and retrieval
3. Set up for global execution across user sessions

## Instructions

### Step 1: Access Gallery Edit Interface

**Context**: Log in and navigate to the gallery to select an editable video or tour, preparing for title injection.

Log in to Zaption at https://www.zaption.com, go to the gallery section, select an existing video or tour, and click 'Edit Info' under Gallery Info.

### Step 2: Craft and Insert Payload

**Context**: Enter the XSS payload in the title field to break out of any quoting and inject executable HTML/JS.

In the title input box, enter a payload such as `xyz123"><img src=x onerror=prompt("XSS")>`. This closes any open attributes/tags and injects an image with an onerror handler that executes JavaScript.

Click 'Done' to save the changes.

> The payload is now stored server-side. Verify by refreshing the edit page; the title should display as entered without errors.

### Step 3: Validate Storage

**Context**: Confirm the payload is persisted without sanitization.

Re-edit the item or search for it to ensure the full payload (including tags) is retrievable.

**Expected Output**: Title saves successfully, and payload is intact on retrieval.

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
- injection

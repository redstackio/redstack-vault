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
updated_at: '2025-12-13T23:52:33.381Z'
sub_techniques: []
id: a67a05c1-d287-4f1e-8dda-63c377a57b85
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inject-Malicious-Payload

## Summary

This procedure involves entering a crafted JavaScript payload into the Discourse search field, disguised as an email address, to exploit reflection in subsequent URLs.

## Description

The payload `@<script>prompt(1337)</script>gmail.com` leverages the '@' symbol to mimic a user mention or email search, bypassing basic input validation. When searched, it gets reflected into the URL without escaping, setting up DOM-based XSS execution upon URL parsing in the advanced search view.

## Requirements

1. Open search interface from previous procedure
2. Knowledge of target payload format
3. Browser with developer tools for inspection

## Defense

Defensive measures and detection strategies:

- Implement input sanitization for search queries, escaping HTML/JS characters
- Use Content Security Policy (CSP) to block inline scripts

## Objectives

1. Submit payload without rejection
2. Observe reflection in search results
3. Confirm no immediate execution (deferred to next step)

## Instructions

### Step 1: Enter Payload

**Context**: Craft and input the malicious string to simulate a legitimate search.

Type `@<script>prompt(1337)</script>gmail.com` into the search box.

> Expected: Input is accepted; no parsing errors.

### Step 2: Submit Search

**Context**: Trigger the search to process and reflect the payload.

Press Enter or click the search submit button.

> Expected: Results page loads with payload visible in query parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dom-xss
- javascript-injection

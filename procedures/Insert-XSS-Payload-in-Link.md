---
tags:
  - xss
  - payload-injection
  - javascript
type: procedure
tools:
  - '[[tools/Summernote-JS]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 186a263e-fec1-4f1d-b0ea-9da7ac63d5d2
created_at: '2025-12-13T23:55:20.630Z'
updated_at: '2025-12-13T23:55:20.630Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Insert-XSS-Payload-in-Link

## Summary

This procedure injects a malicious JavaScript payload into a link within the email template, exploiting the sanitization flaw in Summernote JS.

## Description

By inserting a `javascript:` URI as a link URL, the payload evades client-side checks and stores malicious code. When rendered, it executes in the victim's session, stealing cookies. This is specific to Judge.me's template editor in Shopify.

## Requirements

1. Active template editor with block selected
2. Knowledge of XSS payloads (e.g., alert(document.cookie))
3. No additional tools beyond browser

## Defense

Defensive measures and detection strategies:

- Sanitize all link URLs to block javascript: schemes
- Use DOMPurify or similar libraries for HTML sanitization
- Scan templates for suspicious protocols in links

## Objectives

1. Embed JavaScript in a hyperlink
2. Disguise as benign text
3. Ensure persistence without errors

## Instructions

### Step 1: Insert Malicious Link

**Context**: Add the payload via the link tool.

No command required; editor action:

- Highlight text like "Click Here", click link icon, enter `javascript:alert(document.cookie)` as URL, apply.

> Expected output: Link created; inspect HTML to confirm <a href="javascript:alert(document.cookie)">Click Here</a>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Summernote-JS]]

## Tags

- [[xss]]
- [[payload-injection]]
- [[JavaScript]]

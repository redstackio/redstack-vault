---
id: p2b3c4d5-f6g7-8901-bcde-f2345678901
tags:
  - xss-injection
  - input-sanitization-bypass
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
updated_at: '2025-12-13T23:52:38.772Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Private-Message

## Summary

This procedure involves entering a malicious JavaScript payload into ok.ru's private message input field, exploiting the absence of sanitization to prepare for execution in the recipient's browser.

## Description

ok.ru's message composition lacks proper input filtering, allowing direct injection of HTML and JavaScript. Combined with special usernames, payloads like `<script>alert('XSS');</script>` are preserved and rendered as executable code when viewed, leading to client-side attacks such as cookie theft.

## Requirements

1. Logged-in ok.ru account with special character username
2. Target victim's username
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Enforce server-side and client-side input validation
- Escape HTML in message rendering
- Use DOMPurify or similar libraries for sanitization

## Objectives

1. Bypass input validation in message field
2. Preserve payload integrity during composition
3. Enable execution upon rendering

## Instructions

### Step 1: Navigate to Private Messaging

**Context**: Access the messaging interface to compose a new message.

In the browser, go to ok.ru, log in, and click on 'Messages' to start a new private message to the target.

> Expected: Composition field appears without restrictions.

### Step 2: Enter Malicious Payload

**Context**: Inject the XSS script into the input field.

Type a payload such as `<script>alert(document.cookie);</script>` into the message box, incorporating special username elements if needed for chaining.

> Expected: Payload entered without filtering; no errors on submit preview.

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
- [[payload-injection]]

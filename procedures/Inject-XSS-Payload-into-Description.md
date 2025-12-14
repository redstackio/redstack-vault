---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - xss
  - injection
  - javascript
  - adobe
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
updated_at: '2025-12-14T03:15:52.999Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Description

## Summary

This procedure injects a malicious JavaScript payload into the description field of Adobe's file sharing form, exploiting lack of sanitization to store and later execute the code on victims.

## Description

Targeting the description field in https://cloud.acrobat.com/send, this step inserts HTML/JS like `<img src=x onerror=alert(1)>`, which is stored server-side and rendered unsafely in the file preview (e.g., https://files.acrobat.com/a/preview/[id]). This leads to arbitrary JS execution for authenticated or anonymous users. Prerequisites: Completed prior form steps. Outcomes: Payload stored without filtering.

## Requirements

1. Sharing form with subject entered
2. Web browser developer tools (optional for testing)

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity escaping) to description rendering
- Use Content Security Policy (CSP) to block inline scripts and unsafe images
- Scan inputs for common XSS patterns like onerror handlers

## Objectives

1. Exploit input validation flaw in description
2. Store malicious script for later execution
3. Enable client-side code injection on victims

## Instructions

### Step 1: Locate Description Field

**Context**: Identify the vulnerable textarea for additional notes.

Find the 'Description' or 'Message' field below the subject.

> It allows multi-line input for sharing details.

### Step 2: Insert Payload

**Context**: Enter the XSS vector to trigger on render.

Type `<img src=x onerror=alert(1)>` into the description field.

> The input is accepted raw, without escaping, confirming vulnerability.

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
- injection
- javascript

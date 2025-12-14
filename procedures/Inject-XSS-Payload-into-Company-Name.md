---
id: proc-inject-xss-drive2
tags:
  - xss-injection
  - payload
  - javascript
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
updated_at: '2025-12-13T23:52:33.535Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Company-Name

## Summary

This procedure involves entering a malicious JavaScript payload into the 'Company Name' field of the drive2.ru business account form, exploiting the lack of input sanitization to store executable code.

## Description

The 'Название компании' field on drive2.ru accepts user input without proper escaping, allowing HTML and JavaScript tags like an SVG onload event to be injected. This targets the web form in an authenticated session, with outcomes including payload persistence upon save, leading to execution on the public company page for any visitor.

## Requirements

1. Access to the company management form
2. Knowledge of XSS payloads (e.g., SVG-based for broad compatibility)
3. Browser developer tools for payload testing if needed

## Defense

Defensive measures and detection strategies:

- Sanitize inputs by encoding special characters (e.g., < to &lt;)
- Validate input length and content patterns for company names
- Content Security Policy (CSP) to block inline scripts

## Objectives

1. Insert executable JavaScript without form rejection
2. Ensure payload survives basic client-side checks
3. Prepare for backend persistence

## Instructions

### Step 1: Locate Vulnerable Field

**Context**: Identify the 'Company Name' input in the form.

Scroll to the 'Название компании' field in the management panel.

> Confirm it's a text input without visible restrictions on HTML.

### Step 2: Enter Payload

**Context**: Input the XSS payload to test execution potential.

Type `<svg/onload=confirm(document.domain)>` into the field, and fill other required fields with benign data (e.g., fake address).

> Use browser dev tools (F12) to inspect if the input is altered on blur.

### Step 3: Validate Payload Integrity

**Context**: Check that the payload remains intact before saving.

Tab out of the field or preview if available to ensure no auto-escaping occurs.

> Expected: Payload displays as-is in the input value.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-injection
- payload
- javascript

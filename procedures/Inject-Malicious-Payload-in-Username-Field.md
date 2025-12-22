---
tags:
  - xss-injection
  - payload-storage
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
updated_at: '2025-12-13T23:52:25.332Z'
sub_techniques: []
id: ef8f927e-d7b4-43a4-ad7e-27a6b68e8395
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-in-Username-Field

## Summary

This procedure exploits the lack of input sanitization in the SMTP2GO username field during user creation to store a malicious JavaScript payload, enabling stored XSS attacks when the data is later rendered.

## Description

The add SMTP user form accepts arbitrary input in the username field without HTML entity encoding or script filtering. The payload `<form><input type="date" onfocus="alert(1)">` leverages an onfocus event to execute when focused, commonly triggered in dropdown selections. Prerequisites include an authenticated session; outcomes involve persistent storage of executable code.

## Requirements

1. Access to the Add SMTP User form
2. Knowledge of XSS payloads that evade basic filters
3. Browser developer tools for testing payload variations

## Defense

Defensive measures and detection strategies:

- Server-side input validation and sanitization (e.g., OWASP guidelines)
- Content Security Policy (CSP) to block inline scripts
- WAF rules to detect and block common XSS patterns in inputs

## Objectives

1. Successfully store unsanitized JavaScript in the username
2. Verify storage without immediate execution
3. Set up for cross-user impact via shared interfaces

## Instructions

### Step 1: Initiate User Creation

**Context**: Open the form to input the vulnerable field.

Click the "Add SMTP User" button on the SMTP users page.

### Step 2: Enter Malicious Payload

**Context**: Craft and insert the payload to exploit the storage flaw.

In the username field, enter: `<form><input type="date" onfocus="alert(1)">`. Optionally encode if basic filters apply (e.g., use HTML entities like &lt; for <).

### Step 3: Save the User

**Context**: Persist the payload in the application's database.

Complete any other required fields (e.g., password) and click save.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[web]]


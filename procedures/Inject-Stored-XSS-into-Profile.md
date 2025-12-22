---
id: proc-uuid-003
tags:
  - stored-xss
  - javascript-injection
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
updated_at: '2025-12-14T17:33:06.493Z'
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
# Inject-Stored-XSS-into-Profile

## Summary

This procedure injects a stored XSS payload into profile fields like first name, which persists and executes JavaScript when the profile is viewed by the legitimate user.

## Description

The site's profile editing lacks input sanitization, allowing HTML and JavaScript injection into fields that are later rendered unsafely. Payloads like event handlers (e.g., onfocus) bypass basic filters, storing malicious code server-side for execution on victim visits. This chains from account takeover to drive-by attacks.

## Requirements

1. Compromised account session
2. Knowledge of XSS payloads
3. Access to profile edit form

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs in storage and output
- Use Content Security Policy (CSP) to block inline scripts
- Audit profile changes for suspicious content

## Objectives

1. Store persistent JavaScript for later execution
2. Target victim browsers for code execution
3. Enable redirects or prompts for phishing

## Instructions

### Step 1: Access Profile Edit

**Context**: Open the editable profile fields.

In the profile section, select edit mode for fields like first name.

**Expected Output**: Form fields become editable.

### Step 2: Insert XSS Payload

**Context**: Craft and submit a payload that evades filters.

Enter payload such as `ant" autofocus onfocus=prompt(1) x="` or `l" autofocus onfocus=location.replace("https://evil.com/") x=""` into the first name field and save.

**Expected Output**: Profile saves with payload stored; no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[javascript-injection]]

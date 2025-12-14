---
tags:
  - xss
  - payload-injection
  - trac
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: eadb1c34-990e-4f6a-b70d-1d384e8e044d
created_at: '2025-12-14T00:11:25.234Z'
updated_at: '2025-12-14T00:11:25.234Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Malicious Payload into Workflow Keyword

## Summary

This procedure details injecting a malicious SVG payload into the workflow keyword field during Trac ticket creation to exploit the stored XSS vulnerability.

## Description

The keyword field allows manual entry, and input is not properly escaped, leading to stored XSS when generating delete buttons via JavaScript. The payload "><svg/onload=alert(document.domain)> triggers an alert, but can be adapted for cookie theft or other attacks.

## Requirements

1. Access to ticket creation form
2. Knowledge of XSS payloads
3. Web browser

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user input in forms
- Use Content Security Policy (CSP) to restrict script execution

## Objectives

1. Inject executable JavaScript
2. Store payload in ticket data
3. Enable cross-user execution

## Instructions

### Step 1: Select Keyword Field

**Context**: Enable manual entry for keywords.

Select a Workflow Keyword and click manual entry.

> Field becomes editable.

### Step 2: Paste Payload

**Context**: Insert the malicious string.

Paste the payload: "><svg/onload=alert(document.domain)>.

> Payload is entered without validation errors.

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
- payload-injection
- trac

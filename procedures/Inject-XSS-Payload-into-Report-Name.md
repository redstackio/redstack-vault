---
tags:
  - xss
  - payload-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 0a9ade23-9631-4923-a1eb-4f358f7d88f4
created_at: '2025-12-13T23:56:20.437Z'
updated_at: '2025-12-13T23:56:20.437Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Report Name

## Summary

This procedure injects a malicious XSS payload into the report name field during creation in MoPub.

## Description

Entering the payload exploits insufficient sanitization, allowing scripts to persist. This can lead to execution in viewers' browsers, stealing data. Outcome is payload acceptance.

## Requirements

1. Open report creation form
2. Knowledge of XSS payloads
3. Browser for input

## Defense

Defensive measures and detection strategies:

- Sanitize inputs and escape outputs
- Use content security policy (CSP) to block inline scripts

## Objectives

1. Insert persistent malicious script
2. Exploit vulnerability for storage
3. Prepare for execution on view

## Instructions

### Step 1: Enter Payload in Name Field

**Context**: Input the XSS payload into the designated field.

**Instructions**: Type "><img src=x onerror=alert(document.domain)> into the name field.

> This injects the script without sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[payload-injection]]

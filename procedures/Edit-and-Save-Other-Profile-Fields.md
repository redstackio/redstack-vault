---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - trigger
  - edit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.346Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Edit-and-Save-Other-Profile-Fields

## Summary

This procedure modifies unrelated profile fields and resubmits the form, causing the stored BIO payload to re-render and execute as XSS.

## Description

By editing fields like REAL NAME or LOCATION and saving, the profile form re-processes all stored data, including the malicious BIO. Insufficient escaping during this re-render triggers the JavaScript. This targets the Khan Academy profile endpoint, leading to execution in the user's browser context.

## Requirements

1. Previously stored malicious BIO
2. Access to profile editor
3. Browser session active

## Defense

Defensive measures and detection strategies:

- Escape all stored data on every form render
- Implement strict output encoding for user-generated content
- Use event monitoring to detect unexpected script loads

## Objectives

1. Resubmit form to re-render stored payload
2. Initiate XSS execution
3. Limit impact to current session

## Instructions

### Step 1: Modify Other Fields

**Context**: Alter non-BIO fields to force a form resubmission that includes the stored payload.

Return to the profile editing page, change the REAL NAME to a test value like "Test User" or LOCATION to "Test Location", then click SAVE.

> The form submission re-loads the BIO content, executing the payload after a brief delay.

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
- [[trigger]]

---
tags:
  - xss
  - trigger
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Online-String-Tools]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: cd0863f6-bb1c-4457-84f9-a11490376fa3
created_at: '2025-12-11T06:10:15.971Z'
updated_at: '2025-12-11T06:10:15.971Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Trigger XSS via Chat Upload

## Summary

This procedure involves uploading the modified file and opening the support chat to trigger the execution of the injected XSS payload.

## Description

After injecting the payload, the file is uploaded, and accessing the chat causes the malicious JavaScript to run in the browser, potentially stealing cookies or performing other actions.

## Requirements

1. Modified request forwarded successfully.
2. Access to the support chat interface.
3. Browser to open the chat.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded filenames.
- Monitor chat logs for suspicious script executions.

## Objectives

1. Execute the injected JavaScript.
2. Confirm payload activation.
3. Achieve cookie exfiltration.

## Instructions

### Step 1: Upload File

**Context**: Forward the modified request to complete upload.

Forward the request in Burp Suite.

### Step 2: Open Chat

**Context**: Access the chat to trigger the payload.

Navigate to the support chat on support.cs.money to activate the XSS.

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
- trigger
- web

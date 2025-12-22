---
tags:
  - payload-injection
  - javascript
type: procedure
tools:
  - '[[tools/Mashery-Dashboard]]'
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
updated_at: '2025-12-14T04:38:39.521Z'
sub_techniques: []
id: c6e25d4d-b698-44a6-b0ac-f29d57cf393e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Configure-Malicious-Content-on-Takeover

## Summary

Edit the Mashery portal to inject custom content, such as JavaScript for proof-of-concept or malicious payloads.

## Description

Add code like 'alert(document.domain)' to the welcome page, allowing arbitrary hosting for phishing or theft under the trusted domain.

## Requirements

1. Controlled subdomain in dashboard
2. Basic JavaScript knowledge
3. No additional auth

## Defense

Defensive measures and detection strategies:

- Scan for injected scripts on subdomains
- Implement CSP headers
- Regularly review third-party configs

## Objectives

1. Customize portal content
2. Enable JS execution
3. Demonstrate impact

## Instructions

### Step 1: Edit Welcome Page

**Context**: Access content editor.

In Mashery dashboard, locate the welcome page editor.

**Expected Output**: Editable HTML/JS section.

### Step 2: Inject JavaScript

**Context**: Add POC code.

Insert <script>alert(document.domain)</script> and save.

**Expected Output**: Updated page with script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] Command and Scripting Interpreter: JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mashery-Dashboard]]

## Tags

- [[payload-injection]]
- [[JavaScript]]

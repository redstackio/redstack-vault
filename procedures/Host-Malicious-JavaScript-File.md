---
id: proc-uuid-host-js
tags:
  - payload-hosting
  - javascript
  - xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:26:17.688Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-Malicious-JavaScript-File

## Summary

This procedure creates and hosts a JavaScript file containing XSS payloads on a remote server, enabling its inclusion via RFI in the vulnerable SWF.

## Description

To exploit the FlowPlayer RFI, a malicious JS file must be publicly accessible. The file includes simple alert payloads to demonstrate execution, such as revealing cookies or domain info. Hosting can be done on free services like GitHub or a personal server. This step assumes basic web hosting knowledge and focuses on payload design for JS execution on load.

## Requirements

1. Remote server or hosting service (e.g., GitHub Pages)
2. Text editor for JS creation
3. Public URL generation

## Defense

Defensive measures and detection strategies:

- Scan for and block known malicious JS hosts
- Use network monitoring for unusual file uploads to external domains
- Implement referrer policies to restrict cross-origin loads

## Objectives

1. Create JS with XSS payloads (e.g., alert(document.cookie))
2. Host file accessibly (e.g., http://[redacted]/test.js)
3. Verify load and execution

## Instructions

### Step 1: Create JS File

**Context**: Develop payloads that execute immediately on inclusion.

Write test.js:

```javascript
alert(document.cookie);
alert(document.domain);
```

> Save as test.js.

### Step 2: Upload and Host

**Context**: Make the file publicly available.

Upload to server and note URL: http://[redacted]/test.js.

> Test by accessing URL directly; expect no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[payload-creation]]
- [[remote-hosting]]

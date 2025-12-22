---
id: proc-host-js-payload
tags:
  - payload-hosting
  - javascript
  - xss
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:47:18.642Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host Malicious JavaScript Payload

## Summary

This procedure involves creating and hosting a JavaScript file with XSS payloads to be loaded via RFI, enabling arbitrary code execution in the target's context.

## Description

A simple JS file (test.js) contains payloads like alert(document.cookie) to demonstrate cookie access and alert(document.domain) for domain confirmation. Host it on a remote server (e.g., using Python's http.server or a VPS). The file must be accessible via HTTP to allow the SWF's 'config' parameter to include it. This step assumes control over a web server and focuses on payload simplicity for proof-of-concept. Expected outcome: A publicly reachable URL for the JS.

## Requirements

1. Controllable web server or hosting service
2. Text editor to create the JS file
3. Public HTTP access for the payload

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous JS file hosts and block known malicious domains
- Implement Content Security Policy (CSP) to restrict external script loads
- Log and alert on unexpected script inclusions in Flash or web apps

## Objectives

1. Create JS payloads targeting cookies and domain
2. Host the file for remote inclusion
3. Verify accessibility for exploitation

## Instructions

### Step 1: Create Payload File

**Context**: Write JS code to execute upon inclusion.

Create test.js with content:

```javascript
alert(document.cookie);
alert(document.domain);
```

> Save as test.js; this will trigger popups on execution.

### Step 2: Host the File

**Context**: Serve the file publicly.

Upload to a server at http://[redacted]/test.js and confirm access via browser.

> Ensure no authentication or HTTPS-only restrictions block Flash loading.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[JavaScript]]
- [[payload]]

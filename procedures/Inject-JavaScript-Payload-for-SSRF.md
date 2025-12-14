---
id: proc-uuid-3
name: Inject JavaScript Payload for SSRF
tags:
  - ssrf
  - javascript
  - injection
  - aws
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:28.643Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject JavaScript Payload for SSRF

## Summary

This procedure modifies the intercepted /api/save/ JSON payload in Burp Suite Repeater to inject a closing script tag followed by a new script that dynamically writes an iframe sourcing the AWS EC2 metadata endpoint. When saved and later rendered in PDF generation, the server executes this client-side-like code server-side, triggering SSRF to fetch internal credentials.

## Description

The 'name' field in 'globalInfo' is vulnerable to script injection due to poor sanitization. The payload closes any existing script context and injects one that creates an iframe to http://169.254.169.254/latest/meta-data/iam/security-credentials/EC2CloudWatchRole. During PDF regen, the server processes this as HTML/JS, making the internal request and embedding the response (credentials) in the output.

## Requirements

1. Intercepted /api/save/ request in Burp Repeater
2. Knowledge of JSON structure and HTML/JS syntax
3. Target AWS instance with IAM role (e.g., EC2CloudWatchRole)

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to remove script tags and HTML attributes (e.g., src=)
- Disable server-side JS execution in PDF libraries
- Block outbound requests from app servers to metadata IPs (169.254.169.254)

## Objectives

1. Craft and inject payload without triggering validation errors
2. Ensure server accepts the modified JSON
3. Prepare for SSRF execution on PDF refresh

## Instructions

### Step 1: Edit JSON Payload

**Context**: Locate and alter the vulnerable 'name' field to break out of script context.

In Repeater, find 'name' in 'globalInfo' and replace its value with: '</script><script>document.write("<iframe src=\"http://169.254.169.254/latest/meta-data/iam/security-credentials/EC2CloudWatchRole\" width=1000px height=1000px>")</script>'.

> Escaped quotes prevent JSON breakage.

### Step 2: Send Modified Request

**Context**: Replay the altered request to update the session data on the server.

Click 'Send' in Repeater.

> Server responds with {'status': 'ok'} if accepted.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssrf
- javascript
- injection
- aws

---
tags:
  - xss
  - payload-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/modify-upload-parameters]]'
  - '[[commands/sign-oauth-request]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2ab1ad49-7161-4f6d-99d5-b29c113f4b05
created_at: '2025-12-13T23:56:20.132Z'
updated_at: '2025-12-13T23:56:20.132Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload via Modified Upload

## Summary

This procedure involves injecting an XSS payload into the uploaded file content after bypassing restrictions, enabling script execution on ton.twitter.com when accessed by victims.

## Description

Building on the upload bypass, replace the file content with malicious JavaScript. The file is served without a Content-Type header, causing browsers to interpret it as HTML and execute the script. Signing with OAuth escalates to affect others.

## Requirements

1. Intercepted upload request from previous steps
2. XSS payload ready (e.g., <script>alert(1)</script>)
3. OAuth token for signing

## Defense

Defensive measures and detection strategies:

- Enforce Content-Type headers on served files
- Scan uploads for malicious content

## Objectives

1. Inject and store XSS payload
2. Make the file accessible via signed requests
3. Trigger self-XSS escalatable to victims

## Instructions

### Step 1: Replace Content with Payload

**Context**: Modify the content parameter in the request.

**Command** ([[commands/modify-upload-parameters]]):

```bash
# Set _content_ to <script>alert(1)</script>
```

> This injects the XSS vector into the file.

### Step 2: Sign and Share

**Context**: Use OAuth to sign the request for victim access.

**Command** ([[commands/sign-oauth-request]]):

```bash
# Generate signed URL with OAuth token
```

> Allows victims to access and trigger the XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/modify-upload-parameters]]
- [[commands/sign-oauth-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- payload-injection

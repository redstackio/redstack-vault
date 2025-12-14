---
tags:
  - ssrf
  - port-80
  - nginx
  - gitlab-webhook
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:10.154Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b3aebe20-1b43-400b-9c08-afb00d62a637
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Test-SSRF-on-Port-80-via-GitLab-Webhook

## Summary

This procedure exploits SSRF by submitting a localhost URL targeting port 80 in the GitLab webhook, revealing internal nginx server details through response errors.

## Description

The webhook URL field lacks validation, allowing http://127.0.0.1:80/haha.txt as input. Upon testing, GitLab makes a server-side request to the internal address, returning details like nginx/1.12.1 errors, confirming intranet access and enabling port scanning.

## Requirements

1. Access to GitLab project integrations
2. Authenticated session
3. Knowledge of target internal ports

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting to block localhost and private IPs
- Monitor webhook execution logs for internal connection attempts
- Use WAF rules to detect and block SSRF payloads in integrations

## Objectives

1. Trigger SSRF to probe internal port 80
2. Extract server details from error responses
3. Validate vulnerability for further scanning

## Instructions

### Step 1: Enter SSRF Payload

**Context**: Input the localhost URL in the webhook field.

In the webhook URL field, enter http://127.0.0.1:80/haha.txt.

> Field accepts the URL without validation.

### Step 2: Test Integration

**Context**: Execute the webhook to trigger the request.

Save or click 'Test' to run the hook.

> Response: 'Hook executed successfully but returned HTTP 404' including nginx/1.12.1 details.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[port-80]]
- [[nginx]]
- [[gitlab-webhook]]

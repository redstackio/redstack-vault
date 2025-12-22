---
tags:
  - xss
  - request-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b3020c90-e148-40a3-8687-1a249b03b3dd
created_at: '2025-12-14T00:11:25.259Z'
updated_at: '2025-12-14T00:11:25.259Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept and Modify Upload Request for XSS Injection

## Summary

This procedure involves setting up a proxy to intercept and modify file upload requests to inject XSS payloads into unsanitized parameters, enabling stored XSS attacks.

## Description

The procedure targets web endpoints like support.cs.money/upload_file where filename parameters are not sanitized, allowing malicious JavaScript injection. It requires proxy tools to capture requests, modify parameters, and forward them, leading to arbitrary code execution when viewed.

## Requirements

1. Access to the target web application and upload feature
2. Proxy tool like Burp Suite installed and configured
3. Network access to the target endpoint

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and escaping for all user-controlled parameters
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous request modifications or proxy usage in logs

## Objectives

1. Inject malicious payload into stored data
2. Enable arbitrary JavaScript execution
3. Achieve cookie theft or session hijacking

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept requests.

Turn on intercept in Burp Suite and configure browser to use the proxy.

> This allows capturing the upload request.

### Step 2: Capture and Modify Request

**Context**: Intercept the upload request and inject XSS.

In Burp Suite, modify the filename parameter in the captured request to include the XSS payload.

> Ensures the payload is stored without sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- request-interception

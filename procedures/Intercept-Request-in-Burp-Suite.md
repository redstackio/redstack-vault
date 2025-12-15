---
tags:
  - intercept
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:53.857Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0128ce9b-014f-4807-b4da-4985e9f51931
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Intercept-Request-in-Burp-Suite

## Summary

This procedure configures Burp Suite to intercept HTTP requests, capturing one with the malicious cookie for further exploitation.

## Description

Burp Suite's proxy intercepts traffic, allowing inspection of the Cookie header with the injected payload. Reloading the page sends the request through the proxy, where the unescaped cookie can be processed by the extension.

## Requirements

1. Burp Suite running with proxy listener on 127.0.0.1:8080
2. Browser proxy set to Burp
3. Malicious cookie already set

## Defense

Defensive measures and detection strategies:

- Disable unnecessary proxy interceptions
- Log and review intercepted requests for anomalies
- Use certificate pinning to prevent MITM

## Objectives

1. Capture request with malicious Cookie header
2. Verify payload in headers
3. Forward for code generation

## Instructions

### Step 1: Enable Interception

**Context**: Turn on Burp's intercept feature.

**Instructions**: In Burp Proxy > Intercept tab, toggle 'Intercept is on'.

### Step 2: Trigger Request

**Context**: Send the request containing the cookie.

**Instructions**: Reload the browser tab for https://example.com/.

> The request pauses in Burp; inspect the Cookie header for the payload like 'test='/require('child_process').exec('calc.exe')//'. Forward the request to continue.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Software

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- proxy

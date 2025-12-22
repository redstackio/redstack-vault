---
id: proc-fuzz-burp-001
tags:
  - fuzzing
  - path-traversal
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Network Device
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:44.950Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fuzzing-Web-UI-Path-Bypass-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and fuzz HTTP requests to the Cisco IOS XE web UI, identifying path traversal payloads that bypass Nginx filtering and access the unauthenticated webui_wsma_http endpoint.

## Description

The attack targets improper path validation in Cisco IOS XE's web UI (CVE-2023-20198). By proxying traffic through Burp Suite, attackers manually test paths in Repeater and automate fuzzing in Intruder with payloads like black box characters or '../' sequences. This reveals bypasses to SOAP endpoints (wsma-exec, wsma-config), enabling unauthenticated access. Target environment: Cisco IOS XE with web UI exposed; expected outcome: direct endpoint access without auth redirects.

## Requirements

1. Burp Suite installed and configured as a proxy
2. Network access to the target's web UI (e.g., https://<target>/webui)
3. Browser or tool configured to route traffic through Burp

## Defense

Defensive measures and detection strategies:

- Patch Cisco IOS XE to versions mitigating CVE-2023-20198
- Configure Nginx with strict path validation and WAF rules for traversal attempts
- Monitor HTTP logs for fuzzing patterns (e.g., repeated Intruder payloads)

## Objectives

1. Identify vulnerable paths bypassing Nginx filters
2. Gain unauthenticated access to wsma-http endpoints
3. Prepare for command injection via SOAP

## Instructions

### Step 1: Intercept Web UI Request

**Context**: Capture a standard web UI request to set up for manipulation.

Configure browser proxy to Burp and navigate to the web UI login or search page.

> In Burp, right-click the request and send to Repeater for initial manual tests with path modifications (e.g., append %00../ to URLs).

Expected output: Intercepted request showing original path like /webui/logoutconfirm.html.

### Step 2: Fuzz with Intruder

**Context**: Automate testing of bypass payloads to find working traversals.

Send the request from Proxy or Repeater to Intruder. Set payload positions on the path (e.g., § for insertion points) and load a list of fuzzing payloads (black box chars, ../, null bytes).

> Run the attack; analyze responses for non-404 or auth-bypassed SOAP replies.

Expected output: Successful payload (e.g., /webui/logoutconfirm.html%00../../wsma/device) yielding 200 OK from wsma-http.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[fuzzing]]
- [[path-traversal]]
- [[bypass]]

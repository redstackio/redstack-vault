---
id: proc-2712857-analyze-endpoint
tags:
  - csrf
  - recon
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:24.490Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze-Profile-Edit-Endpoint-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and inspect HTTP requests to the profile edit endpoint, identifying the absence of CSRF protections for potential exploitation.

## Description

Burp Suite acts as a proxy to capture traffic during profile modifications, revealing form parameters and security headers. In this scenario, the POST to /account/profile/edit lacks CSRF tokens, enabling forged requests. This analysis confirms the vulnerability in a web application handling sensitive account changes.

## Requirements

1. Burp Suite Professional installed and running
2. Browser configured to proxy through Burp (127.0.0.1:8080)
3. Authenticated session on the target site

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Use SameSite=Strict cookies for session management
- Log and alert on requests missing CSRF headers

## Objectives

1. Capture and dissect the profile edit request
2. Verify lack of anti-CSRF mechanisms
3. Document parameters for POC creation

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception to monitor traffic to the target endpoint.

Launch Burp Suite, ensure Proxy listener on 8080, configure browser proxy settings accordingly.

> Proxy active, ready for request capture.

### Step 2: Trigger Profile Edit Request

**Context**: Submit a form change to generate interceptable traffic.

With proxy enabled, navigate to https://target.com/account/profile/edit, modify first name, email, password, and submit.

> Request appears in Burp's Proxy > HTTP history tab.

### Step 3: Inspect for CSRF Protections

**Context**: Analyze the request to confirm vulnerability.

In Burp history, select the POST request, check for CSRF token fields (e.g., _token) in body, or headers like Origin/X-Requested-With.

> No protections found, parameters like username, email, password visible and modifiable.

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

- csrf
- recon
- web


---
id: proc-uuid-002
tags:
  - csrf
  - web
  - request-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.924Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Account-Deletion-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept the POST request sent during account deletion initiation, revealing the lack of CSRF tokens and enabling further exploitation.

## Description

Targeted at web applications like the DoD portal, this captures the /users/deleteAccount endpoint request after proxy configuration. It confirms vulnerability by inspecting for missing protections like tokens or origin checks. Prerequisites include an active Burp proxy and authenticated session.

## Requirements

1. Burp Suite installed and running with proxy listener on localhost:8080
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Authenticated test account from prior preparation

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or repeated deletion attempts
- Enforce HTTPS and HSTS to complicate interception
- Log all POST requests to sensitive endpoints like /users/deleteAccount

## Objectives

1. Isolate the deletion request for analysis
2. Verify absence of CSRF mitigations
3. Collect parameters for PoC generation

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception to capture traffic from the target site.

Launch Burp Suite, ensure the Proxy tab is active, and turn on 'Intercept is on'.

**Expected Output**: Burp ready to pause and display requests.

### Step 2: Trigger and Intercept Request

**Context**: Perform the deletion action to send the POST request through the proxy.

With proxy active, click 'DELETE ACCOUNT' and confirm with 'YES'. Burp will intercept the POST to /users/deleteAccount.

**Expected Output**: Request details in Burp, showing body like confirmation=YES and no CSRF token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
- [[request-capture]]

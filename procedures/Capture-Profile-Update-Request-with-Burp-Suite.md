---
tags:
  - request-capture
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:12.356Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 892c007d-7f4b-41b3-b8f8-c84e0cf7b922
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Capture-Profile-Update-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and capture the HTTP request for updating the attacker's profile, revealing the structure and user ID used in the endpoint for later IDOR exploitation.

## Description

To exploit IDOR, understanding the exact request format is crucial. By logging into the attacker account and triggering a profile update (e.g., changing an address field), the POST request to the update endpoint is captured. This includes parameters like 'username' (email) and the path with numeric ID. The request is forwarded to Repeater for manipulation without alerting the server.

## Requirements

1. Installed and running Burp Suite with browser proxy configured (e.g., Firefox set to 127.0.0.1:8080)
2. Active attacker account from previous setup
3. Access to profile update feature on the target site

## Defense

Defensive measures and detection strategies:

- Log all profile update requests and audit for anomalous user agents (e.g., Burp)
- Implement client-side fingerprinting to detect proxy usage
- Use HTTPS with HSTS to complicate interception

## Objectives

1. Intercept legitimate profile update request
2. Identify user ID and parameter structure
3. Store request in Repeater for modification

## Instructions

### Step 1: Configure Browser Proxy

**Context**: Ensure traffic routes through Burp Suite for interception.

Set the browser's proxy settings to point to Burp's listener (default 127.0.0.1:8080) and install the Burp CA certificate if needed for HTTPS.

### Step 2: Log In and Trigger Update

**Context**: Perform an action that generates the target request.

Log in to the attacker account, navigate to profile settings, modify a non-sensitive field like address, and submit the update form.

### Step 3: Intercept and Forward

**Context**: Capture the request in Burp and prepare for editing.

In Burp Proxy > HTTP history, locate the POST to the update endpoint (e.g., /update/ID). Intercept it, inspect, then forward to Repeater.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-capture]]
- [[tools/Burp-Suite]]

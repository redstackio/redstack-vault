---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - proxy
  - interception
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:14.523Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Burp-Proxy-for-Request-Interception

## Summary

This procedure configures Burp Suite as a proxy to intercept and modify HTTP requests to Imgur, enabling payload injection in subsequent steps of the RCE attack.

## Description

In the context of exploiting Imgur's image editor vulnerability, setting up a proxy is essential to capture the /edit/process request generated during image cropping. Burp Suite acts as a man-in-the-middle, allowing real-time editing of parameters like 'y' without disrupting the user workflow. This targets web-based applications and requires no server-side access.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use proxy (e.g., 127.0.0.1:8080)
3. Network access to imgur.com

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or tool signatures in network logs
- Implement client-side certificate pinning to prevent proxy interception

## Objectives

1. Establish interception point for HTTP requests
2. Enable parameter modification for injection
3. Validate proxy setup without errors

## Instructions

### Step 1: Launch and Configure Burp Suite

**Context**: Start Burp and set up the proxy listener to capture browser traffic.

**Command** (No CLI command; GUI setup):

Open Burp Suite, navigate to Proxy > Options, ensure the proxy listener is running on 127.0.0.1:8080.

> This configures Burp to intercept all proxied traffic. Expected output: Proxy status shows 'Running'.

### Step 2: Configure Browser Proxy

**Context**: Route browser requests through Burp for interception.

**Command** (Browser settings):

In your browser (e.g., Firefox), set HTTP proxy to 127.0.0.1 port 8080.

> Test by visiting a site; requests should appear in Burp's Proxy > HTTP history. Expected output: Intercepted requests visible.

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

- proxy-setup
- web-interception

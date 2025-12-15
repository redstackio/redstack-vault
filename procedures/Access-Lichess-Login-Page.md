---
tags:
  - recon
  - web-access
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
updated_at: '2025-12-14T17:26:49.076Z'
sub_techniques: []
id: f5c97760-8e8c-43d2-8361-aad0a4fb446f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Lichess-Login-Page

## Summary

This procedure navigates to the Lichess login page to initiate the attack workflow, ensuring proxy interception is ready for subsequent request capture.

## Description

In the context of testing weak rate limiting on the Lichess login endpoint, accessing the page sets up the environment for capturing legitimate requests. The target is a web application running on Scala with nginx, accessible via HTTPS. Expected outcome is the login form ready for interaction, with no authentication required at this stage.

## Requirements

1. Web browser with Burp Suite proxy configured (e.g., FoxyProxy extension)
2. Network access to https://lichess.org
3. Burp Suite running and listening on default port 8080

## Defense

Defensive measures and detection strategies:

- Monitor for unusual traffic spikes to /login from single IPs
- Implement global rate limiting beyond per-username checks
- Log and alert on proxy-like User-Agent strings

## Objectives

1. Establish initial connection to the login endpoint
2. Verify page accessibility
3. Prepare for request interception

## Instructions

### Step 1: Configure Browser Proxy

**Context**: Route browser traffic through Burp to enable capture.

Set browser proxy to 127.0.0.1:8080 and ensure HTTPS interception is enabled in Burp.

### Step 2: Navigate to Login Page

**Context**: Access the target URL to load the form.

Directly enter https://lichess.org/login in the browser address bar.

> The page should load the login form; if intercepted, forward in Burp Proxy.

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

- recon
- web-access

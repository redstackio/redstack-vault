---
id: proc-002
tags:
  - csrf
  - web
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:30.009Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Intercept-Cancellation-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture and analyze the POST request for canceling a friend request, confirming the absence of CSRF token protection.

## Description

After preparing the cancellation, the attacker intercepts the network traffic to examine the request structure. The XVIDEOS endpoint at https://www.xvideos.com/profiles/USER123/friends/requests/cancel is targeted, revealing no CSRF validation. This step is crucial for vulnerability confirmation in a web-based CSRF attack scenario.

## Requirements

1. Burp Suite Professional installed and configured as browser proxy
2. Authenticated session from previous procedure
3. Target user ID (e.g., USER123)

## Defense

Defensive measures and detection strategies:

- Enforce proxy detection or certificate pinning to block interception tools
- Log all cancellation requests for anomaly detection
- Require CSRF tokens in all POST forms

## Objectives

1. Capture the exact cancellation request
2. Verify missing CSRF protection
3. Document request parameters for POC generation

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept traffic from the browser.

In Burp Suite, ensure the proxy listener is running on 127.0.0.1:8080, and configure your browser to use it. Install Burp's CA certificate if needed.

### Step 2: Trigger and Intercept

**Context**: Perform the cancellation to capture the request.

With the proxy active, click OK on the cancellation popup. The POST request will be intercepted in Burp's Proxy > HTTP history.

### Step 3: Analyze Request

**Context**: Inspect for CSRF vulnerabilities.

Examine the intercepted POST to https://www.xvideos.com/profiles/USER123/friends/requests/cancel. Check headers and body for any CSRF token (e.g., _token field); confirm absence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]

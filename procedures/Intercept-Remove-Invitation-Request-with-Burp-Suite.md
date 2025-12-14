---
tags:
  - intercept
  - burp-suite
  - csrf
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
updated_at: '2025-12-14T17:27:29.857Z'
sub_techniques: []
id: 2b60c6e2-0768-40c4-b0bc-c812b50885b2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Intercept Remove Invitation Request with Burp Suite

## Summary

This procedure uses Burp Suite to capture the HTTP request for removing a team invitation in Infogram, analyzing it for CSRF absence and preparing a malicious URL.

## Description

By proxying traffic through Burp Suite, the remove invitation request (a GET to /api/team/cancel-invitation) is intercepted, revealing no CSRF token. The request is forwarded to Repeater for inspection and dropped to prevent actual execution during testing. This enables crafting a drive-by URL for the attack, targeting authenticated sessions.

## Requirements

1. Burp Suite installed and running
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Authenticated session with pending invitation

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in API endpoints
- Monitor for proxied traffic anomalies
- Use certificate pinning to detect MITM tools like Burp

## Objectives

1. Capture the vulnerable remove request
2. Confirm lack of CSRF protection
3. Extract URL for exploitation

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception for HTTP traffic.

In Burp, enable Intercept in the Proxy tab.

> Ensure the browser routes traffic through Burp's proxy.

### Step 2: Trigger and Intercept Request

**Context**: Perform the remove action to capture it.

Click remove on the invitation; Burp will pause the request.

> Inspect headers/parameters; forward to Repeater, then drop original.

### Step 3: Analyze in Repeater

**Context**: Examine the request details.

Send the intercepted request to Repeater.

> Note the GET URL format: https://infogram.com/api/team/cancel-invitation/{id}?teamId={teamId}&_={timestamp}. No CSRF token present.

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

- intercept
- burp-suite
- csrf

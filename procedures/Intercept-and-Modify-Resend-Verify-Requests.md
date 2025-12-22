---
id: uuid-2
tags:
  - interception
  - enumeration
type: procedure
tools:
  - '[[tools/Intercepting-Proxy]]'
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
updated_at: '2025-12-14T17:33:12.526Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Intercept-and-Modify-Resend-Verify-Requests

## Summary

This procedure uses an intercepting proxy to capture and alter POST requests to the resend-verify endpoint, enabling manual testing for username enumeration based on response differences.

## Description

On the target site, the resend-verify endpoint returns verbose responses that distinguish valid from invalid emails, and triggers emails for valid ones. Intercepting allows modification of the 'email' parameter without browser constraints, bypassing any client-side limits.

## Requirements

1. Installed intercepting proxy like Burp Suite
2. Browser configured to route traffic through proxy (e.g., 127.0.0.1:8080)
3. Active session from prior signup

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and validate referer headers
- Log and rate limit proxy-like traffic patterns
- Use response normalization to avoid info leaks

## Objectives

1. Capture baseline request to the endpoint
2. Modify payloads for targeted enumeration
3. Identify valid accounts via side-channel effects

## Instructions

### Step 1: Configure Proxy

**Context**: Set up the proxy to intercept browser traffic.

Launch [[tools/Intercepting-Proxy]] and configure browser proxy settings.

> Proxy ready when traffic is intercepted.

### Step 2: Capture and Modify Request

**Context**: Trigger and alter the request for testing.

Click resend in browser to intercept the POST to /wp-json/brc/v1/resend-verify. Edit the 'email' parameter (e.g., change to target@example.com) and forward.

**Command** (manual via proxy UI, or replicate with curl):

No bash command; use proxy interface.

> Modified request sent; observe response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Intercepting-Proxy]]

## Tags

- interception
- enumeration

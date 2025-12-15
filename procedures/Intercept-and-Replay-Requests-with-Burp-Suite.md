---
id: 123e4567-e89b-12d3-a456-426614174002
name: Intercept-and-Replay-Requests-with-Burp-Suite
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.938Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - proxy
  - replay
  - web
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Intercept-and-Replay-Requests-with-Burp-Suite

## Summary

This procedure uses Burp Suite as a proxy to capture the 'This Rocks' API request and replay it multiple times rapidly, exploiting the race condition by sending concurrent invocations.

## Description

Burp Suite intercepts HTTP traffic, allowing modification and repetition of requests. In this scenario, after capturing the initial request, the Repeater tool sends it multiple times without synchronization delays, bypassing the one-time limit and confirming the vulnerability. Requires proxy configuration and an authenticated session.

## Requirements

1. Burp Suite installed and running
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Knowledge of the API endpoint from prior recon

## Defense

Defensive measures and detection strategies:

- Enforce idempotency keys in API requests
- Monitor for high-frequency requests from single IPs
- Use web application firewalls to detect replay patterns

## Objectives

1. Capture and analyze a single valid request
2. Replay to test for multiple successes
3. Validate race condition impact on notifications

## Instructions

### Step 1: Configure Proxy and Capture

**Context**: Set up Burp to intercept traffic from the browser.

No command; UI steps:

1. Start Burp Suite and configure proxy listener on port 8080.
2. Set browser proxy to match.
3. Navigate to Social Club, click 'This Rocks' to capture in Proxy > HTTP history.

> Expected output: Captured POST request with full headers and body.

### Step 2: Replay in Repeater

**Context**: Send the request multiple times quickly.

1. Send captured request to Repeater tab.
2. Click 'Send' 5-10 times in rapid succession.

> Expected output: Multiple 200 responses, each acknowledging a 'rock' action.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[proxy]]
- [[replay]]
- [[web]]

---
id: proc-phabricator-csrf-replay-001
name: Replay-Phabricator-CSRF-Token-with-Burp-Suite
tags:
  - csrf
  - token-replay
  - phabricator
  - burp-suite
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
updated_at: '2025-12-14T17:27:03.792Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Replay-Phabricator-CSRF-Token-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and modify a form submission in Phabricator, replacing the current CSRF token with a previously extracted old token to exploit its persistence post-logout.

## Description

After session rotation, the old CSRF token remains valid, allowing replay attacks. Burp Suite acts as a proxy to tamper with requests, enabling submission of forms with the stale token. This targets web forms in Phabricator, leading to unauthorized actions like data manipulation on the user's behalf.

## Requirements

1. Running Burp Suite proxy configured in browser
2. Extracted old CSRF token
3. Active Phabricator session for interception
4. Network access to form endpoints

## Defense

Defensive measures and detection strategies:

- Validate tokens against current session state
- Rate-limit form submissions and monitor proxy-like traffic
- Implement client-side token verification with server-side checks

## Objectives

1. Intercept a legitimate form request
2. Substitute the old CSRF token
3. Achieve successful unauthorized submission

## Instructions

### Step 1: Configure Burp Suite Proxy

**Context**: Set up interception to capture form submissions.

Launch Burp Suite, configure the browser to use its proxy (e.g., 127.0.0.1:8080), and enable Intercept in the Proxy tab.

> Expected output: Traffic routed through Burp; ready for request capture.

### Step 2: Trigger and Intercept Form Submission

**Context**: Perform an action in Phabricator that submits a form while intercepted.

In the new session, navigate to a form (e.g., create a task) and submit it. Burp will pause the request.

> Expected output: Request details visible in Burp, including current CSRF token in body or headers.

### Step 3: Modify and Replay Token

**Context**: Replace the token to test persistence.

In the intercepted request, locate the CSRF token field (e.g., __csrf__) and replace its value with the old extracted token. Forward the request.

> Expected output: Phabricator accepts the request and processes the action, confirming vulnerability (e.g., form succeeds without error).

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

- [[csrf]]
- [[phabricator]]
- [[tools/Burp-Suite]]

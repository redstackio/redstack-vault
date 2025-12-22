---
id: proc-slack-intercept-001
tags:
  - proxy
  - intercept
  - slack
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:47.028Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept-Slack-Signup-Request

## Summary

This procedure uses an intercepting proxy to capture the HTTP POST request to Slack's `api/signup.createUser` endpoint during the workspace invitation signup flow, allowing inspection of authentication parameters like the team ID.

## Description

The Slack signup process sends a POST request to `api/signup.createUser` with details including the team ID from the invitation. By routing traffic through a proxy like Burp Suite, attackers can pause and examine this request before it reaches the server. This is crucial for identifying modifiable parameters in the vulnerability exploitation. Prerequisites include proxy setup on the local machine and starting the signup with a valid invitation. The outcome is a frozen request ready for modification, with no direct impact until forwarded.

## Requirements

1. Intercepting proxy tool installed and running (e.g., Burp Suite)
2. Browser or client configured to use proxy (e.g., 127.0.0.1:8080)
3. Valid Slack invitation to initiate signup

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with certificate pinning to hinder proxy interception
- Monitor for proxy-related traffic anomalies in network logs
- Use client-side integrity checks on requests

## Objectives

1. Capture the signup request payload
2. Identify the team ID parameter location
3. Prepare for parameter tampering

## Instructions

### Step 1: Configure Proxy

**Context**: Set up the proxy to intercept web traffic.

Launch Burp Suite, configure the proxy listener on port 8080, and set your browser to use it as the HTTP proxy.

**Expected Output**: Proxy active and intercepting enabled.

### Step 2: Initiate Signup and Intercept

**Context**: Trigger the request during signup.

Open the Slack invitation link in the proxied browser, proceed to signup, and enter details until the POST to `api/signup.createUser` is sent. The proxy will intercept it.

**Expected Output**: Request body visible, e.g., JSON with `{"team_id": "original_TID", ...}`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[proxy]]
- [[intercept]]
- [[slack]]

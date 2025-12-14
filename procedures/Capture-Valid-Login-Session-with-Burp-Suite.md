---
id: proc-wakatime-capture-session
tags:
  - session-capture
  - auth-recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:43.002Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture Valid Login Session with Burp Suite

## Summary

This procedure uses Burp Suite to intercept and capture session cookies and tokens from a legitimate WakaTime login response, providing the foundation for replay attacks by storing valid authentication data.

## Description

In the context of WakaTime's login mechanism, this step involves proxying traffic to capture the HTTP response from a successful authentication attempt. The response includes a 302 redirect to /dashboard and Set-Cookie headers with session tokens that are not properly invalidated later. This enables attackers to reuse the data for bypassing failed logins. Prerequisites include valid credentials and Burp Suite configured as a proxy (e.g., browser set to 127.0.0.1:8080).

## Requirements

1. Valid WakaTime account credentials (email and password)
2. Burp Suite installed and running with proxy listener enabled
3. Browser configured to route traffic through Burp proxy
4. Direct network access to wakatime.com

## Defense

Defensive measures and detection strategies:

- Implement proper session invalidation on logout and failed attempts
- Use short-lived tokens with timestamps/nonces to prevent replay
- Monitor for anomalous proxy traffic or repeated session usage from invalid contexts

## Objectives

1. Obtain complete valid login response for replay
2. Identify session tokens and cookies for hijacking
3. Set up for auth bypass in subsequent steps

## Instructions

### Step 1: Configure Burp Suite Proxy

**Context**: Set up interception to capture login traffic without disrupting the flow.

Enable Burp's proxy and turn on intercept for responses. No specific command, as this is GUI-based in Burp.

> In Burp, go to Proxy > Intercept tab and ensure "Intercept is on". Configure browser proxy settings to use Burp.

### Step 2: Perform Legitimate Login

**Context**: Submit valid credentials to generate and capture the authentication response.

Navigate to WakaTime login page (https://wakatime.com/login) and enter correct email/password. Intercept the POST /login (or equivalent) response.

> The request body includes JSON or form data with email and password. Response: 302 Found, Location: /dashboard, Set-Cookie: session_token=valid_value; HttpOnly.

### Step 3: Save Captured Response

**Context**: Store the full response for later replay.

Copy the entire HTTP response (status, headers, body) from Burp's Inspector or Repeater tab.

> Expected: Headers include session cookies; body may be empty for redirect. Forward the response to complete login.

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

- session-capture
- auth-recon

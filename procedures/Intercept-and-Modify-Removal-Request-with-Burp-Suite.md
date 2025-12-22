---
id: proc-uuid-2
name: Intercept-and-Modify-Removal-Request-with-Burp-Suite
tags:
  - intercept
  - proxy
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
updated_at: '2025-12-14T17:29:36.543Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Removal-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept a legitimate team user removal request on developers.mtn.com, analyze its parameters, and prepare for modification to exploit IDOR.

## Description

The attack scenario targets the team user removal endpoint, which accepts user_id and team_id parameters without authorization checks. By proxying traffic through Burp Suite, a valid removal (e.g., A removing B from Team A) is captured. The request is forwarded to Repeater for tampering. This applies to web environments with HTTP/HTTPS traffic. Prerequisites include an active Burp proxy setup and authenticated session. Outcomes include visibility into vulnerable parameters and readiness for unauthorized modifications.

## Requirements

1. Installed and running [[tools/Burp-Suite]]
2. Browser configured to use Burp as proxy (e.g., 127.0.0.1:8080)
3. Authenticated session in test accounts

## Defense

Defensive measures and detection strategies:

- Implement client-side certificate pinning to block proxy interception
- Log and alert on anomalous request patterns from proxies
- Use HSTS and secure headers to complicate MITM

## Objectives

1. Capture legitimate removal request structure
2. Identify modifiable parameters (user_id, team_id)
3. Enable manual request replay and alteration

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception of all traffic to the target.

Launch Burp Suite, enable Intercept in the Proxy tab, and configure your browser to route traffic through Burp (e.g., set proxy to 127.0.0.1:8080). Install Burp's CA certificate in the browser.

> Expected: All site requests intercepted; turn off intercept for navigation, enable for actions.

### Step 2: Perform and Intercept Removal

**Context**: Trigger a legitimate removal to capture the request.

Log in to Account A, navigate to Team A, and attempt to remove B. With Intercept on, capture the POST request to the removal endpoint (likely /api/teams/{team_id}/users/{user_id}/remove).

> Expected: Request body or query params showing user_id=1112&team_id=0001.

### Step 3: Forward to Repeater

**Context**: Prepare for modification without losing the original.

In the Intercept tab, forward the request and right-click to send to Repeater. Analyze headers, method (POST), and payload.

> Expected: Repeater loads the exact request for editing.

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

- intercept
- proxy
- burp-suite

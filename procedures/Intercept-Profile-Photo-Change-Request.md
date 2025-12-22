---
tags:
  - interception
  - proxy
  - http-request
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a44028e3-b8d0-4715-920d-2261f9bfa6c6
created_at: '2025-12-14T05:32:13.256Z'
updated_at: '2025-12-14T05:32:13.256Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Profile-Photo-Change-Request

## Summary

This procedure uses a proxy tool to capture HTTP requests during the profile photo change process, enabling modification for vulnerability exploitation.

## Description

After logging in, users navigate to the profile section and attempt to change their photo. Intercepting the request with Burp Suite allows inspection and alteration of parameters before submission to the server at https://auth.ratelimited.me. This is crucial for identifying unvalidated inputs like the 'url' parameter in Gravatar or 'no photo' options. Prerequisites include an active session and Burp Suite configured as the browser proxy.

## Requirements

1. Active authenticated session from prior login
2. Burp Suite installed and running with proxy listener on port 8080
3. Browser proxy settings configured to route through Burp

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS to encrypt traffic and detect proxy interference
- Implement client-side certificate pinning to block proxy tools
- Log and alert on anomalous request patterns or delays indicating interception

## Objectives

1. Capture the photo change request for analysis
2. Identify modifiable parameters like 'url'
3. Enable tampering without direct server interaction

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept traffic from the browser.

Launch Burp Suite and ensure the proxy tab is active with intercept on.

> No command; configure browser to use localhost:8080 as proxy.

### Step 2: Trigger Photo Change

**Context**: Initiate the request to capture it in transit.

Navigate to the profile photo change feature and select an option (e.g., Gravatar).

> The request will pause in Burp's intercept tab, showing parameters for inspection.

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

- [[interception]]
- [[web]]

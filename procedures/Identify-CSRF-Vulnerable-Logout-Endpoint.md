---
tags:
  - csrf
  - recon
  - web
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.032Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f626a195-26ac-4137-b9f4-e1e419864fb1
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-CSRF-Vulnerable-Logout-Endpoint

## Summary

This procedure involves analyzing a web application's logout mechanism to identify CSRF vulnerabilities, specifically checking for GET-based requests without token validation, as seen in WakaTime's implementation.

## Description

In the context of WakaTime, the logout functionality uses a GET request to https://wakatime.com with a 'login' parameter, lacking CSRF protections. This allows cross-origin requests from malicious sites to trigger logout, disrupting user sessions. The procedure requires access to the application and browser tools to inspect requests, confirming the absence of anti-CSRF measures like tokens or same-site cookies.

## Requirements

1. Access to the target web application (e.g., WakaTime)
2. Authenticated session for testing
3. Browser with developer tools (e.g., Chrome DevTools)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens for all state-changing actions, including logout
- Use POST method for logout instead of GET
- Enable SameSite=Strict cookies to prevent cross-site requests
- Monitor for anomalous logout events in logs

## Objectives

1. Confirm the logout endpoint's method and parameters
2. Verify lack of CSRF protections
3. Document the vulnerability for exploitation planning

## Instructions

### Step 1: Inspect Logout Request

**Context**: Log in to the application and trigger a manual logout to capture the request details.

Open browser developer tools (Network tab) and perform logout. Look for the request to https://wakatime.com?login or similar.

> No specific command; use manual browser interaction. Expected output: GET request without CSRF headers or tokens.

### Step 2: Validate CSRF Absence

**Context**: Test if the endpoint accepts cross-origin requests by simulating from another origin.

Use browser console or a simple script to send a cross-origin GET request to the endpoint.

> Expected output: Successful logout without origin checks, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]
- [[tools/Internet-Explorer]]

## Tags

- [[csrf]]
- [[web]]
- [[recon]]

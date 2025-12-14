---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - discovery
  - web
type: procedure
tools: []
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
updated_at: '2025-12-14T17:33:12.228Z'
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
# Discover-Broken-CSRF-Protection-on-account-Endpoint

## Summary

This procedure identifies the lack of Cross-Site Request Forgery (CSRF) protection on the /account endpoint of https://www.niche.co, allowing testers to confirm vulnerability to unauthorized state-changing requests from authenticated users.

## Description

In this attack scenario, a security researcher logs into the target site and tests the /account endpoint for CSRF safeguards. The endpoint handles account modifications like email changes without requiring or validating CSRF tokens, enabling attackers to forge requests using the victim's session. This is typically tested in a controlled environment on web applications with session-based authentication, such as those integrated with Twitter OAuth. Expected outcomes include successful unauthorized modifications, highlighting the need for token-based protections.

## Requirements

1. Active login session on https://www.niche.co via Twitter
2. Access to browser developer tools or a web proxy for request inspection
3. Knowledge of the site's endpoints and authentication flow

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST requests
- Use SameSite cookie attributes to restrict cross-site requests
- Monitor for anomalous account changes via logging and alerts

## Objectives

1. Confirm absence of CSRF validation on /account
2. Document the vulnerability for reporting
3. Assess potential for exploitation in chained attacks

## Instructions

### Step 1: Authenticate and Inspect Endpoint

**Context**: Establish a session and examine the /account endpoint structure.

Log in to https://www.niche.co using Twitter. Open developer tools (F12 in most browsers), navigate to the Network tab, and trigger an account modification action to capture the legitimate POST request to /account. Note the absence of CSRF-related headers or tokens in the request.

### Step 2: Test Without CSRF Token

**Context**: Attempt a modification without protection to verify breakage.

Using the captured request, remove any potential CSRF token or header. Replay the POST request (e.g., via browser console or proxy) to /account with a test change, such as updating a profile field. If the server processes it successfully, CSRF protection is broken.

> Example test payload: POST /account with body {email: "test@example.com"}. Expected output: 200 OK response with updated account confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-vulnerability]]

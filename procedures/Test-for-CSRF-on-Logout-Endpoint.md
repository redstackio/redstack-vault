---
tags:
  - csrf
  - web
  - testing
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-post-logout-test]]'
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 61792b84-cf87-4247-ac1a-dca1154cc398
created_at: '2025-12-14T17:27:42.508Z'
updated_at: '2025-12-14T17:27:42.508Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Test-for-CSRF-on-Logout-Endpoint

## Summary

This procedure tests the /logout endpoint for CSRF protection by attempting POST requests without tokens, confirming if forged requests can invalidate user sessions.

## Description

In web applications, the logout functionality often accepts POST requests to clear sessions. Without CSRF tokens, attackers can forge requests from malicious sites. This procedure involves inspecting the endpoint, sending test requests, and verifying no validation occurs, applicable to any web app like the Enjin platform where /logout lacks protection.

## Requirements

1. Access to the target web application
2. Browser or proxy tool for request inspection
3. Valid session cookie for testing

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Use SameSite cookies to prevent cross-site requests
- Monitor for anomalous logout events from unexpected referers

## Objectives

1. Confirm absence of CSRF protection on /logout
2. Validate that POST requests succeed without tokens
3. Assess potential for remote session disruption

## Instructions

### Step 1: Inspect Logout Endpoint

**Context**: Use developer tools or a proxy to examine the legitimate logout request and check for CSRF token fields.

No command required; manually inspect network tab during normal logout.

> Look for hidden token inputs or headers; absence indicates vulnerability.

### Step 2: Test Forged POST Request

**Context**: Simulate a cross-site POST using curl to verify session invalidation without token.

**Command** ([[commands/curl-post-logout-test]]):
```bash
curl -X POST https://target.com/logout -d '' -b cookies.txt -c cookies.txt
```

> This sends a POST to /logout with an existing session cookie. If the cookie is cleared or session ends without token error, CSRF is missing. Expected output: HTTP 200 or redirect, with session invalidated.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-post-logout-test]]

## Tools Used

- None

## Tags

- [[csrf]]
- [[web-testing]]

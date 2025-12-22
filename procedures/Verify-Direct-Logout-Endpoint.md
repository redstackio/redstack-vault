---
tags:
  - logout
  - endpoint
  - verification
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.482Z'
sub_techniques: []
id: 16b2a2c8-087f-4192-b744-6ff8b279e46a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Direct-Logout-Endpoint

## Summary

This procedure tests the direct accessibility of Weblate's logout endpoint to confirm it lacks CSRF protections, allowing unauthorized session termination via simple HTTP requests.

## Description

From an authenticated session, directly invoking the logout URL demonstrates the vulnerability's root cause: no token validation for cross-origin requests. This step is crucial for validating the exploit path in a web environment using SAML-authenticated sessions. Expected outcome is immediate logout without prompts, highlighting the denial-of-service potential.

## Requirements

1. Active authenticated session from prior login
2. Web browser or HTTP client
3. Access to https://weblate.org

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints like logout
- Log and alert on direct endpoint accesses without referer checks
- Implement same-site cookie policies to mitigate cross-site requests

## Objectives

1. Confirm logout endpoint responds to GET requests
2. Observe session termination behavior
3. Identify absence of protection mechanisms

## Instructions

### Step 1: Access Logout URL

**Context**: While logged in, target the logout endpoint directly to test its functionality.

From the authenticated page (e.g., https://weblate.org/pl/), open a new tab and navigate to https://weblate.org/logout/.

> The browser sends a GET request, terminating the session without confirmation.

### Step 2: Validate Logout Effect

**Context**: Check that the session is indeed ended.

Return to the original tab with https://weblate.org/pl/ and refresh the page.

> The page should redirect to login or show unauthenticated state.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[logout]]
- [[endpoint]]
- [[verification]]
- [[web]]

---
tags:
  - logout-simulation
  - session-reset
  - web-auth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.803Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 843d977d-ff83-4092-956e-6bdd647df85f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Simulate-Unauthenticated-Session

## Summary

This procedure simulates a post-logout or new browser session to verify that authentication is required, highlighting the vulnerability when cookies can still be reused.

## Description

By clearing cookies, logging out, or using incognito mode, this creates an unauthenticated state. Accessing the same admin endpoint should fail or prompt login, but sets up for testing cookie replay. This is crucial for demonstrating broken invalidation in session management.

## Requirements

1. Original browser session
2. Access to browser settings for cookie management
3. Incognito mode capability

## Defense

Defensive measures and detection strategies:

- Enforce session timeouts and invalidation
- Log logout events and monitor session anomalies
- Use one-time tokens or short-lived sessions

## Objectives

1. Establish a clean, unauthenticated context
2. Confirm access denial without valid cookies
3. Prepare for replay testing

## Instructions

### Step 1: Clear Cookies or Logout

**Context**: Remove session artifacts from the browser.

Delete browser cookies for the target domain or explicitly log out via the application's logout function.

**Expected Output**: No active session; user is redirected to login.

### Step 2: Open New Session

**Context**: Use a fresh browser context to avoid residual data.

Open a private/incognito window and navigate to the target site.

### Step 3: Attempt Access to Admin Page

**Context**: Verify unauthenticated state by trying to reach the protected endpoint.

Navigate to https://target.com/admin.101/edit/username; expect a login prompt.

**Expected Output**: Page prompts for credentials or shows access denied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- logout-simulation
- session-reset

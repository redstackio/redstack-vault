---
id: proc-uuid-001
tags:
  - authentication
  - cac
  - dod
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
updated_at: '2025-12-14T17:25:30.017Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-DoD-Application-with-CAC

## Summary

This procedure establishes an authenticated session in the U.S. Department of Defense web application for medical shot records using Common Access Card (CAC) credentials, serving as the entry point for subsequent IDOR exploitation.

## Description

The DoD application requires CAC-based authentication to access user-specific medical records. This step involves navigating to the login endpoint and presenting CAC credentials via a web browser, often integrated with a PIN. Once authenticated, a session is established, allowing access to endpoints that can be proxied for manipulation. Prerequisites include possession of a valid CAC and network access to the DoD domain. Expected outcomes include a successful login without errors, enabling further interactions with the shot records endpoint.

## Requirements

1. Valid CAC card and PIN for a sponsor account
2. Web browser configured for CAC authentication (e.g., with middleware like ActivClient)
3. Network connectivity to the DoD application (e.g., via DoD VPN)
4. Optional: Burp Suite proxy setup to intercept post-authentication traffic

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) beyond CAC and monitor for anomalous login patterns
- Implement session timeout and IP geofencing for DoD network access
- Log all authentication attempts and alert on failed or unusual CAC usages

## Objectives

1. Obtain a valid session token for the authenticated user
2. Verify access to the main application dashboard
3. Prepare for proxy interception of subsequent requests

## Instructions

### Step 1: Configure Browser for CAC

**Context**: Set up the browser to handle CAC authentication by installing necessary middleware and enabling certificate selection.

No specific command; use browser settings to select CAC certificate during login.

> Insert CAC into reader, enter PIN when prompted, and confirm certificate selection.

### Step 2: Navigate to Login Endpoint

**Context**: Access the redacted login endpoint (e.g., https://████/█████) to initiate authentication.

No command; browse to the URL in the configured browser.

> The browser will prompt for CAC/PIN; complete authentication to receive a session cookie and redirect to the dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authentication]]
- [[cac]]
- [[dod]]

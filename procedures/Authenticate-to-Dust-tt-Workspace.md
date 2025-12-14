---
id: proc-dust-auth-001
tags:
  - authentication
  - dust-tt
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:26.910Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Dust-tt-Workspace

## Summary

This procedure establishes an authenticated session as a regular user in a Dust.tt workspace, enabling subsequent API requests for privilege escalation testing.

## Description

In the Dust.tt application, authentication occurs via standard web login, providing session tokens usable in API calls. The workspace ID is extracted post-login for targeting specific environments. This step is prerequisite for exploiting broken access controls, as all attacks require an authenticated context within the same workspace.

## Requirements

1. Valid email and password for a regular user account in the target workspace
2. Web browser or API client with cookie/session handling
3. Network access to https://dust.tt

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for all users
- Monitor login events for anomalous IP locations or times
- Use session rate limiting to prevent brute-force authentication

## Objectives

1. Obtain a valid session token for API authentication
2. Identify and note the workspace ID for endpoint construction
3. Ensure the session has access to the target workspace without admin privileges

## Instructions

### Step 1: Log In to Dust.tt

**Context**: Access the login page and authenticate to create a session.

Navigate to https://dust.tt and enter credentials in the login form. Upon success, the dashboard loads.

> Successful login redirects to the workspace interface; inspect network requests or URL for workspace ID (e.g., /w/mRHt1cXVmK).

### Step 2: Extract Session Token and Workspace ID

**Context**: Capture authentication artifacts for API use.

Use browser developer tools (F12 > Network tab) to inspect a request after login and copy the Authorization Bearer token. Note the workspace ID from the URL or API responses.

> Expected output: Bearer token (e.g., eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...) and workspace ID (e.g., mRHt1cXVmK).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[authentication]]
- [[dust-tt]]

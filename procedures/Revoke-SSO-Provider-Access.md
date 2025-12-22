---
tags:
  - sso
  - revocation
  - access-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 1411d2f7-581b-428e-ae16-3e7e343bcfa0
created_at: '2025-12-13T09:01:26.280Z'
updated_at: '2025-12-13T09:01:26.280Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Revoke SSO Provider Access

## Summary

This procedure outlines the steps to revoke access tokens from an SSO provider like Google or GitHub, simulating a security action that should immediately prevent further logins but may not due to caching issues.

## Description

In this procedure, the attacker or tester revokes authorization from the SSO provider side, such as by logging out or removing the OAuth app. This is typically done to test revocation propagation in integrated systems like AWS Cognito. The expected outcome is immediate denial of access, but vulnerabilities may allow delayed effects.

## Requirements

1. Active SSO account with the provider (Google or GitHub)
2. Access to the provider's account settings page
3. Linked authorization to the target application

## Defense

Defensive measures and detection strategies:

- Implement real-time token validation checks in SSO integrations
- Monitor for repeated login attempts post-revocation

## Objectives

1. Revoke access token effectively
2. Prepare for testing delayed revocation vulnerabilities
3. Confirm revocation on provider side

## Instructions

### Step 1: Access Provider Settings

**Context**: Navigate to the SSO provider's security or app settings to manage authorizations.

Log in to Google or GitHub and go to the authorized apps section.

> For Google: Visit https://myaccount.google.com/permissions; for GitHub: Visit https://github.com/settings/applications.

### Step 2: Revoke Authorization

**Context**: Remove the specific authorization for the target application.

Select the application (e.g., Courier) and choose to revoke or remove access.

> Confirmation message should indicate successful revocation.

### Step 3: Log Out

**Context**: Ensure all sessions are terminated.

Log out from all devices or use the provider's logout functionality.

> This ensures the token is fully invalidated on the provider's end.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[sso]]
- [[revocation]]

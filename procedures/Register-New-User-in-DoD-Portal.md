---
tags:
  - initial-access
  - user-registration
  - salesforce
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:18.154Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 69b5b56f-6b5c-4203-ae16-4eb4201d0534
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Register-New-User-in-DoD-Portal

## Summary

This procedure establishes initial access to the DoD Salesforce portal by registering a new user account and verifying via email, enabling subsequent authenticated requests to exploit misconfigured permissions.

## Description

The DoD tour visitor portal uses Salesforce Community App with Aura Framework. Any visitor can register without restrictions, granting access to query endpoints lacking proper verification. This step creates a valid session for request interception and modification, targeting the public-facing registration endpoint.

## Requirements

1. Internet access to the portal URL (redacted as █████)
2. Valid email address for verification
3. Web browser (e.g., Firefox) with proxy support for Burp Suite

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or additional verification on registration to prevent automated sign-ups
- Monitor for unusual registration spikes from single IPs
- Enforce role-based access controls post-registration to limit query permissions

## Objectives

1. Create a registered user account to obtain session credentials
2. Verify account via email to activate login
3. Establish authenticated session for Aura endpoint access

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the main portal and locate the registration page to begin account creation.

No command required; manually navigate to the target portal URL (redacted as █████) and append the registration path (redacted as ██████████).

> Fill out the form with name, email, and other basic details. Submit to trigger email verification.

### Step 2: Verify Email and Login

**Context**: Confirm the account to enable login and start an authenticated session.

No command required; check email for the verification link, click it, set a password if prompted, and log in.

> Successful login redirects to the portal dashboard, confirming session establishment. Configure browser proxy to Burp Suite for request capture.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- initial-access
- user-registration
- salesforce

---
tags:
  - registration
  - sso-login
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
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
updated_at: '2025-12-14T03:46:37.201Z'
sub_techniques: []
id: fa238dd2-c254-4686-8650-f8fb8d68ab98
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Register-and-Sign-In-to-TopCoder-Platform

## Summary

This procedure outlines the steps to create a new account on TopCoder and sign in using SSO to gain access to the Connect platform, serving as the initial access point for exploiting vulnerabilities like stored XSS in project features.

## Description

The TopCoder platform requires user registration and SSO authentication to access protected areas such as project creation and messaging. This procedure simulates legitimate user onboarding but enables subsequent malicious actions. It targets the web-based interface at topcoder.com and connect.topcoder.com, assuming no prior account. Expected outcome is authenticated access to the dashboard, from which projects can be created.

## Requirements

1. Internet access and a web browser like Chrome
2. A valid email address for registration and SSO verification
3. No existing TopCoder account

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on registrations to prevent abuse
- Monitor for unusual SSO login patterns from new accounts
- Require CAPTCHA on registration forms

## Objectives

1. Establish a foothold on the platform
2. Obtain authenticated session for project interactions
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the main TopCoder site to begin account creation.

In [[tools/Chrome-Browser]], go to https://www.topcoder.com/ and click on the registration or sign-up link.

> Fill in required fields such as email, username, and password. Verify email if prompted.

### Step 2: Sign In with SSO

**Context**: Authenticate to the Connect subdomain using the new credentials.

Navigate to https://connect.topcoder.com/ and sign in using the SSO option with the registered account.

> Successful sign-in redirects to the dashboard, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- registration
- sso-login

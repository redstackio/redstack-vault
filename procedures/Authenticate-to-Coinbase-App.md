---
id: proc-coinbase-auth-001
tags:
  - auth
  - login
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:29.297Z'
sub_techniques:
  - '[[T1078.004]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Coinbase-App

## Summary

This procedure logs into the Coinbase web application to establish an authenticated session, required to access pages with CSRF-protected forms like the API documentation subscription.

## Description

Authentication creates a session with CSRF tokens embedded in forms. In this attack, it positions the attacker to trigger the vulnerable subscription request. Target: Coinbase.com login page. Expected: Valid session cookies and tokens for subsequent navigation.

## Requirements

1. Valid Coinbase account credentials (email/password or 2FA)
2. Browser with proxy configured if intercepting
3. Stable internet connection to coinbase.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on login attempts
- Monitor for unusual login patterns or IP changes
- Enforce multi-factor authentication (MFA) for all sessions

## Objectives

1. Gain authenticated access to protected resources
2. Obtain session-based CSRF token
3. Prepare for form submission in authenticated context

## Instructions

### Step 1: Navigate to Login Page

**Context**: Reach the authentication endpoint.

Open browser and go to https://coinbase.com/signin.

### Step 2: Enter Credentials

**Context**: Submit login details to create session.

Fill in email and password fields, complete any 2FA, and submit the form.

### Step 3: Verify Session

**Context**: Confirm authentication success.

Check for dashboard access or profile elements; inspect dev tools for session cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[T1078.004]] Cloud Accounts

## Commands Used


## Tools Used


## Tags

- [[auth]]
- [[web]]
- [[session]]

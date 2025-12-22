---
id: proc-starbucks-auth
tags:
  - authentication
  - web
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-13T23:52:21.137Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-Starbucks-Account

## Summary

This procedure logs into a Starbucks UK account to establish an authenticated session, necessary for accessing protected endpoints like payment methods where the XSS can be triggered.

## Description

The attack requires an authenticated user context to reach pages like /shop/paymentmethod. Without this, the reflected XSS payload won't execute in a high-privilege area. Use valid credentials to sign in, setting session cookies for subsequent steps.

## Requirements

1. Valid Starbucks UK account email and password.
2. Firefox browser open.
3. Direct access to https://www.starbucks.co.uk.

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) on accounts.
- Monitor login attempts from suspicious IPs.

## Objectives

1. Establish authenticated session.
2. Access account-protected pages.
3. Prepare for payload injection.

## Instructions

### Step 1: Navigate to Sign-In Page

**Context**: Direct the browser to the authentication endpoint.

In Firefox, enter the URL:

```bash
# Manual navigation: https://www.starbucks.co.uk/account/signin
```

> Load the page. Expected output: Sign-in form appears.

### Step 2: Enter Credentials and Submit

**Context**: Provide login details to authenticate.

Fill in email and password fields, then click sign in.

> Expected output: Redirect to account dashboard with session established.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[authentication]]
- [[web]]

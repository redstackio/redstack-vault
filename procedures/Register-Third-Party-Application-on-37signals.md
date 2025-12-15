---
id: proc-37signals-register-app-001
tags:
  - oauth2
  - app-registration
  - 37signals
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:07.309Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Register-Third-Party-Application-on-37signals

## Summary

This procedure outlines registering a malicious third-party application on the 37signals Integration Portal to obtain OAuth2 credentials for subsequent exploitation.

## Description

In the context of CSRF exploitation in 37signals OAuth2, the attacker first creates an application to get a client_id, client_secret, and sets a redirect_uri under their control. This enables the OAuth flow abuse without direct victim interaction beyond session hijacking via CSRF. Prerequisites include access to the portal; no authentication is needed for registration.

## Requirements

1. Internet access to 37signals Integration Portal
2. Valid email for account creation
3. Control over a redirect URI (e.g., attacker-owned domain)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual application registrations from suspicious IPs
- Require CAPTCHA or additional verification for app creation
- Review app scopes and redirect URIs manually

## Objectives

1. Obtain OAuth2 client credentials
2. Configure redirect for code capture
3. Prepare for authorization request

## Instructions

### Step 1: Create Account on Integration Portal

**Context**: Sign up to access app registration features.

Navigate to the 37signals Integration Portal and create an account using a disposable email.

**Expected Output**: Account confirmation email and login access.

### Step 2: Register New Application

**Context**: Set up the app with necessary OAuth parameters.

Log in, go to 'New Application', provide app name, description, and set redirect_uri to attacker-controlled endpoint (e.g., https://evil.com/callback).

**Expected Output**: Client ID and client secret displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth2
- app-registration

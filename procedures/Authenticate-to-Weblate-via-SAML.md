---
tags:
  - authentication
  - saml
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
updated_at: '2025-12-14T17:27:49.494Z'
sub_techniques: []
id: 23f91127-ceb2-4d53-9c28-9de56a9e7eec
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Weblate-via-SAML

## Summary

This procedure outlines the steps to log in to a Weblate instance using SAML authentication, establishing an active session necessary for testing session-based vulnerabilities like CSRF on logout actions.

## Description

Weblate uses SAML for federated authentication, redirecting users through an identity provider. This procedure simulates a legitimate user login to create an authenticated state that can be exploited. The target environment is a web-based translation platform like https://weblate.org, where the absence of CSRF tokens on sensitive actions like logout allows cross-site forgery. Prerequisites include valid credentials; expected outcome is a persistent session cookie enabling access to protected resources.

## Requirements

1. Valid username and password for the SAML-integrated Weblate account
2. Web browser with cookies enabled
3. Direct network access to https://weblate.org and the SAML provider

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to add layers beyond session cookies
- Monitor for unusual login patterns or rapid session terminations
- Use web application firewalls (WAF) to detect anomalous redirects

## Objectives

1. Gain authenticated access to Weblate dashboard
2. Establish session for vulnerability testing
3. Verify SAML flow completes without errors

## Instructions

### Step 1: Navigate to Login

**Context**: Access the Weblate homepage to initiate the authentication flow.

Open a web browser and go to https://weblate.org/pl/ (or the target language/path). Click the top-right login icon (user-tab user-anonymous).

> This redirects to the SAML login page.

### Step 2: Complete SAML Authentication

**Context**: Provide credentials to the identity provider to obtain session tokens.

Follow redirects to https://weblate.org/saml2/login/?next=/pl/, then to https://hosted.weblate.org/accounts/login/?next=/idp/login/process/. Enter username and password on the SAML provider's login form.

> Successful authentication returns to Weblate dashboard with user profile visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[saml]]
- [[web]]

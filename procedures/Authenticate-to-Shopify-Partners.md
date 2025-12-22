---
tags:
  - authentication
  - shopify
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
updated_at: '2025-12-14T03:15:36.265Z'
sub_techniques: []
id: 0ad7bfdf-2f5e-4b24-967e-58d799653411
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Shopify-Partners

## Summary

This procedure outlines logging into the Shopify partners dashboard on app.shopify.com using valid credentials, establishing a session necessary for accessing and exploiting vulnerabilities in authenticated areas.

## Description

In the context of testing or exploiting web vulnerabilities like reflected XSS, authentication is a prerequisite to reach protected pages. This step simulates a legitimate user login but sets up the environment for subsequent payload injection. The target is the Shopify partners platform, where the session enables access to the vulnerable partners services page. Expected outcomes include a valid session cookie, allowing navigation to restricted endpoints without re-authentication.

## Requirements

1. Valid Shopify partner account credentials (email and password)
2. Web browser with JavaScript enabled
3. Network access to https://app.shopify.com (no VPN or proxy restrictions)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential-based access
- Monitor login attempts for anomalies (e.g., unusual IP locations)
- Use session timeouts and cookie security flags (HttpOnly, Secure)

## Objectives

1. Establish an authenticated session on the partners dashboard
2. Verify access to protected pages like /services/partners
3. Prepare for vulnerability exploitation in the logged-in context

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the Shopify app login endpoint to begin authentication.

Navigate to https://app.shopify.com in your web browser.

> The login form will load, prompting for credentials.

### Step 2: Submit Credentials

**Context**: Provide valid partner credentials to authenticate and obtain a session.

Enter your email and password in the form fields, then submit.

> Upon success, you will be redirected to the partners dashboard. Check browser developer tools (F12) for session cookies like '_shopify_s' or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- shopify
- web-login

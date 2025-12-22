---
id: proc-login-vercel
tags:
  - vercel
  - authentication
  - dashboard
type: procedure
tools:
  - '[[tools/Vercel-Dashboard]]'
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
updated_at: '2025-12-14T05:32:31.327Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Vercel-Dashboard

## Summary

This procedure authenticates a user to the Vercel platform using developer credentials, enabling access to domain and project management features necessary for subdomain takeover assessments.

## Description

In the context of subdomain takeover vulnerabilities, logging into Vercel is the initial step to inspect dangling subdomains pointed via CNAME records. The target environment involves web-based access to vercel.com, with outcomes including session establishment for further reconnaissance. Prerequisites include a registered Vercel account; without it, the procedure cannot proceed to claiming checks.

## Requirements

1. Valid Vercel developer account (email and password or OAuth via GitHub/Google)
2. Web browser with JavaScript enabled
3. Internet connectivity to https://vercel.com

## Defense

Defensive measures and detection strategies:

- Monitor Vercel login attempts via audit logs for anomalous IP locations
- Enforce multi-factor authentication (MFA) on Vercel accounts to prevent unauthorized access
- Use browser fingerprinting or device binding to detect session hijacking

## Objectives

1. Establish authenticated session on Vercel dashboard
2. Gain access to domain settings for subdomain verification
3. Prepare for vulnerability scanning without triggering alerts

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the official Vercel authentication endpoint to initiate login.

No command required; manually visit https://vercel.com/login in a web browser.

> Expected output: Login form displayed, prompting for credentials.

### Step 2: Authenticate with Credentials

**Context**: Provide account details to create a session.

Enter email and password, or use OAuth provider. Click 'Continue' or 'Log In'.

> Expected output: Redirect to dashboard with user profile visible; no errors like 'Invalid credentials'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Vercel-Dashboard]]

## Tags

- vercel
- login
- authentication

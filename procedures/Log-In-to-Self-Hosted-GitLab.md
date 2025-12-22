---
id: 123e4567-e89b-12d3-a456-426614174001
name: Log-In-to-Self-Hosted-GitLab
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.882Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - gitlab
  - authentication
commands: []
platforms:
  - Web
tools:
  - '[[tools/GitLab]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Log-In-to-Self-Hosted-GitLab

## Summary

This procedure authenticates a user to a self-hosted GitLab instance with premium access, enabling configuration of integrations like ZenTao for subsequent exploitation steps.

## Description

In the context of exploiting GitLab's ZenTao integration, logging in provides the necessary permissions to create projects and set up malicious integrations. This targets self-hosted instances where premium features are available, allowing access to the web interface without additional tools.

## Requirements

1. Valid username and password for a premium GitLab user account
2. Network access to the self-hosted GitLab server (HTTPS)
3. Browser for web-based login

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) on all accounts
- Monitor login attempts from unusual IPs
- Use role-based access control to limit integration configurations to admins

## Objectives

1. Gain authenticated access to GitLab dashboard
2. Verify premium features availability
3. Prepare for project creation

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the GitLab instance login endpoint to begin authentication.

No command required; use browser to visit https://gitlab.example.com/users/sign_in.

> Enter username and password, then submit the form.

### Step 2: Verify Access

**Context**: Confirm successful login and premium status.

No command; check dashboard for premium indicators like advanced integrations.

> Expected: Redirect to dashboard with user menu showing premium subscription.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitLab]]

## Tags

- [[tools/GitLab]]
- [[authentication]]

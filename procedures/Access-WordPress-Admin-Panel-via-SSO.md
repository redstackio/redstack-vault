---
tags:
  - sso-login
  - admin-access
  - wordpress
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:42.756Z'
sub_techniques: []
id: f3e4fb1e-7c43-40a0-93ca-95a3dfc070ef
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# Access-WordPress-Admin-Panel-via-SSO

## Summary

This procedure uses the verified fake WordPress.com account to log into the target site's admin panel via JetPack SSO, achieving account takeover.

## Description

With email matching enabled, JetPack SSO authenticates based on email correspondence. The now-verified victim's email on WordPress.com matches the local user, granting admin access without passwords or victim interaction. This can lead to full site compromise, e.g., uploading malicious plugins for RCE.

## Requirements

1. Verified WordPress.com account with victim's email
2. Target WordPress site with JetPack SSO and matching enabled
3. Local user with same email

## Defense

Defensive measures and detection strategies:

- Disable email-based SSO matching
- Require additional factors for admin logins
- Log SSO authentications and alert on mismatches

## Objectives

1. Initiate SSO login flow
2. Gain unauthorized admin access
3. Enable post-exploitation

## Instructions

### Step 1: Navigate to Target Login

**Context**: Start the SSO process.

Visit the target site at host.com/wp-login.php.

> SSO button 'Sign in with WordPress.com' is visible.

### Step 2: Authenticate via SSO

**Context**: Use the fake account.

Click the SSO button, log in with the verified victim's WordPress.com credentials.

> Redirected to admin dashboard as the matched user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sso-login
- admin-access
- wordpress

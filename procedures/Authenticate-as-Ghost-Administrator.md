---
tags:
  - authentication
  - ghost-cms
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: f0f94c12-bd66-4345-849e-23a1bb825c0c
created_at: '2025-12-14T04:39:09.667Z'
updated_at: '2025-12-14T04:39:09.667Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-Ghost-Administrator

## Summary

This procedure registers and logs in as the first administrator user in a local Ghost instance, granting publisher role privileges needed to access the vulnerable oEmbed API endpoint.

## Description

In Ghost CMS, the initial user setup during local installation automatically assigns administrator privileges, which include publisher roles (editor, author, etc.). This authentication is required to send requests to protected admin API endpoints like /ghost/api/v3/admin/oembed/. Session cookies from login enable subsequent SSRF exploitation.

## Requirements

1. Running local Ghost instance at http://localhost:2368
2. Web browser for admin portal access
3. No prior credentials; first user is admin

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies for admin accounts
- Monitor admin API access logs for unusual patterns

## Objectives

1. Obtain authenticated session for API calls
2. Simulate publisher role for SSRF exploitation
3. Enable crafted request submission

## Instructions

### Step 1: Access Admin Portal and Register

**Context**: Navigate to the Ghost admin setup to create the initial admin account.

**Instructions**: Open http://localhost:2368/ghost in a browser. Fill in name, email, and password to register. This grants full admin access.

> Expected output: Redirect to dashboard upon successful registration and login.

### Step 2: Capture Session for API Use

**Context**: Extract session cookies for use in API requests.

**Instructions**: Use browser dev tools or proxy to capture the `ghost-admin-api-session` cookie after login.

> Expected output: Valid session token for authenticated requests.

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
- [[ghost-cms]]
- [[initial-access]]

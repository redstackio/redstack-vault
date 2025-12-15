---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - authentication
  - initial-access
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:58.377Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Login-as-Restricted-HackerOne-User

## Summary

This procedure authenticates to the HackerOne platform using credentials for a team member limited to posting internal comments, establishing a baseline restricted session for subsequent exploitation.

## Description

In the context of testing authorization controls, log in to HackerOne with an account tied to a group that only allows 'Post internal comments' permission. This sets up the environment where public posting should be denied, highlighting the bypass in later steps. The target is the web-based HackerOne platform, and success is confirmed by restricted access to report features.

## Requirements

1. Valid HackerOne team member credentials with 'Post internal comments' permission only
2. Web browser or API client with session management
3. Access to a test report (e.g., ID 107329) for verification

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for all accounts
- Monitor login events for unusual IP locations or patterns
- Use role-based access control (RBAC) audits to ensure permissions align with group settings

## Objectives

1. Establish a session with limited privileges
2. Verify restriction on public comment posting
3. Prepare for parameter manipulation testing

## Instructions

### Step 1: Navigate to Login

**Context**: Access the HackerOne authentication endpoint to begin the login process.

No specific command; use browser to visit https://hackerone.com/login and enter credentials.

> Expected output: Redirect to dashboard upon successful authentication.

### Step 2: Verify Permissions

**Context**: Confirm the account's restrictions by attempting a public comment post.

Navigate to a report and try posting a public comment.

> Expected output: Permission denied error for public posting, but internal option available.

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
- [[initial-access]]

---

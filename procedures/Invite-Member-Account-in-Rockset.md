---
tags:
  - account-invitation
  - rockset
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.658Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 0fa1a8c8-8e4a-4d7d-a90d-61b9f81d8696
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-Member-Account-in-Rockset

## Summary

This procedure outlines how an admin user invites a new member account in Rockset's console, setting up a limited-privilege user for testing access control bypasses. It is the initial setup step in demonstrating broken access controls.

## Description

In the Rockset web console, admins can invite users via email with specific roles like 'member', which restricts UI elements such as the billing menu. This procedure creates such an account using a test email, enabling subsequent steps to log in and exploit the vulnerability. The target environment is the Rockset admin dashboard, and the outcome is a functional member account ready for login. Prerequisites include admin credentials and a disposable email address.

## Requirements

1. Valid admin login credentials for https://console.rockset.com/
2. Access to a test email address (e.g., himanshujoshitest2019@gmail.com) that can receive invitations
3. Web browser with no extensions blocking forms

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) audits to monitor invitation patterns
- Use email verification and rate limiting on user invitations to prevent abuse
- Log all admin actions, including user invites, for anomaly detection

## Objectives

1. Create a member account with restricted privileges
2. Simulate a legitimate team member addition
3. Prepare for testing unauthorized access to admin features

## Instructions

### Step 1: Access Admin Dashboard

**Context**: Log in as admin to reach the user management section.

Navigate to https://console.rockset.com/ and authenticate with admin credentials.

> After login, the dashboard should show admin-specific options like user management.

### Step 2: Invite New Member

**Context**: Use the invitation interface to add a member role user.

In the navigation menu, go to 'Organization' or 'Users' settings, then select 'Invite User'. Enter the email address (e.g., himanshujoshitest2019@gmail.com) and assign the 'Member' role. Submit the invitation.

> The system sends an email with a temporary password; check the inbox to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-invitation
- rockset
- setup

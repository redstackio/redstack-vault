---
id: proc-invite-yelp-low-priv-user
tags:
  - invitation
  - user-management
  - yelp
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
updated_at: '2025-12-14T17:30:27.028Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite Low-Privilege User to Yelp Business Account

## Summary

This procedure outlines inviting a low-privilege user to a Yelp business account using the standard invitation feature, granting limited access while explicitly excluding user management capabilities, as a setup for privilege escalation testing.

## Description

In Yelp's business account system, owners can invite additional users to collaborate on account management. However, the system assigns a default low-privilege role that restricts access to sensitive modules like user management. This procedure simulates adding such a user to test for access control flaws. The target environment is the Yelp Business web dashboard, requiring owner credentials. Expected outcomes include the user gaining basic account visibility without elevated permissions, enabling follow-on exploitation.

## Requirements

1. Valid Yelp business account owner login credentials.
2. Access to a web browser with internet connectivity to yelp.com.
3. An email address for the low-privilege user (e.g., a test account).

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) verification on all invitation endpoints to ensure only owners can invite.
- Log all user invitations and monitor for unusual patterns, such as rapid additions from low-reputation IPs.
- Require multi-factor authentication (MFA) for account owners before processing invitations.

## Objectives

1. Add a restricted user to the business account.
2. Confirm the user's limited permissions exclude user management.
3. Prepare for testing unauthorized actions as the invited user.

## Instructions

### Step 1: Log In as Account Owner

**Context**: Access the Yelp Business dashboard to initiate the invitation process.

Navigate to the Yelp Business login page and sign in with owner credentials. Proceed to the account settings or team management section.

### Step 2: Send Invitation

**Context**: Use the built-in invitation tool to add the low-privilege user.

In the user management or team section, click 'Invite User' or similar. Enter the target email, select a standard or viewer role (avoiding admin), and submit. The system sends an invitation email.

### Step 3: Accept Invitation as Low-Privilege User

**Context**: Verify the user's addition with restricted access.

Using a separate browser or incognito mode, log in with the invited user's credentials and accept the invitation via email link. Confirm access to basic features but inability to view or edit user management.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- invitation
- user-management
- yelp

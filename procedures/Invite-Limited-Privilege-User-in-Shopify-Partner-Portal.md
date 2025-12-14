---
tags:
  - shopify
  - user-invitation
  - privilege-setup
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
updated_at: '2025-12-14T17:30:47.378Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c98925b9-8644-4843-8419-a2aab1c70ef8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-Limited-Privilege-User-in-Shopify-Partner-Portal

## Summary

This procedure outlines how to use administrator access in the Shopify Partner Portal to invite a new user with limited privileges, specifically excluding 'View referrals' permission, setting up a test account for authorization bypass testing.

## Description

In the context of testing Shopify's Partner Portal, this step creates a controlled environment with a low-privilege user. The administrator logs in, navigates to account management, and invites a new user without granting referral-related permissions. This simulates an internal attacker or tester preparing to exploit permission mismatches between frontend UI and backend API.

## Requirements

1. Valid administrator credentials for Shopify Partner Portal.
2. Access to email for sending invitations.
3. Web browser with session management capabilities.

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) with audit logs for user invitations.
- Monitor for unusual invitation patterns from admin accounts.
- Require approval workflows for new user creations.

## Objectives

1. Establish a limited-privilege account for testing unauthorized access.
2. Verify that permissions are correctly restricted at invitation time.
3. Prepare for subsequent verification of UI blocks.

## Instructions

### Step 1: Access User Management and Invite User

**Context**: Log in as administrator and initiate the invitation process to create a restricted account.

Navigate to https://partners.shopify.com and log in with admin credentials. Go to the 'Team' or 'Users' section, select 'Invite member', enter details for the new user, and ensure 'View referrals' permission is unchecked. Send the invitation.

> Expected output: Invitation sent successfully; user receives email to complete registration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[user-invitation]]

---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - authorization
  - role-assignment
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:36.739Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Assign-Ad-Manager-Role-to-User

## Summary

This procedure assigns a user the Ad Manager role on a Twitter account, granting permission to create promoted tweets, which sets up the conditions for exploiting an authorization bypass vulnerability.

## Description

In the context of Twitter's Ads & Analytics, account owners can delegate roles to other users. By assigning the Ad Manager role with 'Allow user to create new Promoted-only Tweets' enabled, the assigned user gains limited access intended only for promotional content. This procedure is a prerequisite for bypassing restrictions to post regular tweets. The target environment is the web-based ads.twitter.com interface, requiring administrative access to the target account.

## Requirements

1. Administrative access to the target Twitter account
2. Valid credentials for the account to assign roles
3. Browser access to https://ads.twitter.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access control audits to monitor unusual role assignments
- Require multi-factor approval for role changes in ads accounts
- Log and alert on new user additions to sensitive accounts

## Objectives

1. Grant limited promotional access to a secondary user
2. Prepare for subsequent exploitation of tweet posting restrictions
3. Enable testing of authorization boundaries

## Instructions

### Step 1: Access Account Users Management

**Context**: Log in as the account owner and navigate to the users section to add a new user.

No specific command; use the web interface:

Navigate to `https://ads.twitter.com/accounts/<account_id>/account_users` (replace `<account_id>` with the redacted target ID, e.g., abtest67).

> This loads the page listing current account users.

### Step 2: Add User with Ad Manager Role

**Context**: Enter the secondary user's handle and enable the promoted tweets permission.

Add user (e.g., abtest66) and check 'Allow user to create new Promoted-only Tweets'.

> Successful addition confirms the role assignment, allowing the user to create promoted content only.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authorization
- role-management
- twitter-ads

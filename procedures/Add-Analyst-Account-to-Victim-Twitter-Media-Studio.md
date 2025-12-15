---
tags:
  - access-grant
  - twitter-media-studio
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c222ee03-da10-4b4a-b671-0fbd3fd4aeac
created_at: '2025-12-14T17:25:13.100Z'
updated_at: '2025-12-14T17:25:13.100Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Add-Analyst-Account-to-Victim-Twitter-Media-Studio

## Summary

This procedure grants an Analyst role to an attacker's account on a victim's Twitter Media Studio account, establishing the foundation for subsequent information disclosure by leveraging legitimate access controls.

## Description

In Twitter Media Studio, account owners can add users with specific roles like Analyst, which limits UI access but fails to restrict backend API calls. This step uses the victim's credentials to add the analyst account, simulating a scenario where an insider or compromised account grants access. The target environment is the web-based Twitter Media Studio platform, requiring owner-level credentials. Expected outcomes include successful role assignment, enabling the analyst to switch accounts without triggering immediate alerts.

## Requirements

1. Victim account owner credentials (Account A)
2. Analyst account credentials (Account B)
3. Web browser access to studio.twitter.com
4. No additional tools beyond a standard browser

## Defense

Defensive measures and detection strategies:

- Implement role-based access reviews and audit logs for account additions
- Use multi-factor authentication for account management actions
- Monitor for unusual role assignments via Twitter's audit features

## Objectives

1. Grant Analyst access to victim's account
2. Prepare for account switching without owner privileges
3. Enable API access for disclosure

## Instructions

### Step 1: Log In as Victim and Navigate to Account Management

**Context**: Access the account users management page using victim credentials to add the analyst.

No command required; use browser navigation to https://studio.twitter.com/account_management/YOUR_ACCOUNT_NUMBER/account_users.

> Enter the analyst's username or email, select Analyst role, and confirm addition. Expected output: Success message and updated user list.

### Step 2: Verify Addition

**Context**: Confirm the analyst account is listed with correct role.

Refresh the page and check the user list.

> Expected output: Account B appears with Analyst role permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[access-grant]]
- [[twitter-media-studio]]

---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - wordpress
  - account-creation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:58.328Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Create-WordPress-User-Accounts

## Summary

This procedure sets up attacker and victim user accounts in WordPress with differing privilege levels to enable simulation of the clickjacking attack.

## Description

In a vulnerable WordPress environment (e.g., 4.9.7), create an editor account for the attacker and a lower-privileged author or subscriber account for the victim. This establishes the role-based access needed for embedding unfiltered HTML and targeting profile manipulation. Prerequisites include admin access to create users.

## Requirements

1. Access to WordPress admin dashboard with admin privileges
2. Target WordPress site running on PHP (e.g., port 9080)
3. Browser for manual navigation

## Defense

Defensive measures and detection strategies:

- Restrict user creation to trusted admins
- Monitor for unusual account creations via audit logs
- Implement role-based access controls strictly

## Objectives

1. Establish editor role for HTML embedding
2. Create victim role for targeting
3. Verify account roles and logins

## Instructions

### Step 1: Access User Management

**Context**: Navigate to the users section to add new accounts.

Log in as admin and go to Users > Add New in the dashboard.

### Step 2: Create Editor Account

**Context**: Set up the attacker's privileged account.

Enter username, email, and assign 'Editor' role. Set a strong password and click Add New User.

### Step 3: Create Victim Account

**Context**: Set up the lower-privileged target.

Repeat for victim: assign 'Author' or 'Subscriber' role.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[account-creation]]

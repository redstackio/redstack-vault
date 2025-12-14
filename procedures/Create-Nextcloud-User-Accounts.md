---
tags:
  - nextcloud
  - user-setup
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
techniques: []
updated_at: '2025-12-14T17:24:44.698Z'
sub_techniques: []
id: 29a5c333-5924-4ddf-b1ea-9a015b77266c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Create-Nextcloud-User-Accounts

## Summary

This procedure sets up two user accounts in a Nextcloud instance to simulate an attacker-victim scenario for testing the Talk app vulnerability.

## Description

In the context of exploiting the passcode bypass in Nextcloud Talk Android, creating dedicated user accounts (User A for sending messages via web and User B for the target app) is essential. This requires admin access to the Nextcloud server and ensures isolated testing without affecting production users. The outcome is a configured environment ready for login and vulnerability demonstration.

## Requirements

1. Administrative access to Nextcloud server
2. Nextcloud instance with Talk app enabled
3. Web browser for admin interface

## Defense

Defensive measures and detection strategies:

- Restrict user creation to trusted admins only
- Monitor for unusual account creations in audit logs

## Objectives

1. Establish attacker (User A) and victim (User B) accounts
2. Grant Talk permissions to both
3. Prepare for subsequent login steps

## Instructions

### Step 1: Access Admin Interface

**Context**: Log in as Nextcloud admin to manage users.

Navigate to the Nextcloud web interface, log in with admin credentials, and go to Settings > Users.

### Step 2: Create Users

**Context**: Add new accounts with appropriate permissions.

Click "Add user", create User A with username/password, enable Talk access. Repeat for User B.

**Expected Output**: Users listed in the users panel with active status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[user-creation]]

---
tags:
  - nextcloud
  - group-setup
  - user-creation
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
updated_at: '2025-12-14T17:31:52.300Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 07f164eb-42a7-4118-8429-983a8834ba43
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Nextcloud-Enforcement-Group-and-User

## Summary

This procedure sets up a test group and user in Nextcloud to prepare for 2FA enforcement testing, simulating an environment where 2FA is required for specific users.

## Description

In the context of testing Nextcloud's 2FA bypass vulnerability, this involves logging in as an administrator, creating a new group named 'Enforcement', and adding a test user 'Bypass' with password 'NextCloudEnforcement' to that group. This establishes the prerequisites for enforcing 2FA on the user and demonstrating the session manipulation exploit. The target is a standard Nextcloud instance accessible via web browser.

## Requirements

1. Administrative credentials for Nextcloud
2. Access to the Nextcloud web interface
3. Browser for navigation (e.g., Chrome with dev tools)

## Defense

Defensive measures and detection strategies:

- Monitor admin user actions for unusual group/user creations
- Implement logging for user management changes
- Use role-based access controls to limit group modifications

## Objectives

1. Create a 2FA-enforceable group
2. Assign a test user to the group
3. Prepare for enforcement configuration

## Instructions

### Step 1: Admin Login and Group Creation

**Context**: Authenticate as admin and navigate to user management to create the enforcement group.

Access the Nextcloud login page and authenticate using admin credentials. Click the profile icon in the top-right, go to Users, then Add group with name 'Enforcement'.

### Step 2: User Creation and Assignment

**Context**: Create the test user and assign it to the new group.

From the users section, select New User, enter Username: 'Bypass', Password: 'NextCloudEnforcement', and add to the 'Enforcement' group. Save the user.

**Expected Output**: User 'Bypass' created and visible in the 'Enforcement' group.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- admin-setup

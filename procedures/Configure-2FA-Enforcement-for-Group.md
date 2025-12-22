---
tags:
  - nextcloud
  - 2fa-enforcement
  - configuration
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
updated_at: '2025-12-14T17:31:52.297Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 60634ff2-52e1-4418-aa83-982cc2c17f46
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Configure-2FA-Enforcement-for-Group

## Summary

This procedure configures two-factor authentication enforcement for a specific group in Nextcloud, triggering the requirement for 2FA on assigned users and setting up the conditions for the bypass exploit.

## Description

Using admin access, navigate to security settings to enable group-based 2FA enforcement and add the 'Enforcement' group. This ensures that login attempts with the 'Bypass' user will prompt for 2FA setup, allowing the subsequent cookie manipulation to demonstrate the vulnerability. The process involves UI navigation and saving configurations in a standard Nextcloud admin panel.

## Requirements

1. Admin session active from previous setup
2. 'Enforcement' group and 'Bypass' user already created
3. No existing 2FA on the admin account

## Defense

Defensive measures and detection strategies:

- Audit changes to 2FA settings regularly
- Require approval for security configuration modifications
- Enable alerts for enforcement policy updates

## Objectives

1. Enable group-specific 2FA enforcement
2. Verify enforcement by testing user login
3. Log out to prepare for bypass testing

## Instructions

### Step 1: Navigate to Security Settings

**Context**: Access the administration settings for 2FA configuration.

Click the profile icon, select Settings > Administration > Security > Two-Factor Authentication. Choose enforcement for specific groups.

### Step 2: Add Group and Save

**Context**: Apply enforcement to the 'Enforcement' group and persist changes.

Add 'Enforcement' to the list of enforced groups, then save. Log out of the admin session.

**Expected Output**: Settings saved; subsequent login with 'Bypass' shows 'Two-factor authentication is enforced but has not been configured' message.

### Step 3: Verify Enforcement

**Context**: Test the configuration with the target user.

Attempt login with Username: 'Bypass', Password: 'NextCloudEnforcement' to confirm the prompt.

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
- security-config

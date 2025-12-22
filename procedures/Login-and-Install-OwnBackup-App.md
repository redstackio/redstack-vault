---
id: proc-001
tags:
  - initial-access
  - owncloud
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
updated_at: '2025-12-14T17:23:33.067Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-and-Install-OwnBackup-App

## Summary

This procedure authenticates an administrator to the ownCloud web interface and installs the OwnBackup app, setting the stage for exploiting its backup and restore features.

## Description

In the context of exploiting deserialization vulnerabilities in ownCloud's OwnBackup app, initial access is gained by logging in with admin credentials. The app is then installed from the marketplace to enable the upload, backup, and restore operations that facilitate the attack. This assumes direct network access to the ownCloud instance and valid admin privileges.

## Requirements

1. Valid administrator username and password for ownCloud
2. Web browser access to the ownCloud URL
3. No multi-factor authentication enabled

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin accounts
- Monitor login attempts and app installations via audit logs
- Restrict app marketplace access to trusted administrators

## Objectives

1. Establish authenticated session as administrator
2. Install OwnBackup app without triggering alerts
3. Prepare environment for file uploads

## Instructions

### Step 1: Authenticate to OwnCloud

**Context**: Access the web interface and log in to gain admin privileges.

No specific command; use the browser to navigate to `https://target/owncloud` and enter admin credentials.

> Successful login redirects to the dashboard.

### Step 2: Install OwnBackup App

**Context**: Locate and install the app to enable backup functionality.

No specific command; in the ownCloud UI, go to Apps > Marketplace, search for OwnBackup, and click Install.

> App installation completes, and it appears in the enabled apps list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[owncloud]]

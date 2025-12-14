---
tags:
  - authenticated-access
  - configuration-change
  - concrete-cms
type: procedure
tools: []
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
id: e3de34ac-d8e4-4266-9704-271a6f5aaaaa
created_at: '2025-12-14T17:24:08.473Z'
updated_at: '2025-12-14T17:24:08.473Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-and-Enable-PHP-File-Uploads

## Summary

This procedure authenticates an administrator to the Concrete CMS dashboard and modifies the File Manager settings to allow PHP file uploads, enabling subsequent exploitation of executable file restrictions.

## Description

In Concrete CMS 8.5.2, administrators have unrestricted access to the 'Allow File Types' feature, allowing them to add executable extensions like PHP. This misconfiguration bypasses built-in security filters, permitting the upload of malicious scripts that can be executed on the server. The procedure assumes valid admin credentials and targets the admin dashboard interface.

## Requirements

1. Valid admin credentials for Concrete CMS 8.5.2
2. Web browser access to the CMS login page (e.g., http://target.com/concrete/login)
3. No additional tools required beyond a standard browser

## Defense

Defensive measures and detection strategies:

- Restrict admin privileges to trusted users only; implement role-based access control (RBAC)
- Monitor configuration changes in CMS settings via audit logs; alert on additions to allowed file types
- Disable or harden File Manager to prevent executable uploads, even for admins

## Objectives

1. Authenticate and access admin settings
2. Add PHP as an allowed file type
3. Prepare for payload upload without triggering restrictions

## Instructions

### Step 1: Authenticate to Dashboard

**Context**: Log in using admin credentials to gain access to restricted features.

Navigate to the Concrete CMS login page and enter admin username/password.

> Successful login redirects to the dashboard.

### Step 2: Navigate to File Types Settings

**Context**: Locate the configuration interface for allowed file extensions.

From the dashboard, go to System & Settings > Files > File Types (or similar path in admin menu).

> Interface loads with current allowed types listed.

### Step 3: Add PHP Extension

**Context**: Modify the allowed list to include executables.

Enter 'php' in the add field and save changes.

> Settings update confirms PHP is now permitted; no validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authenticated-access]]
- [[configuration-change]]
- [[concrete-cms]]

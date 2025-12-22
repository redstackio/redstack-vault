---
id: proc-uuid-1
tags:
  - expressionengine
  - admin-access
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.149Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate to ExpressionEngine Admin Profile Settings

## Summary

This procedure accesses the administrative profile settings in ExpressionEngine to reach the avatar configuration, serving as the entry point for exploiting file upload vulnerabilities.

## Description

In ExpressionEngine CMS, administrators can update their profile, including avatars, via the control panel. This step involves logging in and navigating to the specific page where external avatar links can be provided, setting up the scenario for arbitrary file upload without validation. The target environment is a PHP-based web application with admin privileges required.

## Requirements

1. Valid administrative credentials for ExpressionEngine
2. Web browser access to the target host
3. Network connectivity to http://[HOST]/admin.php

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit admin panel exposure
- Monitor admin login attempts and unusual profile updates via audit logs

## Objectives

1. Gain access to avatar settings for exploitation setup
2. Confirm admin privileges are active
3. Prepare for payload delivery

## Instructions

### Step 1: Log In to Admin Panel

**Context**: Authenticate to access protected admin features.

No specific command; use browser to visit http://[HOST]/admin.php and enter credentials.

> Successful login redirects to the control panel dashboard.

### Step 2: Access Profile Settings

**Context**: Navigate to the members profile section to locate avatar options.

No specific command; click on 'Members' > 'Profile' > 'Settings' or directly visit http://[HOST]/admin.php?/cp/members/profile/settings and scroll to 'Change avatar'.

> The form for avatar changes, including 'Link to avatar', is displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy]]

## Tags

- [[expressionengine]]
- [[admin-access]]

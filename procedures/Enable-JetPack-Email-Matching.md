---
tags:
  - wordpress
  - jetpack
  - sso
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - WordPress
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b6bce27b-eb69-4249-9de7-1486b9368c0d
created_at: '2025-12-13T09:01:26.558Z'
updated_at: '2025-12-13T09:01:26.558Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable JetPack Email Matching

## Summary

This procedure configures a WordPress site with JetPack to enable email-based account matching, which is a prerequisite for exploiting SSO authentication bypass.

## Description

By enabling 'Match accounts using email addresses' in JetPack settings, the site allows SSO logins based on email matches without additional verification, setting the stage for unauthorized access via exploited email verification.

## Requirements

1. Access to WordPress admin panel
2. JetPack plugin installed and activated
3. Web browser

## Defense

Defensive measures and detection strategies:

- Regularly audit JetPack settings and disable unnecessary features
- Monitor for unusual user additions or invitations on WordPress.com

## Objectives

1. Enable email matching for SSO
2. Prepare the target site for bypass exploitation
3. Confirm configuration without errors

## Instructions

### Step 1: Access JetPack Settings

**Context**: Navigate to the JetPack configuration in the WordPress dashboard.

Go to plugins > JetPack > settings.

> This opens the JetPack settings page.

### Step 2: Enable Matching Option

**Context**: Turn on the email matching feature.

Locate 'Match accounts using email addresses' and enable it.

> The setting is now active, allowing email-based SSO.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[wordpress]]
- [[jetpack]]

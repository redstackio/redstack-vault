---
id: uuid-2
tags:
  - enable
  - oidc
  - nextcloud
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.341Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable-user_oidc-Module

## Summary

This procedure activates the user_oidc app in Nextcloud, enabling OpenID Connect authentication which is necessary for configuring the malicious discovery endpoint in the XSS attack.

## Description

The user_oidc app integrates Nextcloud with external identity providers using OpenID Connect. Enabling it exposes settings for providers, where the vulnerability lies in how discovery endpoints are processed. This step requires admin access and is performed via the web interface.

## Requirements

1. Running Nextcloud instance with admin credentials
2. Web browser access
3. No prior OIDC configuration

## Defense

Defensive measures and detection strategies:

- Audit app installations in Nextcloud logs
- Disable unused authentication apps
- Monitor for unexpected app activations

## Objectives

1. Activate OIDC support
2. Unlock provider configuration
3. Prepare for payload injection

## Instructions

### Step 1: Access Apps Settings

**Context**: Log in as admin and navigate to the apps management page.

**Instructions**: Go to http://localhost:8081/settings/apps, search for 'user_oidc' in the integration or authentication section.

> Expected: App listed but disabled.

### Step 2: Enable the App

**Context**: Toggle the app to active status.

**Instructions**: Click 'Download and enable' or 'Enable' for user_oidc. Wait for installation and activation.

> Expected output: Confirmation message and app appears in active list. OIDC settings now available under admin authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- enable
- oidc
- nextcloud

---
tags:
  - nextcloud
  - openid-connect
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: cffe43fa-1df5-4577-8a7b-d780dfe1bf64
created_at: '2025-12-13T09:01:26.594Z'
updated_at: '2025-12-13T09:01:26.594Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install and Enable User OIDC App

## Summary

This procedure installs the user_oidc app on a Nextcloud server, enabling the OpenID Connect feature which includes the vulnerable ID4me functionality.

## Description

The user_oidc app provides OpenID Connect integration for Nextcloud, but a flaw allows the ID4me controllers to remain active even when disabled. This setup is a prerequisite for exploiting the vulnerability to create unauthorized accounts.

## Requirements

1. Administrative access to Nextcloud server
2. Nextcloud instance running
3. App store access enabled

## Defense

Defensive measures and detection strategies:

- Regularly audit installed apps and disable unused features completely
- Monitor for unexpected account creations in logs

## Objectives

1. Enable vulnerable ID4me feature
2. Prepare server for exploitation
3. Verify app installation

## Instructions

### Step 1: Install App

**Context**: Access the Nextcloud app store and install user_oidc.

Install via the admin interface or command line if available.

> App installation enables OpenID Connect.

### Step 2: Enable OpenID Connect

**Context**: Activate the feature in settings.

Navigate to settings and enable the app.

> This includes ID4me, which remains vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[nextcloud]]
- [[openid-connect]]

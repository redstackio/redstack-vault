---
tags:
  - setup
  - wordpress
  - jetpack
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:42.774Z'
sub_techniques: []
id: 51148045-ee44-456a-bc36-b8bfa1ed9ded
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Install-and-Configure-JetPack-on-Target-WordPress-Site

## Summary

This procedure installs and configures the JetPack plugin on a self-hosted WordPress site, enabling the SSO feature with email matching that is necessary for the authentication bypass attack.

## Description

The JetPack plugin integrates WordPress sites with WordPress.com services, including SSO. By enabling 'Match accounts using email addresses', the site allows login based on email correspondence between local users and WordPress.com accounts. This setup is a prerequisite for exploiting the verification flaw, as it chains the local user creation with remote account hijacking. The procedure assumes administrative access to the target WordPress instance for simulation or testing purposes.

## Requirements

1. Administrative access to the target WordPress site's dashboard
2. Internet connectivity for plugin download and WordPress.com connection
3. Latest WordPress version (self-hosted)

## Defense

Defensive measures and detection strategies:

- Disable JetPack SSO or email matching if not essential
- Monitor for unusual plugin installations via WordPress logs
- Enforce strict user creation policies requiring email verification

## Objectives

1. Activate JetPack to enable SSO integration
2. Configure email-based account matching
3. Prepare the site for vulnerability chaining

## Instructions

### Step 1: Install JetPack Plugin

**Context**: Download and activate the plugin to establish connectivity.

Log into the WordPress admin at /wp-admin, go to Plugins > Add New, search for "JetPack", install the latest version, and click Activate.

> Upon activation, JetPack prompts for connection to WordPress.com; follow the setup wizard but do not complete full integration yet.

### Step 2: Configure SSO Settings

**Context**: Enable the specific feature that allows email-based matching.

Navigate to JetPack > Settings in the dashboard, scroll to the Sharing or Security section, locate SSO options, and toggle on 'Match accounts using email addresses'. Save changes.

> The setting updates immediately; verify by checking the SSO login button appears on the login page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- wordpress
- jetpack

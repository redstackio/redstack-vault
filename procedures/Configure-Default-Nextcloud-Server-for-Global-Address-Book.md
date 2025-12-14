---
id: proc-nextcloud-config-001
tags:
  - nextcloud
  - configuration
  - privacy-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote System Discovery]]'
updated_at: '2025-12-14T17:24:39.977Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Remote System Discovery]]'
---
# Configure-Default-Nextcloud-Server-for-Global-Address-Book

## Summary

This procedure sets up a standard Nextcloud server instance with default sharing configurations that enable global address book searches, which can lead to privacy leaks when paired with certain clients.

## Description

In a typical attack scenario, an attacker or researcher deploys a clean Nextcloud server to replicate the vulnerability. The default configuration in Nextcloud's admin settings activates 'Search global and public address book for users' without requiring explicit user activation, differing from web and desktop clients. This setup primes the server to query external lookup services when the 'lookup' parameter is absent in incoming requests, as handled in ShareesAPIController.php.

## Requirements

1. Access to a server environment (e.g., Linux VM) with PHP and web server (Apache/Nginx)
2. Download and installation privileges for Nextcloud
3. Administrative access to configure sharing settings

## Defense

Defensive measures and detection strategies:

- Explicitly disable global address book search in Nextcloud admin settings under Sharing
- Monitor server logs for unexpected queries to lookup.nextcloud.com
- Use client-side proxies to inspect iOS app traffic for parameter omissions

## Objectives

1. Replicate default server behavior to enable global lookups
2. Prepare environment for testing client-induced leaks
3. Verify configuration via admin panel

## Instructions

### Step 1: Install and Launch Nextcloud Server

**Context**: Deploy a fresh instance to ensure default settings are applied.

Download and install Nextcloud following official documentation, then access the admin interface at /settings/admin/sharing. Confirm that 'Allow users to share via link' and global address book options are enabled by default.

> No specific command; use web installer or CLI setup script if automated.

### Step 2: Verify Default Configuration

**Context**: Ensure the vulnerability-enabling setting is active.

Navigate to the sharing section in admin settings and note that 'Search global and public address book for users' is toggled on without modification.

> Expected: Setting shows as enabled, no custom config files overriding it.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Remote System Discovery]] Remote System Discovery

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[nextcloud]]
- [[configuration]]
- [[privacy-leak]]

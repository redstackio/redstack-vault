---
tags:
  - misconfiguration
  - nextcloud
  - admin
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8ef0fe9b-d107-48dd-bf93-81a067f3de04
created_at: '2025-12-14T17:23:24.034Z'
updated_at: '2025-12-14T17:23:24.034Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Detect-Nextcloud-Admin-Misconfiguration

## Summary

This procedure checks Nextcloud admin settings for .htaccess validation flaws, particularly on non-HTTPS ports, to identify exploitable misconfigurations.

## Description

Access admin overview at index.php/settings/admin/overview; the security check only runs on port 443, missing port 80 issues where AllowOverride All is absent. Used to confirm RCE/XSS vectors over HTTP.

## Requirements

1. Admin access to Nextcloud settings
2. Web interface on vulnerable instance

## Defense

Defensive measures and detection strategies:

- Manually verify .htaccess on all ports via Apache config
- Use tools like apachectl -t to test config
- Enable comprehensive logging for config changes

## Objectives

1. Identify unchecked HTTP misconfigurations
2. Warn admins of potential exposure
3. Prevent overlooked RCE paths

## Instructions

### Step 1: Access Admin Overview

**Context**: Log in as admin and navigate to settings.

Go to https://www.ournextclouddomain.com/index.php/settings/admin/overview.

> Security warnings display, but only for HTTPS.

### Step 2: Verify Port-Specific Checks

**Context**: Test HTTP access separately.

Access the same page over HTTP (port 80) and note lack of .htaccess warnings.

> Confirms misconfig allowing attacks over unmonitored ports.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[misconfiguration]]
- [[nextcloud]]
- [[admin]]

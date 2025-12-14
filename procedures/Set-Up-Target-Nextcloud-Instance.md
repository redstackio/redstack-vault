---
id: proc-setup-target-instance
tags:
  - nextcloud
  - setup
  - prerequisite
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:24.872Z'
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
# Set-Up-Target-Nextcloud-Instance

## Summary

This preparatory procedure configures a vulnerable Nextcloud instance as the target, ensuring the data directory is web-accessible and federated sharing is enabled.

## Description

The target uses default Nextcloud configuration on Apache where the data dir is inside webroot, allowing potential direct access post-copy. This setup highlights the vulnerability in unpatched instances.

## Requirements

1. Clean Nextcloud installation
2. Apache server with PHP
3. Database setup (MySQL/PostgreSQL)

## Defense

Defensive measures and detection strategies:

- Move data directory outside webroot
- Apply patches for Storage::copyFromStorage
- Use containerized deployments with restricted web access

## Objectives

1. Establish vulnerable target environment
2. Enable federated sharing
3. Confirm data dir configuration

## Instructions

### Step 1: Install Nextcloud

**Context**: Deploy Nextcloud with default settings.

Download and extract Nextcloud, configure Apache virtual host pointing to webroot including data dir.

> Expected output: Instance login page accessible.

### Step 2: Configure Federated Sharing

**Context**: Enable sharing features.

In admin settings, turn on federated cloud sharing.

> Expected output: Sharing options available in UI.

### Step 3: Verify Data Directory

**Context**: Ensure data dir is inside webroot.

Check config/config.php: 'datadirectory' => '/var/www/nextcloud/data/' (within /var/www/html).

> Expected output: Direct HTTP access to /data/ returns 403 (default PHP block).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud-setup

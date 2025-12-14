---
id: proc-disable-nextcloud-blacklist
tags:
  - nextcloud
  - blacklist-bypass
  - modification
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:24.875Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Disable-File-Blacklist-in-Nextcloud

## Summary

This procedure modifies the Nextcloud core filesystem code to disable enforcement of the file blacklist, allowing the creation and upload of restricted files such as .htaccess on an attacker-controlled instance.

## Description

In the attack scenario, an authenticated attacker with admin access to a Nextcloud instance alters the Filesystem.php file to bypass blacklist checks. This is crucial for preparing malicious files that would otherwise be blocked. The target environment is a self-hosted Nextcloud on Apache/PHP, and the outcome enables hosting of permissive .htaccess files for later exploitation.

## Requirements

1. Administrative access to the Nextcloud instance
2. SSH or file system access to the webroot (e.g., /var/www/nextcloud)
3. Basic PHP editing knowledge

## Defense

Defensive measures and detection strategies:

- Monitor core file modifications via file integrity monitoring (e.g., Tripwire or OSSEC)
- Restrict admin access and use read-only deployments for core files
- Regularly audit Nextcloud logs for unauthorized file uploads

## Objectives

1. Disable blacklist to allow blacklisted file creation
2. Prepare instance for malicious payload hosting
3. Enable federated sharing of restricted content

## Instructions

### Step 1: Access and Edit Filesystem.php

**Context**: Locate the core filesystem handling code and comment out or modify the blacklist check to always return true for allowed files.

No specific command; manually edit /lib/private/Filesystem.php around line 616:

```php
// Comment out or modify:
// if (in_array($filename, $blacklist)) { return false; }
// Change to: return true;
```

> Save the file and restart Apache to apply changes. Expected output: No errors on restart, and subsequent uploads of .htaccess succeed.

### Step 2: Verify Blacklist Disable

**Context**: Test by attempting to upload a blacklisted file via the Nextcloud web interface.

Upload a test .htaccess file; it should succeed without rejection.

> Expected output: File appears in file manager without blacklist error messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- blacklist-bypass

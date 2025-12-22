---
id: proc-setup-nextcloud-extract
tags:
  - nextcloud
  - setup
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
updated_at: '2025-12-14T17:24:08.713Z'
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
# Setup-Nextcloud-and-Install-Extract-App

## Summary

This procedure sets up a Nextcloud instance for testing and installs the vulnerable Extract app, providing the foundation for exploiting OS command injection during file extraction.

## Description

In a real-world scenario, target an existing Nextcloud deployment with user authentication. Use a demo instance for replication. The Extract app processes archived files like RAR, but its controller unsafely passes user input to exec() calls. Prerequisites include web access to Nextcloud. Expected outcome: App ready for file upload and extraction.

## Requirements

1. Access to a Nextcloud instance (e.g., https://demo.nextcloud.com)
2. Web browser for interface navigation
3. Authenticated user account

## Defense

Defensive measures and detection strategies:

- Disable unnecessary apps like Extract or use sandboxed extraction
- Monitor app installations via audit logs
- Enforce principle of least privilege for user accounts

## Objectives

1. Gain authenticated access to Nextcloud
2. Enable the Extract app for RAR processing
3. Prepare environment for vulnerability exploitation

## Instructions

### Step 1: Access and Log In to Nextcloud

**Context**: Create or log in to a user account to establish initial access.

No command required; use web interface.

> Navigate to https://demo.nextcloud.com, sign up or log in. Expected output: Dashboard loads.

### Step 2: Install Extract App

**Context**: Add the vulnerable app to enable RAR extraction functionality.

No command required; use web interface.

> Go to Apps > Search 'Extract' > Install. Expected output: App enabled, visible in file actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- setup

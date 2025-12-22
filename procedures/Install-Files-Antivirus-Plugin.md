---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - plugin-installation
  - setup
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Windows Service]]'
updated_at: '2025-12-14T17:23:32.370Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Windows Service]]'
---
# Install-Files-Antivirus-Plugin

## Summary

This procedure installs the vulnerable files_antivirus plugin in ownCloud, enabling the configuration interface that lacks input validation for the antivirus binary path.

## Description

The files_antivirus plugin integrates ClamAV scanning into ownCloud's file upload process. In version 10.4.1.3, its configuration allows admins to set the AV binary path without sanitization, which is exploited for RCE. Installation is done via the ownCloud marketplace, requiring admin access. This step is prerequisite for accessing Protection settings.

## Requirements

1. Admin access to ownCloud interface
2. Internet connectivity for marketplace download (or manual upload from https://github.com/owncloud/files_antivirus)
3. Plugin compatibility with ownCloud 10.4.1.3

## Defense

Defensive measures and detection strategies:

- Disable or review third-party plugins before installation
- Log plugin installations and monitor for unauthorized changes
- Use app whitelisting to restrict marketplace access

## Objectives

1. Enable the files_antivirus plugin
2. Unlock Protection settings for AV configuration
3. Set up for path misconfiguration exploitation

## Instructions

### Step 1: Navigate to Apps Section

**Context**: Access the plugin marketplace from the admin dashboard.

Click on the Apps icon in the top menu and search for "files_antivirus".

> The plugin page loads with download option. Expected output: List of available apps including files_antivirus.

### Step 2: Download and Install

**Context**: Install the plugin to activate its features.

Click "Download and enable" from the marketplace, or manually upload if offline.

> Installation completes; plugin status changes to enabled. Refresh the page if needed to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Windows Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- plugin-installation
- setup

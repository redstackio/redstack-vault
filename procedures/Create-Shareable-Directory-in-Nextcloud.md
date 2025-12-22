---
tags:
  - android
  - nextcloud
  - sharing
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:42.804Z'
sub_techniques: []
id: 290540bc-2d15-429c-b9f4-a7bfb9de37dc
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Create-Shareable-Directory-in-Nextcloud

## Summary

This procedure creates a directory in the Nextcloud Android app and enables sharing, allowing uploaded files to be publicly accessible for exfiltration.

## Description

Within the authenticated Nextcloud app, users can create folders and toggle sharing to generate public links. This sets up the upload target for leaked private files, amplifying impact by making them remotely accessible.

## Requirements

1. Authenticated Nextcloud app session
2. Permissions to create and share folders (default for logged-in users)
3. Stable connection to Nextcloud server

## Defense

Defensive measures and detection strategies:

- Review share logs for unexpected public links
- Limit sharing permissions via admin policies
- Audit directory creations for anomalies

## Objectives

1. Establish a public upload destination
2. Enable file sharing without additional auth
3. Facilitate exfiltration of leaked content

## Instructions

### Step 1: Navigate to File Browser

**Context**: Access the main file management interface.

Open the app and go to the root or desired parent directory.

### Step 2: Create and Share Directory

**Context**: Set up the exploitable folder.

Tap '+', select 'New folder', name it (e.g., 'shared'), then tap the share icon and enable public link.

**Expected Output**: Folder appears with active share status.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sharing]]
- [[directory]]

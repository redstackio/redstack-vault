---
tags:
  - nextcloud
  - file-sharing
  - create-share
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
techniques: []
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 989d458e-78b4-41c6-b03e-5f8f1b65e3d4
created_at: '2025-12-14T17:29:09.989Z'
updated_at: '2025-12-14T17:29:09.989Z'
verified: false
validated: true
submitted: true
---
# Create-File-Share-in-Nextcloud

## Summary

This procedure creates a share link for a file in Nextcloud, setting up the environment for testing expiration date modifications and associated logging.

## Description

To demonstrate logging issues, a file share must first be established using Nextcloud's sharing interface. This involves selecting a file and generating a share (public or internal), which should trigger an audit log entry. The procedure assumes user-level access and focuses on UI interactions in a web-based Nextcloud deployment.

## Requirements

1. Valid user account in Nextcloud with file upload/share permissions
2. A test file uploaded to the user's personal storage
3. Browser access to the Nextcloud file manager

## Defense

Defensive measures and detection strategies:

- Monitor share creation events in audit logs
- Restrict sharing permissions to trusted users
- Review share links periodically for unauthorized access

## Objectives

1. Generate a share link for a specific file
2. Ensure the share is created without expiration initially
3. Confirm share visibility in the UI for further modifications

## Instructions

### Step 1: Select and Share File

**Context**: Navigate to the file and initiate sharing to create the baseline share.

No command required; use the web UI:

- Open the Files app
- Select a test file
- Click the Share icon and choose share type (e.g., Public link)
- Generate the share without setting expiration

> The share link is created, and details appear in the sharing panel; this action should log properly.

### Step 2: Verify Share Creation

**Context**: Confirm the share is active and ready for expiration testing.

No command required; use the web UI:

- Check the share settings panel
- Note the share ID or link for reference

> Success is indicated by the share being listed and accessible.

## MITRE ATT&CK Mapping

### Tactics

- None

### Techniques

- None

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[nextcloud]]
- [[file-sharing]]

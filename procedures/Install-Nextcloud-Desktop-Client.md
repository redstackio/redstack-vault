---
tags:
  - installation
  - desktop-client
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Desktop
  - Windows 10
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:15:53.553Z'
sub_techniques: []
id: 5a599220-ebaa-4444-a190-3203a00fc454
validated: true
---
# Install-Nextcloud-Desktop-Client

## Summary

This procedure installs the Nextcloud Desktop Client on a Windows 10 machine and authenticates a regular user, enabling integration with Nextcloud Talk for vulnerability exploitation.

## Description

The Nextcloud Desktop Client provides synchronization and notification features, including call popups from Talk. Installation involves downloading the official client and logging in, which exposes the client to unsanitized content from the server. This step is crucial for observing XSS in the local application context. The target is a Windows 10 environment with network access to the server. Expected outcomes include a connected client ready for Talk notifications.

## Requirements

1. Windows 10 machine with internet access
2. Regular user credentials from the server
3. Download access to nextcloud.com

## Defense

Defensive measures and detection strategies:

- Verify desktop client downloads with checksums to avoid modified versions
- Monitor client logs for unusual authentication attempts
- Use endpoint protection to scan installations

## Objectives

1. Deploy the desktop client software
2. Authenticate and connect to the Nextcloud server
3. Enable Talk notifications in the client

## Instructions

### Step 1: Download and Install Client

**Context**: Obtain and set up the desktop application on the target machine.

Visit nextcloud.com/install, download the Windows installer, run it, and follow the setup prompts.

> Installation completes with the client app launching.

### Step 2: Log In as Regular User

**Context**: Connect the client to the server using victim credentials.

Open the client, enter server URL, username, and password to authenticate.

> Client shows connected status and begins syncing files.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[installation]]
- [[desktop-client]]

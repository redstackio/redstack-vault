---
tags:
  - client-auth
  - nextcloud
  - session
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:39.355Z'
sub_techniques: []
id: a9cf6ecd-5c3c-46b8-97f6-3b4a3e392be1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Establish-Sessions-in-Desktop-and-Android-Clients

## Summary

This procedure creates active sessions in Nextcloud desktop and Android clients using standard credentials, simulating multi-device access for testing revocation effectiveness.

## Description

After browser login, this step authenticates the desktop and Android clients with the same admin username and password (avoiding app-specific passwords). This results in three concurrent sessions, allowing observation of how revocation impacts non-web clients. The technical approach relies on clients storing credentials locally, which enables persistence. Prerequisites include installed clients configured to point to the Nextcloud server.

## Requirements

1. Nextcloud desktop client installed and configured
2. Nextcloud Android app installed on a device
3. Admin credentials (username and password)
4. Network connectivity to the Nextcloud server

## Defense

Defensive measures and detection strategies:

- Implement token-based authentication with short expiration for clients
- Log and alert on multiple simultaneous logins from different devices

## Objectives

1. Create persistent client sessions
2. Verify multi-device syncing capability
3. Set up conditions for revocation testing

## Instructions

### Step 1: Authenticate Desktop Client

**Context**: Launch and connect the desktop client to establish a session.

Open the Nextcloud desktop client, enter the server URL, admin username, and password, then connect.

### Step 2: Authenticate Android Client

**Context**: Connect the mobile app to create an additional session.

Launch the Nextcloud Android app, input the server details and credentials, and authenticate.

> Both clients should now sync files, confirming active sessions alongside the browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[client-auth]]
- [[nextcloud]]
- [[session]]

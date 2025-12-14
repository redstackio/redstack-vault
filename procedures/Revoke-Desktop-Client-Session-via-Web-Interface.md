---
tags:
  - revocation
  - session-management
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:39.349Z'
sub_techniques: []
id: bd52319b-4db7-41f6-9e10-7ce62658df34
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Revoke-Desktop-Client-Session-via-Web-Interface

## Summary

This procedure attempts to terminate a desktop client session using the Nextcloud web UI's sessions management feature, highlighting the limitation where only PHP sessions are affected.

## Description

Navigating to the Personal > Sessions tab in the web interface allows selection and revocation of listed client sessions. However, in Nextcloud 10.0, this only invalidates the server-side PHP session without notifying or terminating client-side tokens, leading to re-authentication via stored credentials. This step is crucial for demonstrating the bypass in subsequent verification.

## Requirements

1. Active browser session as admin
2. Desktop client session visible in the sessions list
3. Access to User > Personal > Sessions page

## Defense

Defensive measures and detection strategies:

- Ensure revocation propagates to all client types via token invalidation
- Audit session logs for failed revocations or re-authentications

## Objectives

1. Simulate user-initiated session cleanup
2. Trigger the revocation mechanism
3. Observe partial effectiveness on web side

## Instructions

### Step 1: Navigate to Sessions Page

**Context**: Access the session management interface.

In the browser dashboard, go to your user profile > Personal > Sessions.

### Step 2: Select and Revoke

**Context**: Target the desktop client entry for termination.

Locate the desktop client session in the list, select it, and confirm the kill/revoke action.

> The UI should update to show the session as revoked, but no client-side impact occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[revocation]]
- [[session-management]]
- [[nextcloud]]

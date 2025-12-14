---
tags:
  - bypass
  - persistence
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
updated_at: '2025-12-14T17:24:39.335Z'
sub_techniques: []
id: a0f5859c-c776-4347-bca8-b45186fb52a9
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Continued-Access-in-Desktop-Client

## Summary

This procedure tests whether the desktop client session persists after web-based revocation by uploading a file and observing automatic syncing without re-authentication.

## Description

Post-revocation, the desktop client uses stored credentials to re-authenticate on its next sync request, bypassing the intended termination. This violates secure design by not fully invalidating client tokens. The test involves a simple file upload via web to trigger client activity, confirming unauthorized continued access.

## Requirements

1. Revoked desktop session (from prior step)
2. Active desktop client monitoring folder
3. Ability to upload files via web interface

## Defense

Defensive measures and detection strategies:

- Require re-authentication for all client actions after revocation
- Implement client-side token revocation notifications

## Objectives

1. Prove session invalidation failure
2. Demonstrate potential for unauthorized data access
3. Validate impact on file syncing

## Instructions

### Step 1: Upload Test File

**Context**: Create a change on the server to trigger client sync.

In the web interface, navigate to Files and upload a new test file.

### Step 2: Monitor Client Sync

**Context**: Observe if the client pulls the file without prompts.

Check the desktop client's synced directory for the new file appearance.

> The file syncs automatically, indicating the session remains functional via stored credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bypass]]
- [[Persistence]]
- [[nextcloud]]

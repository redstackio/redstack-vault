---
tags:
  - nextcloud
  - android
  - download
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:39.419Z'
sub_techniques: []
id: 5e44d427-00fb-477d-a137-60a71cf4c8f3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Download Media Files Using Nextcloud Android App

## Summary

This procedure involves using the Nextcloud Android app to download media files from the server, which are automatically stored in a shared external storage folder, exposing them to unauthorized access by other apps.

## Description

In the Nextcloud Android app on Android Oreo, media files selected for offline access are saved to /sdcard/Android/media/com.nextcloud.client/nextcloud/ACCOUNT/ without encryption or restrictions. This design choice prioritizes compatibility with external apps (e.g., media players) but creates a vulnerability where files become readable and writable by any app with storage permissions. The procedure sets up the exposure for subsequent access and modification attacks.

## Requirements

1. Nextcloud Android app installed and authenticated with a valid account.
2. Android device running Oreo or compatible version with external storage enabled.
3. Internet connectivity to access the Nextcloud server.
4. Media files available in the user's Nextcloud folders.

## Defense

Defensive measures and detection strategies:

- Enable app-specific storage isolation in Android settings (post-Oreo scoped storage helps, but not retroactive).
- Use Nextcloud app versions with fixed storage behavior (e.g., private directories).
- Monitor device for unauthorized apps with storage permissions via app permission reviews.
- Implement server-side file integrity checks (e.g., hashes) to detect corrupted uploads.

## Objectives

1. Expose sensitive media files in shared storage for third-party access.
2. Enable offline availability that inadvertently allows tampering.
3. Set the stage for confidentiality and integrity compromises.

## Instructions

### Step 1: Initiate Download

**Context**: Launch the app and select files to download, triggering storage in the shared folder.

No specific command; perform via app UI:

- Open Nextcloud app.
- Navigate to a folder with media (e.g., images or videos).
- Tap the download/offline icon on files.

> The app saves files to /sdcard/Android/media/com.nextcloud.client/nextcloud/ACCOUNT/. Verify by checking the folder with a file explorer.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[android]]
- [[download]]

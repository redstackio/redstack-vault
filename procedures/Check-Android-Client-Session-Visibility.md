---
tags:
  - visibility-gap
  - android
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:39.322Z'
sub_techniques: []
id: 90ed23c5-51e1-4e5a-bf7c-fbea7c34d41a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Check-Android-Client-Session-Visibility

## Summary

This procedure verifies that an active Android client session is not displayed or tracked in the web sessions tab, exposing a monitoring gap in Nextcloud 10.0.

## Description

Despite the Android client being fully functional and syncing data, its session does not appear in the Personal > Sessions list. This root cause stems from incomplete session tracking for mobile clients, allowing hidden persistence. The procedure involves basic interaction with the app and refreshing the web list to confirm absence.

## Requirements

1. Active Android client session
2. Access to web sessions page
3. Android device with Nextcloud app

## Defense

Defensive measures and detection strategies:

- Enhance session tracking to include all client types, including mobile
- Cross-reference server logs with client activities for unlisted sessions

## Objectives

1. Identify tracking deficiencies
2. Confirm Android access persistence
3. Highlight risks of unmonitored sessions

## Instructions

### Step 1: Interact with Android Client

**Context**: Ensure the client is active to simulate usage.

Perform a sync or file access action in the Android app.

### Step 2: Refresh Web Sessions List

**Context**: Check for visibility of the mobile session.

Return to the browser's Personal > Sessions tab and refresh.

> The Android session remains unlisted, while functionality persists.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[visibility-gap]]
- [[android]]
- [[nextcloud]]

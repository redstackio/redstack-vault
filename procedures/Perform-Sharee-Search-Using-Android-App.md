---
tags:
  - android
  - search
  - api-request
type: procedure
tools: []
tactics:
  - '[[Exfiltration]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
updated_at: '2025-12-14T17:24:45.120Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 848a4d35-db1f-4fa7-93b1-a44a4f5d9e2c
validated: true
mitre_tactics:
  - '[[Exfiltration]]'
mitre_techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
---
# Perform-Sharee-Search-Using-Android-App

## Summary

This procedure demonstrates how to use the Nextcloud Android client to perform a sharee search, which triggers an API request lacking the 'lookup' parameter, leading to unintended global search activation on the server.

## Description

The Nextcloud Android app handles sharing by querying the server for potential sharees. Due to a flaw, it does not include the 'lookup' parameter in the request, causing the server to default to querying the external lookup server. This step simulates a user attempting to share content, highlighting the privacy issue as searches are leaked without consent, differing from web and desktop clients that require explicit activation.

## Requirements

1. Installed Nextcloud Android app (latest version)
2. Connected to the target Nextcloud server
3. A file or folder in the app to share
4. Android device with network access

## Defense

Defensive measures and detection strategies:

- Update to patched Nextcloud Android client if available
- Educate users on sharing risks and disable global search
- Log and alert on API requests missing parameters

## Objectives

1. Initiate a sharee search in the app
2. Generate an incomplete API request
3. Observe app behavior without error

## Instructions

### Step 1: Navigate to Sharing

**Context**: Select content to share within the app.

Open the Nextcloud Android app, browse to a file or folder, and tap the share icon to open the share dialog.

### Step 2: Enter Search Term

**Context**: Trigger the lookup without global intent.

In the sharee search field, type a term (e.g., a username or email). The app sends the request to /ocs/v2.php/apps/files_sharing/api/v1/sharees without the 'lookup=false' parameter.

### Step 3: Review Results

**Context**: Confirm the search completes.

The app displays potential matches, but the server has already performed a global query.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration]] Exfiltration

### Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol]] Exfiltration Over Unencrypted Non-C2 Protocol

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[search]]
- [[api-request]]

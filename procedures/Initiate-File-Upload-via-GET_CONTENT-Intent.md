---
tags:
  - android
  - intent
  - upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:42.797Z'
sub_techniques: []
id: 70cf6af8-3989-4f42-a223-88e8b0388b00
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Initiate-File-Upload-via-GET_CONTENT-Intent

## Summary

This procedure triggers the Nextcloud app's upload from other apps feature, broadcasting a GET_CONTENT intent that can be intercepted by the malicious app.

## Description

The vulnerability stems from the app's failure to validate returned URIs, allowing external apps to provide access to private /data/data/ paths. This step relies on user interaction in the shareable directory to launch the chooser.

## Requirements

1. Authenticated Nextcloud app with shareable directory
2. Malicious app installed
3. User-level access to app UI

## Defense

Defensive measures and detection strategies:

- Validate all returned URIs to restrict to external storage
- Log intent resolutions for anomalies
- Educate users on app selection in choosers

## Objectives

1. Launch intent chooser for content selection
2. Expose opportunity for malicious response
3. Prepare for URI-based file access

## Instructions

### Step 1: Navigate to Shareable Directory

**Context**: Position for upload action.

Open Nextcloud app and enter the previously created shareable folder.

### Step 2: Trigger Upload Intent

**Context**: Initiate the vulnerable feature.

Tap '+' > 'Upload content from other apps' to start the GET_CONTENT intent.

**Expected Output**: Chooser dialog with app list.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (adapted for Android intents)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[get-content]]
- [[chooser]]

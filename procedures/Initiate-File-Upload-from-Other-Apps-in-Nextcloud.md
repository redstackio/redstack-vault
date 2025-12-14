---
id: uuid-proc-4
tags:
  - upload
  - intent
  - android
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:41.956Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Initiate File Upload from Other Apps in Nextcloud

## Summary

This procedure triggers the Nextcloud app's file upload intent to select content from external apps, setting up the exploitation vector.

## Description

The upload feature uses Android intents to pick files, which can be hijacked by malicious providers to supply invalid paths.

## Requirements

1. Installed and logged-in Nextcloud app
2. Shareable folder created
3. POC app installed

## Defense

Defensive measures and detection strategies:

- Validate all incoming URIs in FileUploader.java for full path patterns
- Log intent invocations for upload attempts
- Restrict external app integrations

## Objectives

1. Open file picker for external selection
2. Expose intent resolver to POC app
3. Prepare for URI-based file provision

## Instructions

### Step 1: Navigate to Shareable Folder

**Context**: Position app for upload.

Open Nextcloud > Go to shareable folder.

**Expected Output**: Folder contents displayed.

### Step 2: Trigger Upload Intent

**Context**: Initiate external file selection.

Tap '+' > "Upload content from other apps".

**Expected Output**: App chooser dialog opens.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-picker]]
- [[intent-trigger]]

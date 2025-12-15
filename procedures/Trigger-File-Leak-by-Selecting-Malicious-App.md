---
tags:
  - android
  - file-leak
  - exfiltration
type: procedure
tools:
  - '[[tools/setresultcontactphotocrop]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:42.790Z'
sub_techniques: []
id: 3bbb6abd-f357-44ea-a5c3-f715b73bc3f7
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Trigger-File-Leak-by-Selecting-Malicious-App

## Summary

This procedure completes the exploit by selecting the malicious app in the intent chooser, causing it to return a private file URI that Nextcloud uploads publicly.

## Description

Upon selection, the EvilActivity sets the intent result to a private URI, which the Nextcloud app reads without validation, uploading contents like preferences.xml (account details, tokens), databases, keys, cookies, and temp files to the shareable directory for public access.

## Requirements

1. Active intent chooser from upload initiation
2. Installed malicious POC app
3. Shareable directory ready

## Defense

Defensive measures and detection strategies:

- Implement URI scheme validation (e.g., block file:// to /data/data/)
- Monitor uploads for private path origins
- Patch app to sanitize intent results

## Objectives

1. Return unauthorized private file URI
2. Upload sensitive data to cloud
3. Achieve public exfiltration

## Instructions

### Step 1: Select Malicious App

**Context**: Intercept the intent.

In the chooser, pick 'setresultcontactphotocrop'.

### Step 2: Confirm Upload and Share

**Context**: Observe leakage.

The app processes the URI, uploads the file, and enables sharing. Access the public link to verify leaked content.

**Expected Output**: Sensitive file in directory, e.g., XML with auth tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/setresultcontactphotocrop]]

## Tags

- [[leak]]
- [[uri]]

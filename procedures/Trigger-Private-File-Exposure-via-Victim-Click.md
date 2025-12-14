---
tags:
  - file-exposure
  - data-leakage
  - local-exfil
type: procedure
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
updated_at: '2025-12-14T17:26:27.178Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: c9928f65-92f8-48a3-8247-3fbaf947f736
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Trigger Private File Exposure via Victim Click

## Summary

This procedure simulates or observes the victim interacting with the malicious deeplink, causing the Basecamp app to save private content to a public directory for unauthorized access.

## Description

Upon clicking, the app's deeplink handler processes the URL, extracts the private file (e.g., progress report), and saves it using the traversed 'filename' path to /sdcard/Download/. This exposes sensitive data to any app with external storage read permissions, such as file managers or malware, without requiring additional privileges. The attack completes with one click, highlighting the risk of unsanitized local file operations in mobile apps.

## Requirements

1. Victim device with Basecamp app and deeplink enabled
2. Shared malicious link from previous step
3. Third-party app on device with READ_EXTERNAL_STORAGE permission

## Defense

Defensive measures and detection strategies:

- Enforce path canonicalization and sandboxing for file writes
- Audit app permissions and revoke broad storage access
- Monitor device for anomalous file creations in shared directories

## Objectives

1. Invoke app's file save intent via deeplink
2. Confirm write to public path
3. Verify exposure to external apps

## Instructions

### Step 1: Simulate Victim Interaction

**Context**: Click the link in Basecamp to trigger processing.

Tap the hyperlinked URL in the app interface.

> Expected: App launches deeplink handler and prompts file save.

### Step 2: Validate Exposure

**Context**: Check for file in target directory and read access.

Use a file explorer to locate /sdcard/Download/disclosure.txt and open with another app.

> Expected: Private content (e.g., report text) readable externally.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-exposure]]
- [[data-leakage]]
- [[local-exfil]]

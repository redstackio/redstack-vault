---
tags:
  - android
  - data-exfiltration
  - broadcast-interception
type: procedure
tools: []
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
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:24:42.242Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b1663493-a76f-48f0-b139-d1f5334861fc
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Automated Collection]]'
---
# Intercept-and-Parse-Nextcloud-Upload-Broadcasts

## Summary

This procedure triggers file operations in the Nextcloud app to emit broadcasts, which are then intercepted by a malicious receiver to parse and exfiltrate sensitive data like account credentials and file details.

## Description

Once the malicious app is installed, user-initiated uploads or syncs in Nextcloud send sticky broadcasts that the high-priority receiver captures first. Sticky broadcasts persist, allowing retrieval even post-emission. Parsing involves extracting Intent extras; this leads to privacy breaches by disclosing user data to malware on the same device.

## Requirements

1. Nextcloud app and malicious APK installed on same device
2. Permissions for storage and network in malicious app
3. ADB or logcat for monitoring (optional)

## Defense

Defensive measures and detection strategies:

- Avoid sticky broadcasts; use one-time sends
- Implement app sandboxing and ICC restrictions
- Detect anomalies via battery/CPU usage from rogue apps

## Objectives

1. Trigger and capture broadcasts during app usage
2. Parse extras for sensitive information
3. Validate data disclosure impact

## Instructions

### Step 1: Trigger Broadcasts

**Context**: Simulate normal app usage to emit vulnerable broadcasts.

Open Nextcloud app, initiate file upload or folder sync.

### Step 2: Capture in Receiver

**Context**: Ensure malicious receiver processes intent before Nextcloud.

The onReceive method triggers automatically due to priority; monitor logs:

```java
// In MaliciousReceiver.onReceive
if (intent.getAction().equals(FileUploader.UPLOAD_START)) {
    // Parse start event data
    String fileUri = intent.getStringExtra("uploadPath");
    // Exfiltrate
}
```

For sticky retrieval:

```java
// Late registration
Intent stickyIntent = context.registerReceiver(null, new IntentFilter(action));
if (stickyIntent != null) {
    // Process even if missed live
}
```

### Step 3: Parse and Exfiltrate

**Context**: Extract and handle data for analysis or theft.

Log or send extras (account, file info, status) to remote server via HTTP.

**Expected Output**: Captured data sample: {"account":"user@domain.com", "file":"/path/to/secret.pdf", "status":"complete"}

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System
- [[Automated Collection]] Automated Collection

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[interception]]
- [[Exfiltration]]

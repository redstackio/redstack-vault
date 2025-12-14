---
id: proc-access-e2ee-data
tags:
  - mobile
  - data-extraction
  - e2ee
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:42.733Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Access-Encrypted-E2EE-Data

## Summary

This procedure outlines extracting encrypted E2EE data from the Rocket.Chat Mobile app's local storage, enabling subsequent password cracking attacks on versions prior to 4.5.1.

## Description

In the context of exploiting the biased E2EE password generation, attackers first need access to the encrypted communications stored on the device. This involves compromising the mobile device (e.g., via physical access or malware) and retrieving app data files containing E2EE-encrypted messages. The data is typically stored in the app's sandboxed directory, such as /data/data/chat.rocket.android/databases on Android. Once extracted, the encrypted payloads serve as the target for brute-force decryption using the weak initial password.

## Requirements

1. Rooted/jailbroken device or ADB/debugging access for Android; jailbreak or backup access for iOS
2. Knowledge of Rocket.Chat app's storage schema (e.g., SQLite for messages)
3. File transfer tools (e.g., ADB pull or iOS backup extractors)

## Defense

Defensive measures and detection strategies:

- Enable app sandboxing and encryption at the device level (e.g., Android Keystore)
- Monitor for unauthorized file access via mobile security tools like MobileIron
- Use remote wipe on device compromise detection

## Objectives

1. Retrieve intact encrypted E2EE data from app storage
2. Identify password-derived encryption artifacts
3. Prepare data for offline cracking without alerting the user

## Instructions

### Step 1: Compromise Device Access

**Context**: Establish access to the mobile device's file system to reach the app's data.

For Android, enable USB debugging and use ADB:

Connect the device and run:

```bash
adb shell
su  # If rooted
cd /data/data/chat.rocket.android/databases
ls  # List files to identify E2EE-related DBs
```

> This grants shell access; expected output includes listing of SQLite files like rocketchat.db containing encrypted messages.

### Step 2: Extract Encrypted Files

**Context**: Pull the relevant files containing E2EE data for offline analysis.

Use ADB to transfer:

```bash
adb pull /data/data/chat.rocket.android/databases/rocketchat.db .
adb pull /data/data/chat.rocket.android/files/e2ee/ .
```

> Expected output: Local copies of encrypted databases and files; verify integrity with file hashes.

### Step 3: Inspect for E2EE Payloads

**Context**: Confirm the presence of encrypted content to validate extraction.

Open the DB with sqlite3:

```bash
sqlite3 rocketchat.db
SELECT * FROM messages WHERE encrypted = 1;
```

> Expected output: Rows with base64-encoded encrypted message bodies, confirming E2EE data availability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mobile]]
- [[data-extraction]]
- [[e2ee]]

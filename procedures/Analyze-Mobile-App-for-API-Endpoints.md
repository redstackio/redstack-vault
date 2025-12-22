---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - recon
  - mobile
  - api
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/analyze-app-traffic]]'
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:27.621Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-Mobile-App-for-API-Endpoints

## Summary

This procedure involves reverse engineering a mobile application to identify API endpoints, focusing on those handling file paths, as a precursor to vulnerability discovery in apps like Starbucks Korea.

## Description

In the context of the Starbucks Korea mobile app, this step requires monitoring network traffic during app usage to uncover API calls to https://msr.istarbucks.co.kr:6443/appif/. Decompiling the APK or using traffic interception tools reveals endpoints vulnerable to path manipulation. Prerequisites include app installation on an emulator or rooted device for proxy setup.

## Requirements

1. Mobile app APK or installed app
2. Proxy tool like Burp Suite or mitmproxy for traffic interception
3. Emulator (e.g., Android Studio) for controlled testing

## Defense

Defensive measures and detection strategies:

- Implement app traffic encryption with certificate pinning
- Monitor for unusual proxy connections in logs
- Use runtime application self-protection (RASP) to detect decompilation attempts

## Objectives

1. Identify API base URL and endpoints
2. Locate file path parameters
3. Map request formats for exploitation

## Instructions

### Step 1: Set Up Traffic Interception

**Context**: Configure a proxy to capture app requests without alerting the app.

**Command** ([[commands/analyze-app-traffic]]):
```bash
mitmproxy --mode transparent --listen-port 8080
```

> This starts a proxy server. Configure the device/emulator to route traffic through it, installing the proxy's CA certificate to decrypt HTTPS.

### Step 2: Interact with App and Capture Traffic

**Context**: Perform actions in the app to trigger API calls, filtering for the target domain.

**Command** ([[commands/filter-traffic]]):
```bash
mitmdump -s script.py --set target_host=msr.istarbucks.co.kr
```

> Run a script to log requests to /appif/. Expected output: JSON payloads with file path params.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/analyze-app-traffic]]
- [[commands/filter-traffic]]

## Tools Used


## Tags

- [[recon]]
- [[mobile]]
- [[api]]

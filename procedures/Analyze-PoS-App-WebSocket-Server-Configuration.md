---
tags:
  - recon
  - websocket
  - android
type: procedure
tools:
  - '[[tools/netstat]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/netstat-listen-sockets]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:30:58.475Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 039f7d76-dd77-4064-9e21-3938fdabe118
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Analyze PoS App WebSocket Server Configuration

## Summary

This procedure involves analyzing the Shopify PoS Android app to identify the WebSocket server's configuration, confirming it binds to all interfaces (0.0.0.0:5000), which exposes it to local network attacks.

## Description

In a local WiFi environment, the PoS app's customer view WebSocket server is vulnerable due to listening on all interfaces. By reverse-engineering the app (e.g., decompiling the APK) and using network tools, attackers can verify the binding and connection string construction using the device's WiFi IP. This step is crucial for planning MiTM attacks as it reveals the attack surface without requiring app modification.

## Requirements

1. Android device with Shopify PoS app installed or APK access
2. ADB shell access or rooted device for running commands
3. Decompiler tools like JADX for code analysis
4. Local network access to the target device

## Defense

Defensive measures and detection strategies:

- Bind WebSocket servers to localhost (127.0.0.1) instead of 0.0.0.0
- Monitor for unusual network bindings using app logs or endpoint protection
- Use network segmentation to isolate PoS devices from general WiFi

## Objectives

1. Confirm WebSocket server exposure on port 5000
2. Extract connection details for relay setup
3. Identify crypto handshake entry points

## Instructions

### Step 1: Decompile and Examine App Code

**Context**: Reverse-engineer the APK to locate the WebSocket server setup in com.shopify.pos.customerview.server.CustomerViewWebSocketServer::getConnectionString(), which uses WiFi IP and binds to 0.0.0.0:5000.

No command required; use JADX or similar to view source.

> Decompiled code shows server listening on all interfaces, enabling local MiTM.

### Step 2: Verify Server Binding with Netstat

**Context**: Run [[commands/netstat-listen-sockets]] on the Android device via ADB shell to list listening sockets and confirm port 5000 binding.

**Command** ([[commands/netstat-listen-sockets]]):
```bash
netstat -an | egrep 'LISTEN[^I]'
```

> This filters listening sockets, excluding irrelevant outputs; expect tcp 0 0 0.0.0.0:5000 0.0.0.0:* LISTEN.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/netstat-listen-sockets]]

## Tools Used

- [[tools/netstat]]

## Tags

- recon
- websocket
- android

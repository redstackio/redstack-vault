---
tags:
  - mitm
  - websocket
  - relay
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:30:58.471Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 1baf7ac4-2c92-4e8b-9fc8-25ac8621085a
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Build WebSocket Relay Server for Message Interception

## Summary

This procedure creates a custom relay server to intercept and monitor WebSocket messages between the Shopify PoS server and customer view app, revealing the unencrypted handshake details like public keys and nonces.

## Description

The relay acts as a transparent proxy for ws:// connections, allowing snooping on raw messages before Curve25519 encryption. Implemented in Python with the websockets library, it helps understand the initial communication from the QR code without altering traffic yet. This is essential for crafting key override exploits.

## Requirements

1. Python 3 with websockets library (pip install websockets)
2. Attacker machine on the same network as the target
3. Knowledge of WebSocket protocol and basic proxying
4. Port forwarding setup if needed

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS for WebSockets (wss://)
- Log and alert on unexpected proxy connections or traffic anomalies
- Use end-to-end encryption validation in app code

## Objectives

1. Proxy WebSocket traffic without disruption
2. Capture handshake elements (public key, nonce)
3. Analyze message formats for exploitation

## Instructions

### Step 1: Implement Relay Server

**Context**: Write a Python script to create a relay that forwards messages while logging them.

**Command** (Python script execution):
```bash
python websocket_relay.py --listen-port 5000 --target-ip <pos-ip>
```

> The script connects to the real server, logs plaintext handshake, and relays; expect logs showing initial public key exchange.

### Step 2: Test Relay with PoS Connection

**Context**: Direct the client app to connect through the relay by spoofing or DNS, observing the QR code-derived nonce and key.

No specific command; monitor logs for raw messages.

> Successful relay shows unencrypted startup messages, confirming crypto setup visibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- mitm
- websocket
- relay

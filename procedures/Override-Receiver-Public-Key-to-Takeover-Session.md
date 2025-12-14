---
tags:
  - crypto-override
  - session-takeover
  - curve25519
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Android
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Encrypted Channel]]'
updated_at: '2025-12-14T17:30:58.462Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: e2bca6d5-e90a-455a-b591-f59c694d0e23
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Encrypted Channel]]'
---
# Override Receiver Public Key to Takeover Session

## Summary

This procedure injects a new receiver public key during the WebSocket handshake, exploiting the lack of ACK validation to override the Curve25519 key and takeover the session for data interception and modification.

## Description

The client app's ClientCryptoProtocol::receiveMessageFromServer() calls setReceiverPublicKey() without verifying the encrypted ACK if cryptoType != 1, allowing unconditional override. By altering message types in the MiTM relay, the attacker sets their own key, decrypting subsequent messages to modify carts, tips, opt-ins, and view customer info.

## Requirements

1. Active MiTM relay from previous steps
2. Extracted initial public key and nonce (from QR or messages)
3. Curve25519 implementation for key generation (e.g., libsodium)
4. Ability to parse/modify WebSocket frames

## Defense

Defensive measures and detection strategies:

- Validate all public keys with encrypted ACK checks in crypto protocol
- Use mutual authentication in handshake
- Implement key pinning or rotation with server-side verification

## Objectives

1. Bypass key validation to set attacker-controlled key
2. Achieve full decryption/encryption control
3. Manipulate session data without detection

## Instructions

### Step 1: Extract Initial Key and Nonce

**Context**: From relay logs, pull the original public key and nonce from QR code scan or startup message.

No command; parse logs manually or with script.

> Key and nonce obtained in raw form for replication.

### Step 2: Generate and Inject New Key

**Context**: In the relay, modify the message to change type, triggering the override condition (cryptoType != 1), and insert attacker's Curve25519 public key via setReceiverPublicKey().

**Command** (example Python snippet in relay):
```python
import nacl.public
box = nacl.public.SealedBox(nacl.public.PrivateKey.generate())
new_pubkey = box.public_key
# Inject into message payload
message['receiverPublicKey'] = bytes(new_pubkey).hex()
```

> Relay sends modified message; client accepts without validation, switching to attacker's key.

### Step 3: Verify Takeover and Manipulate Data

**Context**: Decrypt incoming messages with private key; modify (e.g., change tip) and re-encrypt before forwarding.

> Successful override allows reading customer details and altering cart; test by opting into emails or viewing phone.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Encrypted Channel]] Encrypted Channel

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- crypto-override
- session-takeover
- curve25519

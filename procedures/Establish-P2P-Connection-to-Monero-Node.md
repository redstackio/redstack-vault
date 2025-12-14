---
id: e6a66b05-f175-47d4-8cb2-8ec49b081b89
name: Establish-P2P-Connection-to-Monero-Node
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.817Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Web Protocols]]'
sub_techniques: []
tags:
  - p2p
  - connection
  - monero
  - cryptonote
commands: []
platforms:
  - Linux
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Web Protocols]]'
---

# Establish-P2P-Connection-to-Monero-Node

## Summary

This procedure establishes a peer-to-peer connection to a Monero node using the CryptoNote protocol, serving as the initial access point for subsequent DoS exploitation.

## Description

In the context of attacking Monero nodes, connecting via the P2P port (default 18080) is essential. The CryptoNote protocol requires a handshake involving version exchange and peer ID negotiation. This step is low-impact on its own but enables remote interaction without authentication. Prerequisites include network reachability to the target and a compatible client implementation, typically in C++ mirroring the Monero codebase.

## Requirements

1. Network access to the target's P2P port (e.g., TCP 18080)
2. Custom or modified CryptoNote P2P client (based on Monero source code)
3. Knowledge of CryptoNote protocol binary serialization

## Defense

Defensive measures and detection strategies:

- Firewall rules to restrict P2P port access to trusted peers
- Rate limiting on incoming P2P connections
- Logging of handshake attempts for anomaly detection

## Objectives

1. Gain remote access to the node's protocol handler
2. Verify node responsiveness for exploitation
3. Establish a channel for malicious message transmission

## Instructions

### Step 1: Implement or Launch P2P Client

**Context**: Create or use a client that initiates the CryptoNote P2P handshake. This involves sending a handshake message with protocol version, peer ID, and network address.

Implement the connection logic by serializing a binary handshake packet (e.g., using Boost.Serialization or manual byte crafting in C++):

- Protocol version: 0x07 (for recent Monero)
- Peer ID: Random 8-byte value
- Reserved fields and timestamp as per spec

Connect via socket to target IP:18080 and send the packet.

> Upon success, the node responds with its handshake, confirming connection. Expected output: Binary response packet with matching version and peer details.

### Step 2: Negotiate and Maintain Connection

**Context**: Handle the node's response and exchange timing sync messages to keep the connection alive.

After handshake, send periodic p2p::PING messages to maintain the session.

> This ensures the connection remains open for the next exploitation step. Expected output: ACK responses from the node.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Web Protocols]] Web Protocols (adapted for P2P)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[p2p]]
- [[monero]]
- [[connection]]

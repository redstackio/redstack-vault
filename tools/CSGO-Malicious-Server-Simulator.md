---
id: tool-csgo-server-001
url: null
tags:
  - exploit
  - server-sim
type: tool
verified: false
platforms:
  - Windows
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.189Z'
validated: true
submitted: true
---
# CSGO-Malicious-Server-Simulator

**Status**: Unverified

## Overview

A Python 3 script that simulates a malicious CS:GO server, sending crafted Protobuf messages to exploit the Source Engine signedness vulnerability for RCE demonstration.

## Description

This tool emulates a Source Engine server, allowing attackers to send custom CSVCMsg_ClassInfo, CCSUsrMsg_ShowMenu, and other messages over UDP/TCP. It handles entity spawning, cvar sets, and connection management for heap spraying and exploitation. Used in offensive security to replicate the HackerOne-reported RCE.

## Features

- Feature 1: Protobuf message crafting for ClassInfo underflow.
- Feature 2: Heap spraying via entity commands.
- Feature 3: ROP chain delivery and pointer leakage simulation.

## Installation

### Requirements

- Python 3.6+
- protobuf library: `pip install protobuf`

### Install Commands

```bash
pip install protobuf
# Clone or load script (F831986)
```

## Basic Usage

```bash
python malicious_server.py --port 27015 --target client_ip
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `-p, --port` | Server port (default 27015) |
| `-t, --target` | Victim IP |

## Examples

### Example 1: Basic Server Start

```bash
python malicious_server.py
```

### Example 2: Exploit Mode

```bash
python malicious_server.py --exploit rce --rop-chain calc.exe_gadgets.bin
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1203.001]] Exploitation for Client Execution
- [[DLL Search Order Hijacking]] Hijack Execution Flow

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on game ports with anomalous Protobuf payloads.
- Rapid entity messages from unknown servers.

## Related Procedures

- [[procedures/Heap-Spraying-for-Predictable-Allocations]]
- [[procedures/Pointer-Leakage-via-ClassInfo-Underflow]]

## Related Tools

- [[tools/Steam-Browser-Attack-HTML]]

## References

- HackerOne Report #876719

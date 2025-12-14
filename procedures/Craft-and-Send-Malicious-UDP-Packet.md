---
id: proc-uuid-3
tags:
  - dos
  - udp-packet
  - poc-script
  - rlp-malformed
type: procedure
tools:
  - '[[tools/Python-3]]'
  - '[[tools/pysha3]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/install-pysha3]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.329Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Craft-and-Send-Malicious-UDP-Packet

## Summary

This procedure prepares a Python environment and executes a proof-of-concept script to generate and send a crafted UDP packet containing malformed RLP data, triggering the infinite loop in the RSKJ server's decode2 function and initiating the denial-of-service.

## Description

The exploit targets the RLP decoding in RLP.java, where bytesToLength returns -5, setting length to 0 without advancing position, causing an infinite loop at line 490. The PoC uses pysha3 for SHA3 hashing to craft the payload. Requires Python 3 on Linux; modify HOST in poc.py to target's IPv6 address and port 5050. Expected outcome: Packet sent, server begins hanging on processing.

## Requirements

1. Python 3 installed on client machine
2. Network reachability to target's UDPv6 port 5050
3. poc.py script downloaded from vulnerability disclosure source

## Defense

Defensive measures and detection strategies:

- Implement RLP input sanitization and length bounds checking
- Monitor for anomalous UDP packet sizes or patterns from unknown sources
- Use firewalls to rate-limit UDP traffic on port 5050

## Objectives

1. Install dependencies and prepare the exploit script
2. Send the malformed UDP packet to exploit the vulnerability
3. Trigger uncontrolled resource consumption on the server

## Instructions

### Step 1: Install pysha3 Library

**Context**: Install the required Python library for SHA3 operations in the PoC.

**Command** ([[commands/install-pysha3]]):
```bash
pip install pysha3
```

> Expected output: "Successfully installed pysha3" message.

### Step 2: Configure and Run PoC Script

**Context**: Download poc.py, set HOST to target IP (e.g., [::1] for localhost), and execute to send the packet.

Run the script:

```bash
python3 poc.py
```

> The script crafts RLP data with trailing zeros and negative length simulation, sends via UDP to port 5050. Expected output: Confirmation of packet transmission.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used

- [[commands/install-pysha3]]

## Tools Used

- [[tools/Python-3]]
- [[tools/pysha3]]

## Tags

- [[dos]]
- [[udp-packet]]
- [[poc-script]]
- [[rlp-malformed]]

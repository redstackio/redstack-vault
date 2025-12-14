---
tags:
  - packet-analysis
  - fb-packet
  - mysql
type: procedure
tools:
  - '[[tools/tcpdump]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:28:20.386Z'
sub_techniques: []
id: 08dbda09-10f4-43a7-b782-59498a8c55d8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Capture and Analyze FB Packet in MySQL Traffic

## Summary

This procedure involves dissecting captured network packets from a LOAD DATA LOCAL INFILE operation to pinpoint the vulnerable 'FB' packet, which echoes the filename back to the client.

## Description

Using the pcap file from tcpdump, examine the server response following the LOAD DATA query. The FB packet has a specific structure: 2-byte size (0c), 1-byte packet number (000001), 1-byte type (fb), followed by the null-terminated filename (e.g., /etc/passwd hex-encoded as 2f6574632f70617373776400). This analysis confirms the protocol flaw exploitable by a rogue server.

## Requirements

1. tcpdump pcap file from prior capture
2. Tools like Wireshark or tcpdump for analysis
3. Knowledge of MySQL wire protocol

## Defense

Defensive measures and detection strategies:

- Validate all incoming MySQL packets for unexpected types like FB
- Implement client-side checks to ignore unsolicited filename packets
- Log and alert on anomalous protocol sequences

## Objectives

1. Identify FB packet in traffic
2. Decode filename and structure
3. Document flaw for rogue server crafting

## Instructions

### Step 1: Read and Filter Pcap

**Context**: Load the capture and filter for MySQL traffic post-query.

**Command**:
```bash
tcpdump -r mysql_traffic.pcap -nn -X | grep -A 5 -B 5 'fb'
```

> Filters for the FB type byte, showing surrounding hex dump.

### Step 2: Decode Packet Structure

**Context**: Manually parse the packet to extract components.

**Command**:
```bash
xxd mysql_traffic.pcap | grep '0c 00 01 fb'
```

> Locates the packet header (size 0c, seq 01, type fb) and following filename.

### Step 3: Verify Filename Echo

**Context**: Confirm the echoed filename matches the query.

**Command**:
```bash
echo '2f6574632f70617373776400' | xxd -r -p
```

> Converts hex to ASCII, outputting /etc/passwd\0.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/tcpdump]]

## Tags

- packet-analysis
- fb-packet
- mysql

---
tags:
  - pcap-analysis
  - wireshark
  - exfiltration
type: procedure
tools:
  - '[[tools/Wireshark]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.692Z'
sub_techniques: []
id: 64a6f9ee-04ff-4a77-b6b5-346705568e4e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Analyze-PCAP-with-Wireshark

## Summary

This procedure analyzes the captured PCAP file using Wireshark to extract and view the sensitive file contents exfiltrated via the MySQL LFI exploit.

## Description

After capturing traffic with tcpdump, Wireshark dissects the MySQL protocol packets to reveal the file data. Look for the login packet with LoadLocalData=1 and the subsequent 'Request Command Unknown' packet containing the file payload. Prerequisites: Wireshark installed and PCAP file available. Expected outcome: Readable file contents from the target server.

## Requirements

1. Wireshark installed (download from wireshark.org)
2. Captured PCAP file (e.g., infogramsteal.pcap)
3. Basic knowledge of MySQL protocol dissection
4. Host OS supporting Wireshark (Linux/Windows/macOS)

## Defense

Defensive measures and detection strategies:

- Enable MySQL protocol logging on servers
- Use anomaly detection for unexpected file reads
- Scan for Wireshark/tcpdump usage in environments
- Implement data loss prevention (DLP) for file exfiltration

## Objectives

1. Dissect MySQL packets to confirm LFI success
2. Extract file contents like /etc/passwd
3. Validate LoadLocalData feature enabled

## Instructions

### Step 1: Open PCAP File

**Context**: Load the capture into Wireshark.

**Instructions**: Launch Wireshark and open infogramsteal.pcap via File > Open.

> Expected output: Packet list loads with MySQL traffic.

### Step 2: Filter and Inspect

**Context**: Focus on relevant MySQL packets.

**Instructions**: Apply filter `mysql` or `tcp.port == 3306`. Select the initial handshake packet to check for LoadLocalData=1 in the MySQL Client Authentication packet. Then, find the LOAD DATA packet labeled 'Request Command Unknown' and expand to view file data payload.

> Expected output: File lines visible in hex or text view (e.g., root:x:0:0... from /etc/passwd).

### Step 3: Export Data

**Context**: Save extracted contents if needed.

**Instructions**: Right-click the payload packet and select Follow > TCP Stream or export objects.

> Expected output: Clean text file with exfiltrated data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Wireshark]]

## Tags

- pcap-analysis
- wireshark
- exfiltration

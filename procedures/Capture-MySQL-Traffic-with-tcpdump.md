---
tags:
  - network-capture
  - mysql
  - tcpdump
type: procedure
tools:
  - '[[tools/tcpdump]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/tcpdump-mysql-capture]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:26:22.706Z'
sub_techniques: []
id: f1948752-8618-4ecf-bc5d-1a24d8c350c2
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Capture-MySQL-Traffic-with-tcpdump

## Summary

This procedure uses tcpdump to capture network traffic on the attacker's MySQL server during the Infogram connection attempt, recording packets containing exfiltrated file data.

## Description

As part of the LFI exfiltration, Infogram's MySQL client connects to the attacker's server and sends file contents via the LOAD DATA LOCAL INFILE protocol. tcpdump captures this on port 3306. Prerequisites: Attacker Linux server with tcpdump installed and MySQL running. Expected outcome: PCAP file with MySQL packets including file data.

## Requirements

1. Linux server with tcpdump installed (apt install tcpdump)
2. Root or sudo access for packet capture
3. eth0 interface (or appropriate NIC)
4. MySQL listening on 3306

## Defense

Defensive measures and detection strategies:

- Monitor for tcpdump or similar tools on servers
- Use network segmentation to limit outbound app connections
- Implement IDS rules for anomalous MySQL traffic patterns
- Encrypt sensitive MySQL communications with TLS

## Objectives

1. Capture incoming MySQL connections from Infogram
2. Record packets with LoadLocalData flag and file contents
3. Save to PCAP for offline analysis

## Instructions

### Step 1: Start Capture

**Context**: Begin listening on MySQL port before triggering the exploit.

**Command** ([[commands/tcpdump-mysql-capture]]):
```bash
tcpdump -s 0 port 3306 -i eth0 -w infogramsteal.pcap
```

> Captures full packets on eth0 to file. Expected output: Live capture display, file growing.

### Step 2: Stop Capture

**Context**: End after exploit execution.

**Instructions**: Press Ctrl+C once Infogram error appears.

> Finalizes the PCAP. Expected output: Capture stopped, file ready.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques


## Commands Used

- [[commands/tcpdump-mysql-capture]]

## Tools Used

- [[tools/tcpdump]]

## Tags

- network-capture
- mysql
- tcpdump

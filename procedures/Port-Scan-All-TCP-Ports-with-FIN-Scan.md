---
id: 6be0a602-f92b-446a-b7f6-53d330b4d9f4
name: Port-Scan-All-TCP-Ports-with-FIN-Scan
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T19:01:25.720362+00:00'
updated_at: '2023-05-26T00:47:29.774295+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/nmap-fin-scan-with-service-version-detection]]'
tools:
  - '[[tools/Nmap]]'
platforms:
  - Linux
  - Network
validated: true
---

# Port-Scan-All-TCP-Ports-with-FIN-Scan

## Summary

This procedure performs a comprehensive FIN scan on all TCP ports of a target host using Nmap, combined with service version detection. It is useful for bypassing certain firewalls that may block or filter SYN packets, allowing discovery of additional open ports and services that standard SYN scans might miss.

## Description

A FIN scan sends TCP packets with only the FIN bit set, which can elicit responses from open ports without completing a full TCP handshake. This technique is particularly effective against non-stateful firewalls or systems that do not properly handle unexpected FIN packets. By scanning all 65535 TCP ports (-p-) and enabling service version detection (-sV), the procedure identifies not only open ports but also the versions of running services, providing valuable reconnaissance data for further exploitation. This approach is commonly used in penetration testing when initial SYN scans yield incomplete results due to firewall evasion tactics.

## Requirements

1. Nmap tool installed on the attacking machine (version 7.0 or later recommended).
2. Network connectivity to the target IP address, with no blocking firewalls on the attacker's side.
3. Basic knowledge of TCP/IP and port scanning concepts.
4. Target host that is responsive to TCP probes (e.g., not firewalled to drop all FIN packets).

## Defense

Defensive measures include configuring stateful firewalls to drop invalid TCP packets like FIN scans, enabling intrusion detection systems (IDS) to alert on scan patterns, and logging anomalous TCP traffic. Tools like Snort or Suricata can detect Nmap FIN scans via signatures for -sF flags. Network segmentation and rate limiting can also mitigate reconnaissance attempts.

## Objectives

1. Identify open TCP ports on the target that may be hidden from SYN scans.
2. Enumerate service versions to assess potential vulnerabilities.
3. Gather intelligence for subsequent attack phases, such as targeted exploitation.
4. Verify host responsiveness and basic network characteristics.

## Instructions

### Step 1: Execute FIN Scan with Service Version Detection

**Context**: This step initiates the FIN scan across all TCP ports while probing for service details. It sends FIN packets to each port and analyzes responses to determine open, closed, or filtered states. Service detection runs only on identified open ports to avoid unnecessary noise. Use this when standard scans are blocked, as FIN scans can sometimes succeed where others fail.

**Command** ([[commands/nmap-fin-scan-with-service-version-detection]]):
```bash
nmap -sV -sF -p- $_TARGET_IP
```

> This command performs the scan and outputs a report listing open ports, services, and versions. The -sF flag enables the FIN scan, -p- scans all ports, -sV detects service versions, and $_TARGET_IP is replaced with the actual target address (e.g., 10.10.10.10). Expect the scan to take several minutes depending on network latency and host responsiveness. Review the output for open ports like 21/tcp or 22/tcp, which indicate potential entry points. If no ports are found, consider alternative scan types like XMAS or NULL scans.

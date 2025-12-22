---
id: 947caf48-e5cf-4a22-ae68-851706f04af3
name: Basic-Port-Scan-and-Scripted-Service-Enumeration
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T18:35:43.404781+00:00'
updated_at: '2023-05-26T00:52:19.234580+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/Nmap-Service-Scan-with-Default-Scripts]]'
platforms:
  - Linux
  - Windows
  - macOS
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Basic-Port-Scan-and-Scripted-Service-Enumeration

## Summary

This procedure performs a basic SYN port scan on a target host followed by service version detection and execution of default Nmap Scripting Engine (NSE) scripts to enumerate open services, identify software versions, and gather additional details like anonymous access or configuration information. It is commonly used during the reconnaissance phase to map the attack surface without completing full TCP connections, minimizing detection risk.

## Description

In offensive security operations, understanding the services running on a target is crucial for identifying potential entry points. This procedure uses Nmap's SYN scan (-sS implied by default behavior with -sV) to stealthily probe ports, detect service versions with -sV, and run safe default scripts via -sC to reveal details such as FTP anonymous login status or HTTP server banners. The technique aligns with passive and active network discovery, helping attackers prioritize vulnerabilities based on exposed services. It assumes the attacker has network visibility to the target but no prior credentials, and it's effective against common firewalls that drop SYN packets.

## Requirements

1. Network connectivity to the target IP or hostname (no firewall blocking outbound scans).
2. Nmap tool installed on the attacker's machine (version 7.0 or later recommended for full NSE support).
3. Administrative privileges on the attacker's host if scanning requires raw sockets (common on Unix-like systems).
4. Basic knowledge of networking to interpret scan results.

## Defense

Defensive measures include network segmentation, firewall rules to limit scan traffic, intrusion detection systems (IDS) like Snort to alert on port scans, and endpoint protection that monitors for anomalous outbound connections. Detection can involve logging SYN packets without ACK responses or using tools like Zeek for scan pattern analysis.

## Objectives

1. Identify open ports on the target host.
2. Determine service versions and potential vulnerabilities.
3. Gather configuration details via NSE scripts to inform further exploitation.
4. Validate host responsiveness and basic service accessibility.

## Instructions

### Step 1: Verify Nmap Installation and Target Reachability

**Context**: Before scanning, confirm Nmap is available and the target is reachable to avoid false negatives from tool or network issues. This step ensures prerequisites are met and provides baseline connectivity data.

Use a simple ping or initial scan to test reachability, but since this procedure focuses on port scanning, proceed directly if ping is blocked.

**Command** ([[commands/Nmap-Host-Discovery]]):
```bash
nmap -sn $_TARGET_IP
```

> This command performs a ping scan (-sn) to check if the host is up without port scanning. Expected output includes host status (up/down) and latency. If the host is down, abort the procedure.

### Step 2: Execute SYN Scan with Service Detection and Default Scripts

**Context**: Launch the core scan to detect open ports, identify services, and run enumeration scripts. The -sV flag probes for version details, while -sC executes safe NSE scripts for additional intel like anonymous access checks. This step accomplishes the primary objective of service enumeration.

**Command** ([[commands/Nmap-Service-Scan-with-Default-Scripts]]):
```bash
nmap -sV -sC $_TARGET_IP
```

> Run this from a Kali Linux or similar environment. The scan will output open ports, service names, versions, and script results (e.g., FTP anonymous login allowed). Review for high-value services like SSH, HTTP, or databases. If stealth is needed, add -T2 for slower timing.

### Step 3: Analyze and Save Results for Further Use

**Context**: Post-scan, save output to a file for documentation and integration with other tools (e.g., feeding to vulnerability scanners). This verifies success and prepares data for chaining into more advanced procedures like vulnerability scanning.

Save the output using Nmap's -oN flag or redirect stdout.

**Command** ([[commands/Nmap-Service-Scan-with-Default-Scripts]] variation):
```bash
nmap -sV -sC -oN scan_results.txt $_TARGET_IP
```

> Expected output is written to scan_results.txt, including a summary of open ports and services. Success is indicated by the file containing version info and script findings without errors like 'host seems down'.

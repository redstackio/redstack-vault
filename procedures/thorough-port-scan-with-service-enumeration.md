---
id: 1fce62e4-778b-4a93-b78c-572637ee1edd
name: thorough-port-scan-with-service-enumeration
type: procedure
verified: true
submitted: true
created_at: '2019-10-11T19:37:17.178400+00:00'
updated_at: '2023-05-26T00:40:33.582175+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043]]'
techniques:
  - '[[techniques/Scan Network Protocols Services and Targets|T1595.002]]'
sub_techniques: []
tags:
  - enumeration
  - network
  - reconnaissance
commands:
  - '[[commands/nmap-scan-with-service-enumeration]]'
  - '[[commands/nmap-udp-scan-with-service-enumeration]]'
  - '[[commands/nmap-full-port-scan-with-service-enumeration]]'
platforms:
  - Linux
  - Windows
  - Network
tools:
  - '[[tools/Nmap]]'
validated: true
---

# thorough-port-scan-with-service-enumeration

## Summary

This procedure performs comprehensive port scanning on a target host to identify open ports, running services, and versions, helping to map the attack surface for further exploitation, such as targeting web services on port 80.

## Description

Port scanning probes TCP/UDP ports to determine listening services, which is essential in reconnaissance to identify vulnerable applications like web servers. Multiple scan types are used progressively: SYN for quick TCP checks, UDP for non-TCP services, and full scans for thorough coverage. This is typically the first step in engaging a new target, assuming only network access is available.

## Requirements

- Network connectivity to target IP
- Nmap installed on attacker machine
- No special privileges needed for basic scans

## Defense

- Implement firewalls to limit port exposure (e.g., only 80/443 open)
- Use intrusion detection systems (IDS) to alert on scan patterns
- Rate-limit incoming connections to detect brute-force probes

## Objectives

- Discover open ports and services
- Identify web server for follow-on web attacks
- Gather version info for vulnerability research

## Instructions

### Step 1: Basic TCP SYN Scan with Version Detection

**Context**: Perform an initial quick scan on the top 1000 ports to identify common services without completing full connections, reducing detection risk.

**Command** ([[commands/nmap-scan-with-service-enumeration]]):
```bash
nmap -sV $_TARGET_IP -oN initial_scan.txt
```

> This command sends SYN packets and detects service versions via banner grabbing. Expect output listing open ports like 80/tcp open http.

### Step 2: UDP Port Scan with Version Detection

**Context**: Scan UDP ports, which may host services like DNS or SNMP, often overlooked in TCP-focused scans.

**Command** ([[commands/nmap-udp-scan-with-service-enumeration]]):
```bash
nmap -sU -sV $_TARGET_IP -oN udp_scan.txt
```

> UDP scans are slower due to lack of acknowledgments; look for open|filtered states indicating potential services.

### Step 3: Full TCP Port Scan

**Context**: Exhaustively scan all 65535 TCP ports to ensure no obscure services are missed, confirming web presence.

**Command** ([[commands/nmap-full-port-scan-with-service-enumeration]]):
```bash
nmap -sV -p- $_TARGET_IP -oN full_scan.txt
```

> This is resource-intensive; success is confirmed by identifying HTTP on port 80 with Apache/WordPress indicators.

---
id: proc-discover-smi-001
tags:
  - recon
  - port-scan
  - cisco
  - smi
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-port-scan]]'
verified: false
platforms:
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:27.360Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Vulnerability Scanning]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover Exposed Cisco SMI Service

## Summary

This procedure involves scanning a target network-connected machine to identify an exposed Cisco Smart Install (SMI) service on TCP port 4786, which serves as an entry point for further exploitation.

## Description

Cisco SMI is a protocol for managing network switches but, when exposed without authentication, allows remote attackers to perform reconnaissance and prepare for RCE. This procedure uses port scanning to detect the service on an Informatica machine or similar embedded/network platform. Prerequisites include network access to the target IP. Expected outcomes: Confirmation of open port and service banner.

## Requirements

1. Network connectivity to the target IP
2. Nmap tool installed on the attacker's machine
3. Basic knowledge of port 4786 as the SMI default

## Defense

Defensive measures and detection strategies:

- Firewall rules to block inbound TCP 4786
- Regular port scanning with tools like nmap from internal networks to identify exposures
- Disable unnecessary services like SMI on non-Cisco devices

## Objectives

1. Identify vulnerable services on the target
2. Gather service version for exploit selection
3. Prepare for initial access via public-facing application

## Instructions

### Step 1: Perform Targeted Port Scan

**Context**: Scan the target IP for the SMI port to confirm exposure.

**Command** ([[commands/nmap-port-scan]]):
```bash
nmap -p 4786 -sV <target_ip>
```

> This command probes port 4786 and detects the service version. Expected output includes a banner like "4786/tcp open  cisco-smi" if exposed.

### Step 2: Verify Service Response

**Context**: If open, attempt a basic connection to elicit a response.

**Command** ([[commands/nc-connect]]):
```bash
nc -v <target_ip> 4786
```

> Send a simple probe; SMI may respond with protocol data. Success confirms the service is active and unauthenticated.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

- [[Vulnerability Scanning]]

## Commands Used

- [[commands/nmap-port-scan]]
- [[commands/nc-connect]]

## Tools Used

- [[tools/nmap]]

## Tags

- [[recon]]
- [[port-scan]]
- [[cisco]]

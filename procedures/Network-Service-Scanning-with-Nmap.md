---
id: proc-nmap-scanning-927413
tags:
  - scanning
  - port-enum
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-port-scan]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:27:35.678Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Network-Service-Scanning-with-Nmap

## Summary

This procedure employs nmap to scan the target IP for open ports, services, and versions, revealing potential entry points like port 443 on Zomato's AWS-hosted infrastructure.

## Description

Nmap performs comprehensive port scanning and service detection on the resolved IP (52.77.124.190), identifying vulnerabilities in exposed services. In this scenario, it uncovers web services that lead to further enum, with risks of detection via traffic logs.

## Requirements

1. Nmap installed
2. Target IP address
3. Elevated privileges for raw sockets (optional)

## Defense

Defensive measures and detection strategies:

- Deploy IDS/IPS to alert on port scans
- Use cloud WAF to block scanning IPs

## Objectives

1. Identify open ports and services
2. Enumerate service versions for vuln research
3. Map attack surface

## Instructions

### Step 1: Run Comprehensive Scan

**Context**: Scan all ports with version detection to detail services.

**Command** ([[commands/nmap-port-scan]]):
```bash
nmap -sV -p- 52.77.124.190
```

> Output includes open ports (e.g., 443/TCP HTTPS) and service banners, aiding in identifying misconfigs like exposed auth services.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/nmap-port-scan]]

## Tools Used

- [[tools/nmap]]

## Tags

- [[scanning]]
- [[port-enum]]

---
tags:
  - port-scan
  - service-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/nmap-port-scan-on-ip]]'
platforms:
  - Cloud
  - Linux
techniques:
  - '[[Network Service Scanning]]'
skill_level: beginner
impact_level: medium
detection_risk: high
sub_techniques: []
id: b929b413-d5fd-440c-a55e-457e6aa604db
created_at: '2025-12-14T03:15:05.037Z'
updated_at: '2025-12-14T03:15:05.037Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Port-Scan-Exposed-Origin-IPs

## Summary

This procedure scans origin IPs for open ports and services, revealing additional attack vectors like direct PostgreSQL access on exposed cloud instances.

## Description

After IP exposure, port scanning identifies unintended open services (e.g., RDP, databases) due to misconfigurations. Uses Nmap on GCP IPs to enumerate ports like 5432/tcp.

## Requirements

1. Nmap installed (common on Linux)
2. Target IP (e.g., 35.241.6.32)
3. Network access (public IPs are scanable)

## Defense

Defensive measures and detection strategies:

- Close unnecessary ports with firewalls (e.g., GCP VPC rules)
- Use intrusion detection to flag port scans (e.g., unusual SYN packets)
- Implement rate limiting on cloud security groups

## Objectives

1. Identify open ports on origin IPs
2. Detect exposed services like PostgreSQL or RDP
3. Guide further exploitation

## Instructions

### Step 1: Perform Full Port Scan with Service Detection

**Context**: Scan all ports to find exposed services.

**Command** ([[commands/nmap-port-scan-on-ip]]):
```bash
nmap -p- -sV 35.241.6.32
```

> Expected output: Ports like 80/tcp open (http), 5432/tcp open (postgres).

### Step 2: Analyze Results for Vulnerabilities

**Context**: Review for high-risk ports (e.g., 3389/tcp RDP).

**Command** (Follow-up targeted scan):
```bash
nmap -p 5432,3389 -sV 35.241.6.32
```

> Confirm service versions for known exploits.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/nmap-port-scan-on-ip]]

## Tools Used

- None

## Tags

- [[port-scan]]
- [[service-discovery]]

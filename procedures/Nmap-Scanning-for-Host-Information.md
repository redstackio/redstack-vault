---
id: proc-nmap-scan-zomato
tags:
  - scanning
  - network-recon
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-host-scan]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:32.271Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Nmap-Scanning-for-Host-Information

## Summary

This procedure performs an in-depth nmap scan on the target's IP to gather network details, open ports, and service information for Zomato targets.

## Description

Following IP discovery, nmap is used to scan the host at 52.77.124.190, revealing services like HTTPS on port 443 and potential vulnerabilities. This active scanning helps map the attack surface in a web-based environment.

## Requirements

1. nmap installed
2. IP address from prior step
3. Sufficient network permissions

## Defense

- Deploy IDS to detect port scans
- Rate-limit incoming scan traffic

## Objectives

1. Identify open ports and services
2. Detect OS and version info
3. Uncover potential entry points

## Instructions

### Step 1: Execute Host Scan

**Context**: Run a version detection and OS fingerprinting scan.

**Command** ([[commands/nmap-host-scan]]):
```bash
nmap -sV -O 52.77.124.190
```

> Output includes port 443/tcp open https, service versions, and OS guesses like Linux.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/nmap-host-scan]]

## Tools Used

- [[tools/nmap]]

## Tags

- [[scanning]]
- [[network-recon]]

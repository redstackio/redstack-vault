---
tags:
  - recon
  - nmap
  - dns
  - bind9
type: procedure
tools:
  - '[[tools/Nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-scan-target]]'
verified: false
platforms:
  - Linux
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:26:30.421Z'
sub_techniques: []
id: e9bd0925-7931-40af-a731-107f9925167a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Scan-Target-with-Nmap-for-Vulnerable-BIND9-Services

## Summary

This procedure uses Nmap to perform network reconnaissance on a target host, identifying open ports and service versions, specifically to detect vulnerable BIND9 DNS servers on port 53.

## Description

In the context of targeting owncloud.com (IP 50.30.33.235), this step scans for services like SSH on port 22 and BIND9 on port 53, revealing version 9.9.4-rpz2.13269.14-P2, which is susceptible to CVE-2015-5477. It enables attackers to map the attack surface and pinpoint DoS opportunities in public-facing DNS infrastructure.

## Requirements

1. Network access to the target host
2. Nmap installed (version 6.49BETA4 or later)
3. Resolver for hostname to IP (e.g., owncloud.com to 50.30.33.235)

## Defense

Defensive measures and detection strategies:

- Implement firewall rules to limit Nmap scan traffic (e.g., rate limiting on unusual UDP/TCP probes)
- Use intrusion detection systems (IDS) like Snort to alert on port scans
- Regularly update and patch services to reduce reconnaissance value

## Objectives

1. Discover open DNS port 53 and BIND9 version
2. Identify potential DoS vectors
3. Map target infrastructure for exploitation

## Instructions

### Step 1: Execute Nmap Scan

**Context**: Launch a basic service version scan to enumerate ports and identify BIND9.

**Command** ([[commands/nmap-scan-target]]):
```bash
nmap owncloud.com
```

> This command resolves owncloud.com to 50.30.33.235, scans common ports, and detects services with version detection enabled by default. Expected output includes host status, open ports (e.g., 22/tcp OpenSSH 5.8, 53/tcp BIND 9.9.4-rpz2.13269.14-P2), and filtered ports.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/nmap-scan-target]]

## Tools Used

- [[tools/Nmap]]

## Tags

- recon
- nmap
- scanning

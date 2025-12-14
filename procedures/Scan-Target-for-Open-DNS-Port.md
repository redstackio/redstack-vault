---
tags:
  - reconnaissance
  - scanning
  - dns
type: procedure
tools:
  - '[[tools/Nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nmap-scan-host]]'
platforms:
  - Linux
  - Network
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: de2f643a-c865-4bfb-bd2b-56813fa44ccd
created_at: '2025-12-14T17:26:36.893Z'
updated_at: '2025-12-14T17:26:36.893Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Scan-Target-for-Open-DNS-Port

## Summary

This procedure uses Nmap to scan a target host for open ports and services, specifically identifying an exposed DNS service on port 53 running BIND9, as part of reconnaissance for potential DoS vulnerabilities.

## Description

In the context of targeting public-facing infrastructure like ci.nextcloud.com, this procedure performs a basic TCP port scan to enumerate services. It reveals port 53 as open and tcpwrapped, indicating a DNS implementation vulnerable to CVE-2015-5477. This step is crucial for confirming the attack surface before proceeding to exploitation. Prerequisites include network access to the target and Nmap installed on a Linux system.

## Requirements

1. Network connectivity to the target host (e.g., internet access for external scans)
2. Nmap tool installed (version 7.40 or later)
3. Basic command-line knowledge

## Defense

Defensive measures and detection strategies:

- Implement firewall rules to limit port scanning (e.g., rate limiting with iptables)
- Use intrusion detection systems (IDS) like Snort to alert on Nmap signatures
- Monitor network logs for unusual scan patterns from unknown IPs

## Objectives

1. Discover open ports and associated services on the target
2. Identify DNS service exposure for further targeting
3. Map the attack surface without alerting defenses

## Instructions

### Step 1: Perform Port Scan

**Context**: Execute a default Nmap scan to identify open ports, focusing on service detection for port 53.

**Command** ([[commands/nmap-scan-host]]):
```bash
nmap ci.nextcloud.com
```

> This command sends SYN packets to common ports and identifies services based on responses. Expected output includes a report listing open ports like 22/tcp open ssh, 53/tcp open domain (tcpwrapped), 80/tcp open http, and 443/tcp open https, confirming DNS presence.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/nmap-scan-host]]

## Tools Used

- [[tools/Nmap]]

## Tags

- [[Reconnaissance]]
- [[scanning]]
- [[DNS]]

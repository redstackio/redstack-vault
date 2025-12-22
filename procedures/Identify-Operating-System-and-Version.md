---
id: 39222e4f-9269-4895-a8c1-22cf4ded889e
name: Identify Operating System and Version
type: procedure
verified: true
submitted: true
created_at: '2019-10-19T01:09:28.077023+00:00'
updated_at: '2023-05-26T00:40:19.084222+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - network
  - reconnaissance
  - discovery
commands:
  - '[[commands/nmap-os-detection-and-service-scan]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Nmap]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Identify Operating System and Version

## Summary

This procedure fingerprints a target's operating system and version through passive and active network techniques, including TTL analysis from ping responses and Nmap-based OS detection combined with service banner enumeration. It enables attackers to gather system information remotely without direct access, aiding in tailoring subsequent exploits to the identified platform.

## Description

Operating system fingerprinting is a key reconnaissance step in network attacks, allowing identification of the target's OS family (e.g., Windows vs. Linux/Unix) and specific version for vulnerability research. This procedure uses ICMP echo requests (ping) to observe TTL values—typically 128 for Windows and 64 for Unix-like systems, adjusted for network hops—and Nmap's OS detection module, which sends probes and matches responses against a database of known signatures. For precise versioning, service banners (e.g., from SSH or HTTP) are enumerated and cross-referenced with OSINT sources like Google or distribution repositories. This approach is non-intrusive but can be evaded by firewalls or custom TTL settings. It applies to remote targets accessible over the network and assumes no authentication barriers.

## Requirements

1. Network connectivity to the target (e.g., ability to send ICMP and TCP/UDP probes).
2. Installation of Nmap tool on the attacker's machine.
3. Access to OSINT resources (e.g., Google, Wikipedia, distribution package trackers like Launchpad or DistroWatch).
4. Basic command-line proficiency for executing scans.

## Defense

Defensive measures include firewall rules to block ICMP (ping) and unnecessary service probes, OS hardening to randomize TTL values or suppress banners, and network segmentation to limit reconnaissance scope. Detection strategies involve monitoring for unusual probe traffic (e.g., Nmap signatures via Snort or Suricata rules) and logging anomalous TTL patterns or service queries.

## Objectives

1. Determine the target's OS family (Windows, Linux/Unix) via TTL and probe responses.
2. Identify the exact OS version through banner enumeration and OSINT correlation.
3. Validate findings to ensure accuracy for follow-on exploitation planning.

## Instructions

### Step 1: Perform TTL Analysis via Ping

**Context**: Send ICMP echo requests to observe the TTL in responses, which indicates the OS family. Windows systems typically return TTL near 128, while Linux/Unix return near 64, accounting for hop decrements.

**Command** ([[commands/nmap-os-detection-and-service-scan]] is not used here; use standard ping):

```bash
ping -c 4 $_TARGET_IP
```

> This step sends four ping packets to the target IP. Analyze the TTL field in the response lines (e.g., "ttl=124" suggests Windows after ~4 hops; "ttl=52" suggests Linux/Unix). If no response, the target may block ICMP—proceed to active scanning.

### Step 2: Run Nmap OS Detection and Service Scan

**Context**: Use Nmap to actively fingerprint the OS via TCP/IP stack characteristics and enumerate open services for banner grabbing, providing both OS family and version clues.

**Command** ([[commands/nmap-os-detection-and-service-scan]]):

```bash
nmap -O -sV $_TARGET_IP
```

> This combines OS detection (-O) with service version scanning (-sV). Nmap probes ports, analyzes responses, and matches against its fingerprint database. Review the "Running:" and "OS details:" sections for OS identification (e.g., "Running: Linux 2.6.X"). Service banners (e.g., "OpenSSH 7.2p2 Ubuntu") offer additional versioning hints.

### Step 3: Enumerate and Correlate Service Banners with OSINT

**Context**: Extract version strings from service banners identified in Step 2, then search public sources to map them to specific OS releases. This refines broad OS detection to exact versions.

**Instructions**: From Nmap output, note banners (e.g., "Apache httpd 2.4.18 ((Ubuntu))" or "Microsoft IIS httpd 10.0"). Search queries like "Apache httpd 2.4.18 OS" on Google or sites like Launchpad.net/CVE databases. For Windows, reference IIS version histories on Wikipedia.

> No specific command here; manual OSINT. Expected: Confirmation of OS/version (e.g., Ubuntu 17.04 from Apache banner; Windows 10 from IIS 10.0).

### Step 4: Verify and Document Findings

**Context**: Cross-validate multiple indicators to increase accuracy, as single methods can be inaccurate or spoofed.

**Instructions**: Combine TTL, Nmap OS match, and banner-derived info. If discrepancies arise (e.g., TTL suggests Windows but Nmap says Linux), re-run with verbose flags (-v) or additional probes (-A for aggressive scan). Document the target's OS/version for use in targeted exploits.

> Success if consistent indicators point to a specific OS/version; otherwise, note uncertainties.

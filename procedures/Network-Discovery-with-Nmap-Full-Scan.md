---
id: fdbd2d83-7a46-4eab-944a-e76ca03e62ff
name: Network-Discovery-with-Nmap-Full-Scan
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.991137+00:00'
updated_at: '2023-04-10T20:25:08.706963+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
  - >-
    [[techniques/System Network Configuration Discovery|T1016 - System Network
    Configuration Discovery]]
sub_techniques: []
tags:
  - '[[tags/Network Discovery]]'
  - '[[tags/Nmap]]'
commands:
  - '[[commands/nmap-aggressive-scan]]'
platforms:
  - Linux
  - Windows
  - macOS
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Network-Discovery-with-Nmap-Full-Scan

## Summary

This procedure performs comprehensive network discovery using Nmap's aggressive scanning mode to identify active hosts, open ports, operating systems, service versions, and potential vulnerabilities through script scanning and traceroute. It is ideal for initial reconnaissance in red team engagements or penetration testing to map the attack surface.

## Description

Network discovery involves probing a target network to enumerate hosts, services, and configurations that could reveal entry points or weaknesses. Nmap's full scan (-A flag) combines host discovery, port scanning, OS fingerprinting, service version detection, NSE script execution for vulnerability checks, and traceroute for topology mapping. This technique is commonly used by attackers to gather intelligence on target environments, such as internal networks after initial access. The scan analyzes TCP/IP stack responses to infer OS details and probes services for version banners. In a defensive context, it helps security teams audit their own networks, but unauthorized use can trigger alerts in monitored environments. This procedure assumes the scanner has network access to the target range and focuses on IPv4 scanning; for larger networks, consider output formatting for analysis.

## Requirements

1. Network access to the target hosts or subnet (e.g., via VPN, direct connection, or compromised host).
2. Nmap installed on the attacking machine ([[tools/Nmap]]).
3. Sufficient privileges to send raw packets (root/admin on Unix/Windows).
4. Target hostname or IP range (e.g., a single host, CIDR block like 192.168.1.0/24).

## Defense

- Implement network segmentation and firewalls to restrict unauthorized scanning (e.g., rate-limit ICMP/TCP probes).
- Deploy intrusion detection systems (IDS) like Snort or Suricata to monitor for Nmap signatures (e.g., SYN scans, OS fingerprinting probes).
- Use honeypots to detect and divert reconnaissance attempts.
- Enable logging on network devices to track anomalous traffic patterns.

## Objectives

1. Discover active hosts and their basic network configuration.
2. Enumerate open ports, running services, and software versions for vulnerability assessment.
3. Identify operating systems and network topology to prioritize attack vectors.
4. Generate actionable output for further exploitation planning.

## Instructions

### Step 1: Verify Nmap Installation and Target Accessibility

**Context**: Ensure the tool is ready and basic connectivity exists to avoid false negatives. This step confirms prerequisites without performing the full scan.

Run a simple ping or host discovery to validate reachability.

**Command** ([[commands/nmap-host-discovery]]):
```bash
nmap -sn $_TARGET
```

> This performs a ping scan (-sn) to list active hosts without port scanning. Replace $_TARGET with the IP range (e.g., 192.168.1.0/24). Expected output: A list of up hosts like "Nmap scan report for 192.168.1.1" indicating MAC addresses and hostnames if resolved.

If no hosts respond, check firewall rules or network access.

### Step 2: Execute Aggressive Full Scan

**Context**: Launch the comprehensive scan to gather OS, version, script, and traceroute data. This is the core step that provides detailed reconnaissance.

Use the aggressive scan option for maximum information collection.

**Command** ([[commands/nmap-aggressive-scan]]):
```bash
nmap -A -T4 $_TARGET
```

> The -A flag enables OS detection (-O), version scanning (-sV), script scanning (-sC), and traceroute. -T4 sets aggressive timing for faster execution on responsive networks. $_TARGET is the host or range (e.g., scanme.nmap.org or 10.0.0.0/24). Run as root for best results. This may take several minutes per host depending on network latency.

Save output to a file for analysis: add -oN scan_results.txt.

### Step 3: Analyze and Verify Output

**Context**: Review results for key indicators of the target environment, such as vulnerable services or unusual ports. This ensures the scan data is usable.

Examine the output for OS fingerprints, service versions, and script results.

**Command** ([[commands/nmap-output-parse]]):
```bash
grep -E "open|OS details|NSE" scan_results.txt
```

> Pipe or grep the saved output to filter relevant sections. Expected: Lines showing open ports (e.g., "22/tcp open ssh"), OS guesses (e.g., "Running: Linux 4.X"), and script alerts (e.g., "VULNERABLE: Heartbleed").

If scripts detect vulnerabilities, note them for follow-up procedures like [[procedures/Service-Exploitation-Via-Known-Vulnerabilities]]. Decision point: If OS detection confidence is low (<90%), rerun with --osscan-guess.

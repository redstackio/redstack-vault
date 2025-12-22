---
id: 02af3d7c-4e91-4a51-b2ee-b02824d028fd
name: Basic-Nmap-Service-Version-Scan
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.964588+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Network Discovery]]'
  - '[[tags/Nmap]]'
commands:
  - '[[commands/nmap-service-version-scan-with-scripts]]'
platforms:
  - Linux
  - Network
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Basic-Nmap-Service-Version-Scan

## Summary

The Basic Nmap Service Version Scan procedure utilizes the Nmap tool to conduct network reconnaissance by identifying active hosts, open ports, running services, and their versions on a target network. This technique is essential in the initial discovery phase of an attack to map the network topology, pinpoint potential entry points, and gather intelligence for subsequent exploitation steps.

## Description

This procedure involves sending crafted packets to target hosts using Nmap's capabilities to elicit responses that reveal open ports and service details. It is typically employed during reconnaissance to understand the target's attack surface without causing disruption. The scan includes service version detection to identify software versions that may have known vulnerabilities and runs default Nmap Scripting Engine (NSE) scripts for additional insights like vulnerability checks or banner grabbing. Success provides a foundational map of the network, enabling attackers to prioritize targets based on exposed services. This aligns with passive and active scanning methods in offensive security operations, assuming the scanner has outbound network access but no prior credentials on the target.

## Requirements

1. Nmap tool installed on the attacker's system (version 7.0 or later recommended for full NSE support).
2. Network access to the target IP or range, including permission to send ICMP, TCP SYN, or UDP packets.
3. Sufficient privileges on the attacker's machine to run raw socket operations (may require root/sudo on Linux).
4. Optional: A wordlist or custom NSE scripts for enhanced detection, though defaults suffice for basic scans.

## Defense

- Deploy firewalls and intrusion detection systems (IDS) like Snort or Suricata to monitor and block unusual scanning patterns, such as rapid port probes or SYN floods.
- Implement network segmentation using VLANs or zero-trust architectures to limit lateral visibility and contain reconnaissance efforts.
- Enable logging on network devices and hosts to capture anomalous traffic, and use tools like Zeek for protocol analysis to detect Nmap signatures.
- Regularly update services to obscure version information and configure systems to ignore or rate-limit ICMP responses.

## Objectives

1. Discover active hosts and their responsiveness on the target network.
2. Enumerate open ports and identify associated services with version details.
3. Execute default NSE scripts to uncover additional vulnerabilities or configuration weaknesses.
4. Generate output files for offline analysis and further attack planning.

## Instructions

### Step 1: Verify Nmap Installation and Target Accessibility

**Context**: Before scanning, confirm Nmap is available and test basic connectivity to the target to ensure the network path is viable, avoiding wasted scans on unreachable hosts.

Run a simple ping or host discovery if needed, but for this procedure, use Nmap's built-in host discovery.

**Command** ([[commands/nmap-host-discovery]]):
```bash
nmap -sn $_TARGET_IP
```

> This command performs a ping scan (-sn) to check if the host is up without port scanning. Replace $_TARGET_IP with the target IP or range (e.g., 192.168.1.0/24). If the host responds, proceed; otherwise, investigate firewall blocks or routing issues.

**Expected Output**: A list of discovered hosts, e.g., "Nmap scan report for 192.168.1.1
Host is up (0.001s latency)." If no hosts are found, the scan may need adjustment for stealth or evasion.

### Step 2: Execute the Service Version Scan with Scripts

**Context**: This core step runs the full Nmap scan to probe open ports, detect services and versions, and apply default scripts for enriched data collection. It builds on host discovery to focus efforts efficiently.

**Command** ([[commands/nmap-service-version-scan-with-scripts]]):
```bash
nmap -sV -sC -oA ~/nmap-initial $_TARGET_IP
```

> The -sV flag enables service version probing, -sC runs the default set of NSE scripts (e.g., for HTTP title grabbing or SSH version detection), and -oA saves results in normal, XML, and grepable formats prefixed with "nmap-initial" in the home directory. This allows easy parsing and reporting. For larger networks, add --min-rate 1000 to speed up, but monitor for detection.

**Expected Output**: Detailed scan results showing ports, states, services, and script outputs, e.g.,:

Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-01 12:00 UTC
Nmap scan report for 192.168.1.1
Host is up (0.0012s latency).
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
|_ssh-hostkey: ssh-rsa AAAAB3NzaC1yc2E...
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Welcome to nginx!

Nmap done: 1 IP address (1 host up) scanned in 5.23 seconds

If services are detected, note versions for vulnerability research (e.g., via CVE databases).

### Step 3: Analyze and Follow Up with Full Port Scan if Needed

**Context**: Review the initial results for high-value targets, then optionally expand to all 65,535 ports if the default top 1,000 ports missed anything, balancing thoroughness with time and detection risk.

Examine the output files: ~/nmap-initial.nmap (human-readable), ~/nmap-initial.xml (for tools like Zenmap), ~/nmap-initial.gnmap (grepable).

If open ports beyond the top 1,000 are suspected, run an extended scan.

**Command** ([[commands/nmap-full-port-scan]]):
```bash
nmap -sV -sC -p- -oA ~/nmap-full $_TARGET_IP
```

> The -p- flag scans all ports. This takes longer (minutes to hours) but uncovers uncommon services. Use on confirmed live hosts only.

**Expected Output**: Similar to Step 2 but covering all ports, potentially revealing additional services like 8080 or 8443 for web apps.

**Success Indicators**:
- At least one host discovered and responsive.
- Open ports identified with service versions (e.g., vulnerable Apache 2.4.x).
- NSE scripts provide extra details without errors.
- Output files generated for documentation and chaining to next procedures like vulnerability scanning.

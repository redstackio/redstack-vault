---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.909410+00:00'
updated_at: '2023-04-10T20:25:09.453398+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Remote-System-Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Network Discovery]]'
  - '[[tags/Nmap]]'
commands:
  - '[[commands/nmap-host-discovery-scan]]'
platforms:
  - Linux
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Network-Host-Discovery-with-Nmap

## Summary

This procedure uses Nmap to perform host discovery on a target network, identifying live hosts without scanning for open ports or services. It is a foundational step in reconnaissance to map the active systems in a subnet, helping attackers identify potential targets for further enumeration and exploitation while minimizing detection through lightweight scanning.

## Description

Network host discovery is critical in offensive security operations to quickly identify which IP addresses in a given range are occupied by active devices. Nmap's host discovery mode sends probes such as ICMP echo requests or TCP SYN packets to determine host responsiveness without performing full port scans, reducing noise and execution time. This technique is particularly useful in internal network pivoting or external reconnaissance where broad IP ranges need to be assessed. The procedure focuses on disabling unnecessary features like ARP ping and DNS resolution to speed up scans and avoid potential logging triggers. Success provides a list of live hosts that can be targeted in subsequent procedures like port scanning or service enumeration. It maps to MITRE ATT&CK's Remote System Discovery technique, commonly used in the Discovery tactic during initial reconnaissance phases.

## Requirements

1. Attacker machine with network access to the target subnet (e.g., via VPN, compromised host, or direct connection).
2. Nmap installed on the attacker's system (version 7.0 or later recommended).
3. Administrative privileges on the attacker machine if raw socket operations are needed for certain probe types.
4. Knowledge of the target IP range (e.g., 192.168.1.0/24).

## Defense

- Implement network segmentation to limit the blast radius of scans and isolate critical assets.
- Deploy intrusion detection systems (IDS) like Snort or Suricata to monitor for anomalous ICMP, TCP SYN, or UDP traffic patterns indicative of host discovery.
- Enable firewall rules to rate-limit or block unsolicited probe traffic from unknown sources.
- Use endpoint detection tools to log and alert on unexpected network reconnaissance attempts.

## Objectives

1. Discover live hosts within a specified IP range to build a target inventory.
2. Minimize scan footprint by avoiding port scans and DNS lookups.
3. Filter output to focus only on responsive hosts for efficient follow-up actions.

## Instructions

### Step 1: Identify Target IP Range

**Context**: Determine the subnet or IP range to scan based on prior intelligence, such as network diagrams or previous access. This ensures the scan is targeted and avoids unnecessary traffic that could trigger alerts.

Choose a range like 192.168.1.1-254 for a /24 subnet. Verify your network position to ensure probes can reach the targets without routing issues.

### Step 2: Execute Host Discovery Scan

**Context**: Run the Nmap host discovery command to probe the network. This step uses ping-based discovery while disabling ARP (useful for non-local scans) and DNS resolution to keep the scan fast and stealthy. Pipe the output to grep to exclude down hosts immediately.

**Command** ([[commands/nmap-host-discovery-scan]]):
```bash
nmap -sn -n --disable-arp-ping $_IP_RANGE | grep -v "Host down"
```

> This command performs host discovery only (-sn), skips DNS resolution (-n), disables ARP ping for remote networks (--disable-arp-ping), and filters out non-responsive hosts. Replace $_IP_RANGE with your target, e.g., 192.168.1.1-254. Expected output includes a list of live hosts with their IP addresses and basic hostnames if any resolution occurs despite the -n flag.

### Step 3: Analyze and Verify Results

**Context**: Review the filtered output to confirm live hosts and prepare for next steps. This verification ensures the scan was effective and identifies any false positives from partial responses.

Save the output to a file for further processing: `nmap -sn -n --disable-arp-ping $_IP_RANGE | grep -v "Host down" > live_hosts.txt`. Manually check a few hosts with a simple ping to validate. If no hosts are found, adjust the range or probe types (e.g., add -PE for ICMP only).

> Success is indicated by a list of responsive IPs. If the scan returns empty, consider firewall blocks or incorrect range.

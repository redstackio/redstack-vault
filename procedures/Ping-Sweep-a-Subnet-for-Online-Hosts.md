---
id: 9c2e6154-9aa4-4d6c-a595-2561fbb9f561
name: Ping-Sweep-a-Subnet-for-Online-Hosts
type: procedure
verified: true
submitted: true
created_at: '2019-09-11T20:46:03.582746+00:00'
updated_at: '2023-05-26T00:51:50.193820+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/nmap-ping-sweep]]'
platforms:
  - Linux
  - Network
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Ping-Sweep-a-Subnet-for-Online-Hosts

## Summary

This procedure uses Nmap to perform a ping sweep on a specified subnet, identifying active hosts through ICMP echo requests and TCP/UDP probes to common ports. It is a foundational reconnaissance technique for discovering live systems in a network without conducting full port scans, helping to map the attack surface efficiently.

## Description

In offensive security operations, discovering remote systems is a critical first step in reconnaissance. This procedure leverages Nmap's host discovery capabilities to ping sweep a subnet, such as 10.10.10.0/24, by sending ICMP packets and probing popular ports like 80 and 443. This approach is stealthier than full scans as it avoids aggressive port enumeration. It maps directly to MITRE ATT&CK technique T1018 (Remote System Discovery) under the Discovery tactic, commonly used in red team engagements to identify potential targets for further enumeration. The procedure assumes the attacker has network access to the target subnet and is not firewalled from ICMP traffic.

## Requirements

1. Nmap tool installed on the attacker's machine (version 7.0 or higher recommended).
2. Network connectivity to the target subnet, including permission to send ICMP echo requests.
3. Basic knowledge of CIDR notation for specifying the subnet (e.g., /24 for a Class C network).
4. No administrative privileges required on the target, but firewall rules on the attacker's side should allow outbound ICMP.

## Defense

Defensive measures include configuring firewalls to block ICMP echo requests (e.g., using iptables rules to drop ping traffic), enabling host-based firewalls on endpoints to ignore discovery probes, and monitoring network traffic for unusual ICMP or port probe patterns using tools like Snort or Suricata. Intrusion detection systems can alert on high volumes of host discovery attempts from unknown sources.

## Objectives

1. Identify all active hosts within the specified subnet to build a network map.
2. Determine host responsiveness without revealing detailed service information.
3. Provide a list of IP addresses for subsequent targeted reconnaissance or scanning.
4. Minimize detection risk by using lightweight discovery methods.

## Instructions

### Step 1: Verify Nmap Installation and Target Subnet

**Context**: Before executing the sweep, confirm Nmap is available and identify the target subnet to ensure accurate scoping. This prevents errors from incorrect CIDR notation or missing tools.

Run a version check using Nmap's built-in command:

**Command** ([[commands/nmap-version-check]]):
```bash
nmap --version
```

> This command displays the installed Nmap version and confirms the tool is operational. If not installed, refer to the [[tools/Nmap]] installation guide.

Expected output includes the Nmap version (e.g., "Nmap version 7.94 ( https://nmap.org )").

### Step 2: Execute the Ping Sweep

**Context**: Perform the actual host discovery by running Nmap with the -sn flag, which disables port scanning and focuses on host detection via ping and port probes. Specify the target as the base IP and CIDR mask.

**Command** ([[commands/nmap-ping-sweep]]):
```bash
nmap -sn $_TARGET_SUBNET/$_CIDR
```

> Replace $_TARGET_SUBNET with the base IP (e.g., 10.10.10.0) and $_CIDR with the mask (e.g., 24). This sends ICMP echo requests and probes common ports to determine host liveness. The -sn option ensures no ports are scanned, keeping the operation quick and low-profile.

### Step 3: Analyze and Save Results

**Context**: Review the output to identify live hosts and save the results for further use, such as feeding into subsequent tools like masscan or targeted Nmap scans. This step verifies success and prepares data for chaining procedures.

Use grep or manual inspection on the output to filter live hosts:

**Command** ([[commands/grep-live-hosts]]):
```bash
nmap -sn $_TARGET_SUBNET/$_CIDR | grep "Nmap scan report" > live_hosts.txt
```

> This pipes the Nmap output to grep, capturing lines with scan reports (indicating live hosts), and redirects to a file. Open live_hosts.txt to list IPs like "Nmap scan report for 10.10.10.1".

Expected output: A file containing IP addresses of responsive hosts with latency information.

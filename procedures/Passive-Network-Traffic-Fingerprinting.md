---
id: f3302b27-d0ce-4038-9595-768e2f3012fa
name: Passive-Network-Traffic-Fingerprinting
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T18:07:35.334769+00:00'
updated_at: '2023-05-26T00:51:21.284862+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Sniffing|T1040 - Network Sniffing]]'
sub_techniques: []
tags:
  - '[[tags/data exposure]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/p0f-passive-fingerprinting]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/p0f]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Passive-Network-Traffic-Fingerprinting

## Summary

This procedure uses passive network traffic analysis to fingerprint devices and services on a network without sending any packets that could alert intrusion detection systems. It leverages tools like p0f to identify operating systems, applications, and device characteristics based on observed TCP/IP stack behaviors, making it ideal for stealthy reconnaissance in red team engagements or network mapping.

## Description

Passive network traffic fingerprinting involves monitoring and analyzing existing network traffic to infer details about connected hosts and services. Unlike active scanning, which probes targets and risks detection, this method observes natural communication patterns, such as TCP SYN packets, TTL values, and window sizes, to build a profile of the network environment. It is particularly useful in scenarios where the attacker has compromised a network segment (e.g., via man-in-the-middle or lateral movement) and needs to map the infrastructure quietly. The technique aligns with MITRE ATT&CK's Network Sniffing (T1040) under Discovery and Credential Access tactics, as it can reveal sensitive communication patterns or aid in identifying high-value targets for further exploitation. Expected outcomes include a log of fingerprinted hosts with OS versions, application details, and connection parameters.

## Requirements

1. Administrative privileges on the monitoring host to access network interfaces in promiscuous mode.
2. Network access to the interface carrying the target traffic (e.g., via compromised host or ARP poisoning for lateral visibility).
3. p0f tool installed ([[tools/p0f]]).
4. A quiet network environment or filtered capture to focus on relevant traffic; high-volume networks may require additional filtering tools like tcpdump.

## Defense

Defensive measures and detection strategies:

- Enable network segmentation and micro-segmentation to limit visibility into traffic.
- Deploy encrypted protocols (e.g., TLS 1.3) to obscure fingerprintable packet details.
- Monitor for unusual promiscuous mode usage on interfaces using tools like auditd or Windows Event Logs (Event ID 4688 for process creation).
- Use anomaly detection in NIDS/IDS (e.g., Snort rules for p0f signatures) to flag passive monitoring tools.
- Implement endpoint detection for unauthorized packet capture libraries (e.g., libpcap).

## Objectives

1. Identify operating systems and device types on the network without active probing.
2. Enumerate running services and applications based on traffic signatures.
3. Generate a log for further analysis to support targeted attacks, such as identifying vulnerable hosts.
4. Maintain operational stealth by avoiding any generated traffic.

## Instructions

### Step 1: Identify Monitoring Interface

**Context**: Determine the network interface to monitor, as this ensures you're capturing traffic from the desired segment. Use tools like ip link or ifconfig to list interfaces; select one with visibility into target traffic (e.g., eth0 for wired, wlan0 for wireless).

**Command** ([[commands/list-network-interfaces]]):
```bash
ip link show
```

> This command lists all network interfaces. Look for the one connected to the monitored network. Expected output includes interface names, states (UP/DOWN), and MTU sizes. If on Windows, use `ipconfig` instead.

### Step 2: Configure Promiscuous Mode and Run p0f

**Context**: Launch p0f in promiscuous mode to capture all traffic on the interface and output fingerprints to a log file. Promiscuous mode (-p) allows seeing traffic not destined for the host, essential for full visibility. The tool loads signature files to match observed packets against known OS/app behaviors.

**Command** ([[commands/p0f-passive-fingerprinting]]):
```bash
p0f -i $_INTERFACE -p -o $_OUTPUT.log
```

> Replace $_INTERFACE with your selected interface (e.g., eth0) and $_OUTPUT.log with a file path (e.g., fingerprints.log). Run as root/sudo for interface access. Expected output on console shows initialization (loaded signatures, interface bound), followed by real-time fingerprints like client IP, app type (e.g., NMap SYN scan), and raw signatures. Let it run for sufficient time to capture meaningful traffic; Ctrl+C to stop.

### Step 3: Analyze Output Log

**Context**: Review the generated log file to extract actionable intelligence, such as host OS versions or unusual scan activity. Use grep or text editors to filter entries by IP or signature.

**Command** ([[commands/analyze-p0f-log]]):
```bash
grep "client" $_OUTPUT.log | sort -u
```

> This extracts unique client fingerprints. Expected output: Lines showing client IPs, apps, distances, and parameters. Cross-reference with network maps to prioritize targets (e.g., Windows servers for lateral movement).

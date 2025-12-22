---
id: e53ef3f3-7e8e-4364-8680-2b820d4b178f
name: Capture-Network-Packets-with-Meterpreter
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.433515+00:00'
updated_at: '2023-04-10T20:24:58.736284+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Sniffing|T1040 - Network Sniffing]]'
sub_techniques: []
tags:
  - '[[tags/metasploit]]'
  - '[[tags/meterpreter-basic]]'
  - '[[tags/network-monitoring]]'
commands:
  - '[[commands/meterpreter-packetrecorder-list-interfaces]]'
  - '[[commands/meterpreter-packetrecorder-record-packets]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Metasploit]]'
validated: true
---

# Capture-Network-Packets-with-Meterpreter

## Summary

This procedure uses Meterpreter's packetrecorder post module to capture network traffic on a compromised target, enabling attackers to sniff packets for reconnaissance, credential harvesting, or man-in-the-middle attacks. It involves listing available network interfaces and then recording packets from a selected interface, storing the capture in a PCAP file for later analysis.

## Description

In a post-exploitation scenario, after gaining a Meterpreter session on a target machine with network access, this procedure allows capturing raw network packets to discover hosts, services, topology, or sensitive data like credentials transmitted in cleartext. The packetrecorder module leverages the target's network stack to perform sniffing without additional tools, making it stealthy for lateral movement or data collection phases. It maps to MITRE ATT&CK technique T1040 for network sniffing under Discovery and Credential Access tactics, useful in environments where traffic is unencrypted (e.g., HTTP, Telnet). Prerequisites include an active Meterpreter session via Metasploit, and the target must have promiscuous mode support on the interface if needed for full capture.

## Requirements

1. Active Meterpreter session on the target machine (established via exploit or payload delivery).
2. Target machine with network interface access (e.g., Ethernet or Wi-Fi adapter).
3. Metasploit Framework running on the attacker's machine to manage the session.
4. Sufficient privileges on the target for packet capture (typically administrator/root level).

## Defense

Defensive measures and detection strategies:

- Implement network segmentation to isolate sensitive systems and limit lateral traffic visibility.
- Enforce encrypted protocols (e.g., HTTPS, SSH) to protect data in transit from sniffing.
- Monitor for anomalous network activity, such as unexpected packet capture processes or high I/O on network interfaces using tools like Wireshark on endpoints or IDS like Snort.
- Enable endpoint detection and response (EDR) solutions to flag Meterpreter-like behaviors, including suspicious module loads in Metasploit payloads.

## Objectives

1. List available network interfaces for selection.
2. Capture packets on the target network to identify hosts, services, and topology.
3. Harvest sensitive information such as credentials from unencrypted traffic.
4. Enable man-in-the-middle attacks by analyzing captured data for further exploitation.

## Instructions

### Step 1: List Available Network Interfaces

**Context**: Begin by enumerating the network interfaces on the target to identify which one to capture from. This step ensures you select the correct interface connected to the desired network segment, avoiding irrelevant local loopback traffic.

**Command** ([[commands/meterpreter-packetrecorder-list-interfaces]]):
```bash
run packetrecorder -li
```

> This command queries the target's network stack and displays a numbered list of interfaces with details like names and IP configurations. Review the output to choose an interface with active traffic, such as the primary Ethernet adapter. If no interfaces appear, verify the Meterpreter session privileges and network connectivity.

### Step 2: Record Packets on Selected Interface

**Context**: Once an interface is identified, initiate packet capture on it to record traffic. This step starts the sniffing process, saving packets to a PCAP file in the loot directory of the Metasploit session for offline analysis with tools like Wireshark. Stop the capture manually when sufficient data is collected or to avoid detection.

**Command** ([[commands/meterpreter-packetrecorder-record-packets]]):
```bash
run packetrecorder -i $_INTERFACE_ID -o captured_traffic.pcap
```

> Replace $_INTERFACE_ID with the number from Step 1 (e.g., 1 for eth0). The optional -o flag specifies the output filename; without it, a default is used. The command runs continuously until interrupted (e.g., Ctrl+C in the Meterpreter console). Monitor for errors like permission denied, which indicate insufficient privileges. After stopping, download the PCAP file using Meterpreter's download command for analysis.

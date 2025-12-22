---
id: 1916ed79-da75-416f-a25b-849b2a80bc64
name: Netdiscover-Network-Discovery
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.247259+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Netdiscover]]'
  - '[[tags/Network Discovery]]'
commands:
  - '[[commands/netdiscover-scan-hosts-in-range]]'
platforms:
  - Linux
tools:
  - '[[tools/Netdiscover]]'
validated: true
---

# Netdiscover-Network-Discovery

## Summary

Netdiscover-Network-Discovery is a procedure that utilizes the Netdiscover tool to perform active network scanning via ARP requests, identifying live hosts on a local network along with their IP addresses, MAC addresses, and vendor information. This technique is commonly used in offensive security to map network topology and enumerate potential targets, while defenders can apply it to detect unauthorized devices.

## Description

Netdiscover operates by sending ARP (Address Resolution Protocol) packets to a specified IP range on a chosen network interface, listening for responses from active hosts. This allows for passive and active discovery modes, but the standard usage focuses on active scanning to quickly identify devices. In an attack scenario, an adversary with network access can use this to footprint the environment, discover hosts for further reconnaissance or targeting. Defensively, security teams can run periodic scans to baseline the network and alert on anomalies like rogue devices. The procedure requires local network access and is most effective on Layer 2 networks where ARP is relevant. It maps directly to MITRE ATT&CK's Network Service Scanning technique under the Discovery tactic, as it reveals active network services and hosts without deeper port probing.

## Requirements

1. Local access to the target network (e.g., via compromised host or authorized testing machine).
2. Administrative privileges on the scanning system to install and run Netdiscover.
3. Netdiscover tool installed (see [[tools/Netdiscover]] for installation details).
4. Knowledge of the network interface (e.g., eth0) and IP range to scan (e.g., 192.168.1.0/24).

## Defense

- Implement network access controls (NAC) to restrict unauthorized devices and monitor ARP traffic for anomalies.
- Use intrusion detection systems (IDS) to flag unusual ARP requests or scanning patterns.
- Segment networks with VLANs or firewalls to limit the scope of discovery attempts.
- Enable ARP spoofing detection features on switches and monitor for duplicate MAC/IP bindings.

## Objectives

1. Discover all live hosts on the local network segment.
2. Enumerate IP and MAC addresses to map network topology.
3. Identify device vendors for targeted exploitation or anomaly detection.

## Instructions

### Step 1: Identify Network Interface and Range

**Context**: Before scanning, determine the appropriate network interface and IP range. Use `ip link show` or `ifconfig` to list interfaces, and identify the subnet (e.g., via `ip route`).

This step ensures the scan targets the correct local network without affecting others.

### Step 2: Execute Network Scan

**Context**: Run Netdiscover to send ARP requests and capture responses, revealing active hosts.

**Command** ([[commands/netdiscover-scan-hosts-in-range]]):
```bash
netdiscover -i $_INTERFACE -r $_IP_RANGE
```

> This command actively scans the specified IP range on the given interface. The `-i` flag selects the interface (e.g., eth0), and `-r` defines the range (e.g., 192.168.1.0/24). It displays real-time output of discovered hosts. Run as root for full packet capture capabilities. If no responses appear, verify interface and range; consider passive mode with `-p` for quieter scanning.

**Expected Output**: A table of discovered hosts showing IP, MAC, packet count, length, and vendor:

```
Currently scanning: Finished!   |   Screen View: Unique Hosts

20 Captured ARP Req/Rep packets, from 4 hosts.   Total size: 876
_____________________________________________________________________________
IP            At MAC Address     Count     Len  MAC Vendor / Hostname
-----------------------------------------------------------------------------
192.168.1.AA    68:AA:AA:AA:AA:AA     15     630  Sagemcom
192.168.1.XX    52:XX:XX:XX:XX:XX      1      60  Unknown vendor
192.168.1.YY    24:YY:YY:YY:YY:YY      1      60  QNAP Systems, Inc.
192.168.1.ZZ    b8:ZZ:ZZ:ZZ:ZZ:ZZ      3     126  HUAWEI TECHNOLOGIES CO.,LTD  
```

### Step 3: Analyze and Verify Results

**Context**: Review the output for unexpected devices. Cross-reference MAC vendors against known assets.

If needed, export results (Netdiscover supports `-o` for output file in some modes) or follow up with tools like Nmap for deeper enumeration.

**Success Indicators**:
- At least the scanning host and known devices appear in output.
- No errors like "interface not found" or permission denied.

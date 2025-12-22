---
id: b20ac768-9d0d-468f-bede-789108368493
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.200662Z'
updated_at: '2023-04-10T20:25:05.850867Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Masscan]]'
  - '[[tags/Network Discovery]]'
  - scanning
  - reconnaissance
commands:
  - '[[commands/masscan-discover-network-machines]]'
  - '[[commands/extract-machines-from-masscan-output]]'
  - '[[commands/masscan-scan-ports-on-machine]]'
  - '[[commands/nmap-enumerate-tcp-services]]'
  - '[[commands/nmap-enumerate-udp-services]]'
platforms:
  - Linux
tools:
  - '[[tools/masscan]]'
  - '[[tools/Nmap]]'
validated: true
---

# Network-Discovery-with-Masscan

## Summary

This procedure uses Masscan, a high-speed port scanner, to perform network discovery by identifying active hosts and open ports on a target network. It then leverages Nmap for detailed service enumeration on discovered hosts, providing attackers with insights into potential entry points, running services, and vulnerabilities for further exploitation in reconnaissance phases.

## Description

Network discovery with Masscan is a reconnaissance technique ideal for large-scale network scanning where speed is critical. Masscan operates by sending TCP SYN packets at high rates to detect open ports across IP ranges, making it suitable for scanning entire subnets or enterprise networks quickly. Once hosts and ports are identified, Nmap performs deeper analysis, including service version detection and script-based vulnerability checks. This approach is commonly used in red team engagements to map the attack surface without alerting defenders prematurely due to Masscan's stealthy, low-interaction nature. The procedure assumes the attacker has network access, such as via a compromised host or VPN, and requires root privileges for raw socket operations. Expected outcomes include lists of live hosts, open TCP/UDP ports, and service banners that can inform targeted attacks like service exploitation or lateral movement.

## Requirements

1. Network access to the target subnet (e.g., via compromised host, VPN, or direct connection).
2. Masscan and Nmap tools installed on a Linux-based attack platform (Kali Linux recommended).
3. Root or sudo privileges to bind to raw sockets for scanning.
4. A tun/tap interface configured if scanning routed networks (e.g., in lab environments like HackTheBox).
5. Output directories created for scan results (e.g., mkdir -p $MACHINE_IP/scans).

## Defense

- Close unnecessary ports and services on hosts to reduce the attack surface.
- Implement network segmentation with firewalls to limit scanner reach to critical systems.
- Deploy intrusion detection systems (IDS) like Snort or Suricata to monitor for high-volume SYN scans and anomalous traffic patterns.
- Use rate-limiting on edge devices and enable logging for unusual port probes.

## Objectives

1. Discover active hosts within the target network.
2. Identify open TCP and UDP ports on discovered hosts.
3. Enumerate services, versions, and potential vulnerabilities for attack planning.
4. Generate actionable intelligence for subsequent exploitation steps.

## Instructions

### Step 1: Discover Active Machines on the Network

**Context**: Use Masscan to quickly scan the target network for live hosts by probing common ports. This step identifies potential targets without full port scans initially.

**Command** ([[commands/masscan-discover-network-machines]]):
```bash
sudo masscan --rate 500 --interface tap0 --router-ip $_ROUTER_IP --top-ports 100 $_NETWORK -oL masscan_machines.tmp
```

Run this command to output open ports in list format to a temporary file. The --top-ports 100 flag focuses on the 100 most common ports for efficiency. Expected output is a file with lines indicating open ports per IP.

### Step 2: Extract Unique Machine List

**Context**: Process the Masscan output to create a clean list of unique active IP addresses, filtering for confirmed open ports to focus on viable targets.

**Command** ([[commands/extract-machines-from-masscan-output]]):
```bash
cat masscan_machines.tmp | grep open | cut -d " " -f4 | sort -u > masscan_machines.lst
```

This bash one-liner parses the output, extracts IP addresses from lines with 'open' status, removes duplicates, and saves to a list file. Verify by checking the file contents with `cat masscan_machines.lst`; it should list unique IPs.

### Step 3: Scan Open Ports on a Specific Machine

**Context**: For a selected target machine (e.g., from the list), perform a comprehensive port scan including banners to identify all open TCP/UDP ports.

**Command** ([[commands/masscan-scan-ports-on-machine]]):
```bash
sudo masscan --rate 1000 --interface tap0 --router-ip $_ROUTER_IP -p1-65535,U:1-65535 $_MACHINE_IP --banners -oL $_MACHINE_IP/scans/masscan-ports.lst
```

This scans the full port range (1-65535 for TCP, UDP specified with U:). The --banners flag attempts to grab initial service banners. Output is a list file in the machine's scans directory. Success is confirmed by the presence of 'open' lines in the file.

### Step 4: Enumerate TCP Services with Nmap

**Context**: Use the open TCP ports from Masscan to run Nmap for detailed service detection, version identification, and default script execution to uncover vulnerabilities.

**Context**: First, extract TCP ports from the Masscan output.

**Command** ([[commands/nmap-enumerate-tcp-services]]):
```bash
TCP_PORTS=$(cat $_MACHINE_IP/scans/masscan-ports.lst | grep open | grep tcp | cut -d " " -f3 | tr '\n' ',' | head -c -1)
[ "$TCP_PORTS" ] && sudo nmap -sT -sC -sV -v -Pn -n -T4 -p$TCP_PORTS --reason --version-intensity=5 -oA $_MACHINE_IP/scans/nmap_tcp $_MACHINE_IP
```

If TCP ports are found, Nmap performs a TCP connect scan (-sT) with version detection (-sV), default scripts (-sC), and high verbosity. Output files (.nmap, .gnmap, .xml) are saved in the scans directory. Expected output includes service versions like '22/tcp open ssh OpenSSH 7.6p1'.

### Step 5: Enumerate UDP Services with Nmap

**Context**: Similarly, scan open UDP ports for service details, which is useful for discovering less common protocols like DNS or SNMP.

**Command** ([[commands/nmap-enumerate-udp-services]]):
```bash
UDP_PORTS=$(cat $_MACHINE_IP/scans/masscan-ports.lst | grep open | grep udp | cut -d " " -f3 | tr '\n' ',' | head -c -1)
[ "$UDP_PORTS" ] && sudo nmap -sU -sC -sV -v -Pn -n -T4 -p$UDP_PORTS --reason --version-intensity=5 -oA $_MACHINE_IP/scans/nmap_udp $_MACHINE_IP
```

This mirrors the TCP step but uses UDP scan (-sU). Note that UDP scanning is slower and may produce false negatives due to no-response behavior. Review output files for UDP service details.

---
id: 881bce42-157a-4a0d-9e98-83b4d20a8986
name: scan-ports-for-services-without-host-discovery
type: procedure
verified: true
submitted: false
created_at: '2019-09-12T18:53:18.223938+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - enumeration
  - network
commands:
  - '[[commands/nmap-service-scan-without-host-discovery]]'
platforms:
  - Linux
  - Network
tools: []
validated: true
---

# Scan Ports for Services Without Host Discovery

## Summary

This procedure performs a service enumeration scan on a target host using Nmap, bypassing host discovery to handle cases where the target does not respond to ICMP ping requests. It identifies open ports, running services, and their versions, providing critical reconnaissance data for identifying potential vulnerabilities without alerting basic host detection mechanisms.

## Description

During network reconnaissance, many production environments configure firewalls or hosts to ignore ICMP echo requests (pings) to reduce visibility. This procedure uses Nmap's -Pn flag to skip the host discovery phase and assume the target is up, proceeding directly to port scanning and service version detection with -sV. This approach is particularly useful in stealthy operations or when dealing with firewalled networks. It maps to the MITRE ATT&CK Discovery tactic (TA0007) and the Network Service Scanning technique (T1046), as it systematically probes for exposed services that could serve as entry points for further attacks. The scan typically targets the top 1000 TCP ports by default but can be customized for specific ranges.

## Requirements

1. Nmap tool installed on a Linux-based attacking machine (e.g., Kali Linux).
2. Network connectivity to the target IP address, potentially through a pivot or direct access.
3. Administrative privileges on the attacking machine to run Nmap (non-root scans may be limited).
4. Knowledge of the target's IP address or hostname.

## Defense

Defensive measures and detection strategies:

- Deploy network intrusion detection systems (NIDS) like Snort or Suricata to alert on unusual port scan patterns, even without ICMP responses.
- Use host-based firewalls (e.g., iptables, Windows Firewall) to restrict service exposure and log scan attempts.
- Implement application-layer monitoring to detect anomalous service probes, such as unexpected version detection requests.
- Enable logging of SYN packets and half-open connections to identify -Pn scans.

## Objectives

1. Enumerate open TCP ports on the target without triggering host discovery.
2. Identify service types and versions for vulnerability research and exploitation planning.
3. Collect banner information to map the target's attack surface efficiently.

## Instructions

### Step 1: Verify Nmap Installation and Target Accessibility

**Context**: Before scanning, confirm Nmap is installed and test basic network reachability to the target (e.g., via traceroute or a simple TCP connect if possible). This ensures the scan will proceed without environmental issues and helps validate the need for -Pn (e.g., if ping fails).

Run a quick ping test to confirm non-responsiveness:

```bash
ping -c 3 $_TARGET_IP
```

> If no response, proceed to the scan. This step confirms the prerequisite for skipping host discovery.

**Expected Output**: No ICMP replies, indicating the need for -Pn.

### Step 2: Execute the Service Version Scan

**Context**: Launch the Nmap scan to probe ports and detect services. The -sV option sends additional probes to open ports to gather version and banner details, which can reveal software versions vulnerable to known exploits. This is the core action of the procedure.

**Command** ([[commands/nmap-service-scan-without-host-discovery]]):

```bash
nmap -sV -Pn $_TARGET_IP
```

> This invokes Nmap in its default SYN scan mode, skipping ping (-Pn), and enabling service detection (-sV). Replace $_TARGET_IP with the actual target (e.g., 10.10.10.10). For verbose output, add -v; to scan specific ports, include -p (e.g., -p 21,22,80).

**Expected Output**: A report listing open ports, services, and versions, such as:

```
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:52 EDT
Nmap scan report for 10.10.10.10
Host is up (0.0017s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
MAC Address: 00:0C:29:66:97:CB (VMware)
Service Info: Hosts:  host.localdomain, irc.host.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.72 seconds
```

### Step 3: Analyze and Document Results

**Context**: Parse the output to identify high-value services (e.g., outdated FTP or HTTP versions). Use tools like grep to filter results for specific services, and document findings for chaining into further procedures like vulnerability scanning.

Example filtering command (not linked as a formal command):

```bash
nmap -sV -Pn $_TARGET_IP | grep "open"
```

> This extracts lines showing open ports and services. If a service like vsftpd 2.3.4 is found, research CVEs (e.g., backdoor vulnerabilities) for exploitation.

**Expected Output**: Filtered list of open services, e.g., "21/tcp open ftp vsftpd 2.3.4".

**Success Indicators**:
- Scan completes without errors and reports at least one open port.
- Service versions are detected, providing actionable intelligence.
- No host discovery failures; all probed ports are evaluated.

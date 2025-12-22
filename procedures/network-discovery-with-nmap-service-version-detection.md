---
id: 1973b52d-79ba-48d9-8e67-85234a505dca
name: network-discovery-with-nmap-service-version-detection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.040013+00:00'
updated_at: '2023-05-26T00:58:41.239584+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - network-discovery
  - nmap
commands:
  - '[[commands/nmap-service-version-scan-with-report-generation]]'
platforms:
  - Linux
  - Network
tools:
  - '[[tools/Nmap]]'
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# network-discovery-with-nmap-service-version-detection

## Summary

This procedure uses Nmap to perform network discovery by identifying active hosts, open ports, and the versions of services running on those ports. It maps the network topology to reveal potential entry points for attacks, such as vulnerable services, and generates an HTML report for analysis.

## Description

Network discovery with Nmap service version detection involves scanning a target network or IP range to detect live hosts, enumerate open ports, and probe for service details including exact versions. Attackers use this to understand the environment, identify exploitable services (e.g., outdated software with known CVEs), and plan further actions like targeted exploitation. Nmap employs techniques like TCP SYN scans for stealthy port detection and version probes to fingerprint services without full connections. The output can be saved in XML format and converted to an HTML report for easier review. This is particularly useful in reconnaissance phases of red team engagements or penetration tests. From a defensive standpoint, it highlights the business value in proactive scanning to close unnecessary ports and patch services before adversaries do the same.

## Requirements

1. Network access to the target IP range or hosts (e.g., from an internal position or via VPN).
2. Administrative privileges on the scanning machine if raw sockets are needed for advanced scans.
3. Nmap and xsltproc installed on the scanning machine (xsltproc for XML to HTML conversion).
4. Permission to scan the target network to avoid legal issues.

## Defense

Defensive measures and detection strategies:

- Implement network segmentation to limit visibility and reduce the attack surface for scanners.
- Deploy firewalls and intrusion detection systems (IDS) like Snort or Suricata to block or alert on suspicious scan patterns (e.g., SYN floods or version probes).
- Regularly perform your own vulnerability scans with tools like Nmap or OpenVAS to identify and remediate open ports and outdated services.
- Monitor network traffic for anomalous patterns, such as high volumes of SYN packets or connections to uncommon ports.

## Objectives

1. Identify active hosts on the target network.
2. Enumerate open ports and the services running on them.
3. Determine the exact versions of services to assess for known vulnerabilities.
4. Generate a readable HTML report of the scan results for analysis.

## Instructions

### Step 1: Execute Nmap Service Version Scan and Generate Report

**Context**: This step performs the core discovery by scanning the target for hosts, ports, and service versions, saving results in XML, and converting to an HTML report with a timestamped filename. It combines host discovery, port scanning, and version detection in one operation for efficiency.

**Command** ([[commands/nmap-service-version-scan-with-report-generation]]):

```bash
nmap -sV $_TARGET_IP -oX scan.xml && xsltproc scan.xml -o "`date +%m%d%y`_report.html"
```

> The Nmap command with -sV enables service version detection, probing open ports for detailed service information. -oX outputs in XML format to scan.xml for further processing. The chained xsltproc command transforms the XML into a human-readable HTML report, appending the current date (MMDDYY format) to the filename. Run this from a Kali Linux or similar environment with network access to the target. If scanning a range, use CIDR notation like 192.168.1.0/24 for $_TARGET_IP.

**Expected Output**: Nmap will display real-time scan progress on the console, followed by a summary of discovered hosts, open ports, and service versions. The HTML file (e.g., 052623_report.html) will open in a browser showing a formatted table of results, including host details, port states, and service banners.

Sample console output:

Starting Nmap 7.94 ( https://nmap.org ) at 2023-05-26 00:00 UTC
Nmap scan report for 192.168.1.100
Host is up (0.0012s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http     Apache httpd 2.4.41 ((Ubuntu))
Nmap done: 1 IP address (1 host up) scanned in 5.23 seconds

**Success Indicators**:
- Console shows discovered open ports with service versions.
- XML file (scan.xml) is created and non-empty.
- HTML report file is generated and viewable in a browser without errors.

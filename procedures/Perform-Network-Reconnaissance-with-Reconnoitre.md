---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Network Discovery]]'
  - '[[tags/Reconnoitre]]'
commands:
  - '[[commands/install-reconnoitre]]'
  - '[[commands/run-reconnoitre-scan]]'
platforms:
  - Linux
tools:
  - '[[tools/Reconnoitre]]'
verified: true
validated: true
---

# Perform-Network-Reconnaissance-with-Reconnoitre

## Summary

This procedure uses the Reconnoitre tool to perform active network reconnaissance on a target IP range, discovering live hosts, resolving hostnames, and enumerating services to map the network and identify potential entry points for further attacks.

## Description

Network reconnaissance is a critical initial phase in penetration testing and red team operations, aimed at gathering intelligence on the target's infrastructure without causing disruption. This procedure focuses on active scanning using Reconnoitre, a Python-based tool that automates host discovery via ping sweeps, DNS resolution for hostnames, and service detection on common ports. It is particularly useful in internal network assessments where the attacker has initial network access, such as after pivoting from a compromised host. The output provides a structured report of active hosts and services, which can inform subsequent steps like vulnerability scanning or exploitation. This aligns with discovery tactics in adversarial simulations, helping to build a comprehensive network map while minimizing detection through quick scan options.

## Requirements

1. Network access to the target range (e.g., via VPN, compromised host, or direct connectivity).
2. Python 2.7 installed on the attacker's system.
3. Git for cloning the Reconnoitre repository.
4. Administrative privileges on the attacker's machine for tool installation.
5. Sufficient disk space for output reports (typically under 100MB for small ranges).

## Defense

Defensive measures and detection strategies:

- Implement network segmentation to limit reconnaissance scope and isolate critical assets.
- Deploy intrusion detection systems (IDS) like Snort or Suricata to monitor for anomalous scanning traffic, such as ICMP pings or SYN scans on multiple ports.
- Use firewalls to block unauthorized scanning attempts and enable logging for tools like Nmap or custom scripts.
- Regularly update and patch network devices to reduce exposed services identifiable via enumeration.
- Monitor DNS query volumes for unusual resolution patterns indicative of hostname enumeration.

## Objectives

1. Discover live hosts within the target IP range through ping sweeps.
2. Resolve hostnames for identified hosts to understand network topology.
3. Enumerate running services on common ports to identify potential vulnerabilities.
4. Generate a report for planning targeted exploitation or deeper reconnaissance.

## Instructions

### Step 1: Install Reconnoitre

**Context**: Before scanning, install the Reconnoitre tool by cloning its repository and setting up dependencies. This ensures the script is available and functional on your system.

**Command** ([[commands/install-reconnoitre]]):
```bash
git clone https://github.com/nccgroup/reconnoitre.git && cd reconnoitre && pip2 install -r requirements.txt
```

> This command clones the Reconnoitre repository from GitHub and installs required Python 2.7 dependencies using pip. Expected output includes successful clone messages and dependency installation logs without errors. Verify by checking that reconnoitre.py exists in the directory.

### Step 2: Prepare Output Directory

**Context**: Create a dedicated directory for scan results to organize outputs like host lists, service reports, and screenshots if enabled.

**Command**:
```bash
mkdir -p ./results/
```

> This mkdir command creates the results folder if it doesn't exist. Expected output is no error message, confirming the directory is ready for use. This step ensures clean organization of reconnaissance data.

### Step 3: Execute Network Scan

**Context**: Run the Reconnoitre scan on the target IP range, performing ping sweeps, hostname resolution, and service detection. Use the --quick flag to reduce scan time by limiting port checks.

**Command** ([[commands/run-reconnoitre-scan]]):
```bash
python2.7 ./reconnoitre.py -t 192.168.1.2-252 -o ./results/ --pingsweep --hostnames --services --quick
```

> This invokes Reconnoitre to scan the specified IP range (adjust as needed). It performs a ping sweep to find live hosts, resolves hostnames via DNS, and detects services on standard ports. Expected output includes progress logs, a summary of discovered hosts (e.g., "Found 50 live hosts"), and files in ./results/ such as hosts.csv, services.json, and screenshots if configured. Success is indicated by non-zero host discoveries and no connection timeouts.

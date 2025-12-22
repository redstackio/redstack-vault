---
id: 3bd393e7-f61b-4b8c-9894-fe7e9df6c95e
name: Enumerate-Domain-Subdomains-using-OSINT
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T17:55:36.119392+00:00'
updated_at: '2023-05-26T00:47:15.907233+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather-Victim-Network-Information|T1590 - Gather Victim Network
    Information]]
sub_techniques: []
tags:
  - OSINT
  - reconnaissance
  - subdomain-enumeration
commands:
  - '[[commands/sublist3r-enumerate-subdomains]]'
platforms:
  - Linux
tools:
  - '[[tools/Sublist3r]]'
validated: true
---

# Enumerate-Domain-Subdomains-using-OSINT

## Summary

This procedure uses open-source intelligence (OSINT) sources to enumerate subdomains associated with a target domain, helping to map the attack surface during reconnaissance phases of security assessments. It leverages search engines, certificate transparency logs, and other public databases to discover hidden or forgotten subdomains without direct interaction with the target infrastructure.

## Description

Domain subdomain enumeration via OSINT is a passive reconnaissance technique that collects information from publicly available sources to identify subdomains. This is useful in red team engagements to discover potential entry points, such as administrative panels or misconfigured services, without alerting the target. The procedure relies on tools like Sublist3r, which queries multiple OSINT providers including search engines (Baidu, Yahoo, Google, Bing), DNS databases (Netcraft, DNSdumpster), threat intelligence platforms (VirusTotal, ThreatCrowd), and passive DNS sources. Success reveals a list of unique subdomains, which can be further probed for vulnerabilities. This approach minimizes detection risk as it generates no traffic to the target.

## Requirements

1. Access to a Linux environment (e.g., Kali Linux) with internet connectivity.
2. Sublist3r tool installed and configured ([[tools/Sublist3r]]).
3. Target domain name (e.g., example.com) provided as input.
4. Optional: Python dependencies like requests and dnspython for Sublist3r functionality.

## Defense

Defensive measures include monitoring for aggregated subdomain queries across OSINT sources, though detection is challenging due to the passive nature. Implement certificate transparency monitoring to track new subdomain registrations and use tools like DNSDumpster defensively to audit exposed subdomains.

## Objectives

1. Discover all publicly indexed subdomains for the target domain.
2. Compile a unique list of subdomains for further enumeration or targeting.
3. Identify potential attack surfaces without active scanning.

## Instructions

### Step 1: Verify Tool Installation and Environment

**Context**: Ensure Sublist3r is installed and accessible to avoid runtime errors. This step confirms the tool's availability and tests basic functionality.

Navigate to the Sublist3r directory and run the help command to verify installation.

**Command** ([[commands/sublist3r-show-help]]):
```bash
sublist3r -h
```

> This displays the tool's usage options. If the command fails, reinstall via git clone and pip install -r requirements.txt.

### Step 2: Prepare Target Domain

**Context**: Define the target domain to enumerate. This step involves validating the domain format and optionally creating an output file structure for organized results.

Create a working directory and note the target domain (e.g., cisco.com). Ensure the domain is resolvable via a quick DNS lookup.

**Command** ([[commands/sublist3r-enumerate-subdomains]]):
```bash
nslookup $_DOMAIN
```

> Expected output confirms the domain resolves (e.g., IP addresses returned). If it fails, check for typos or use a valid domain.

### Step 3: Execute Subdomain Enumeration

**Context**: Run the core enumeration using multiple OSINT sources to gather subdomains. This aggregates data from search engines, DNS dumps, and certificate logs for comprehensive coverage.

Invoke Sublist3r with the target domain flag to start querying sources.

**Command** ([[commands/sublist3r-enumerate-subdomains]]):
```bash
sublist3r -d $_DOMAIN -o $_OUTPUT_FILE
```

> The tool will query sources like Baidu, Yahoo, Google, Bing, Netcraft, DNSdumpster, VirusTotal, ThreatCrowd, SSL certificates, and PassiveDNS. Progress messages indicate each source being searched.

### Step 4: Review and Deduplicate Results

**Context**: Analyze the output file for unique subdomains and remove duplicates. This step validates the enumeration and prepares data for subsequent tools like httpx or masscan.

Open the output file and count unique entries using standard Unix tools.

**Command** ([[commands/sublist3r-enumerate-subdomains]]):
```bash
sort -u $_OUTPUT_FILE | wc -l
```

> This sorts, uniques, and counts lines, showing the total unique subdomains found.

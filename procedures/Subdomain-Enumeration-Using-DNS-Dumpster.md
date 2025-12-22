---
id: 0c0fc5b7-6370-4cf6-8d79-00a25b7687fe
name: Subdomain-Enumeration-Using-DNS-Dumpster
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.744937+00:00'
updated_at: '2023-04-10T20:25:40.123615+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Network Information|T1590 - Gather Victim Network
    Information]]
  - >-
    [[techniques/Search Open Technical Databases|T1596 - Search Open Technical
    Databases]]
sub_techniques: []
tags:
  - '[[tags/Enumerate all subdomains (only if the scope is *.domain.ext)]]'
  - '[[tags/Subdomains Enumeration]]'
  - '[[tags/Using dnsdumpster]]'
commands:
  - '[[commands/git-clone-dnsdumpster-repository]]'
  - '[[commands/run-dnsdumpster-enumeration]]'
platforms:
  - Linux
tools:
  - '[[tools/DNS-Dumpster]]'
validated: true
---

# Subdomain-Enumeration-Using-DNS-Dumpster

## Summary

This procedure uses the DNS Dumpster tool to enumerate subdomains for a target domain by querying public sources such as DNS records, search engines, and certificate transparency logs. It provides a list of discovered subdomains that can be used for further reconnaissance, identifying potential attack surfaces like forgotten or misconfigured subdomains hosting vulnerable applications.

## Description

Subdomain enumeration is a key reconnaissance technique to map the attack surface of a target organization. DNS Dumpster automates the collection of subdomain data from multiple open sources, including VirusTotal, Recon, and Spamhaus, without requiring direct access to the target's infrastructure. This is particularly useful in penetration testing or red team engagements to discover hidden assets. From an offensive standpoint, it reveals entry points for attacks like subdomain takeover or targeted phishing. Defensively, it helps organizations identify shadow IT or unauthorized subdomains. The procedure assumes a Linux environment with Python and Git installed, and it outputs a CSV file with subdomains, IPs, and associated data for analysis.

## Requirements

1. Internet access to query public sources
2. Git and Python 3 installed on a Linux system
3. The DNS Dumpster tool, cloned from its GitHub repository
4. Target domain name (e.g., example.com)

## Defense

Defensive measures and detection strategies:

- Implement DNS monitoring tools like DNSSec or log aggregation to detect anomalous queries
- Use certificate transparency monitoring to track subdomain registrations
- Restrict public exposure of subdomains through internal DNS zoning and avoid wildcard certificates where possible
- Employ web application firewalls (WAFs) to block reconnaissance attempts on discovered subdomains

## Objectives

1. Discover all publicly resolvable subdomains for the target domain
2. Gather associated IP addresses and host details for prioritization in further attacks
3. Identify potential vulnerable or forgotten subdomains for exploitation

## Instructions

### Step 1: Clone the DNS Dumpster Repository

**Context**: Download the DNS Dumpster tool from its official GitHub repository to obtain the necessary Python scripts for enumeration.

**Command** ([[commands/git-clone-dnsdumpster-repository]]):
```bash
git clone https://github.com/nmmapper/dnsdumpster
```

> This command fetches the repository containing dnsdumpster.py and its dependencies. Expected output includes progress messages ending with 'Cloning into 'dnsdumpster'...'. Verify by checking for the dnsdumpster.py file in the new directory.

### Step 2: Navigate to the Directory and Run Enumeration

**Context**: Change into the cloned directory and execute the tool against the target domain to query public sources and generate a subdomain report.

**Command** ([[commands/run-dnsdumpster-enumeration]]):
```bash
cd dnsdumpster && python dnsdumpster.py -d example.com
```

> Replace 'example.com' with the target domain. The tool will query sources like DNSdumpster's API equivalents and output a CSV file (e.g., example.com.csv) with subdomains, IPs, and metadata. Expected output includes console logs of queries and a success message upon completion, such as 'Data written to example.com.csv'.

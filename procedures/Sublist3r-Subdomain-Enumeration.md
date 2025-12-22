---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Network Information|T1590 - Gather Victim Network
    Information]]
sub_techniques:
  - >-
    [[techniques/Gather Victim Network Identity Information|T1590.001 - Gather
    Victim Network Identity Information]]
tags:
  - subdomain-enumeration
  - osint
  - reconnaissance
  - sublist3r
commands:
  - '[[commands/sublist3r-bruteforce-enumeration]]'
  - '[[commands/sublist3r-verbose-enumeration]]'
  - '[[commands/sublist3r-specific-engines-enumeration]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/Sublist3r]]'
validated: true
---

# Sublist3r-Subdomain-Enumeration

## Summary

This procedure uses Sublist3r, a Python-based OSINT tool, to enumerate subdomains of a target domain through search engine queries, web scraping, and optional brute-forcing. It helps attackers or penetration testers identify hidden subdomains that could serve as additional attack surfaces, such as administrative interfaces or forgotten assets.

## Description

Subdomain enumeration is a key reconnaissance step to map the target's digital footprint. Sublist3r leverages multiple sources like Google, Bing, Yahoo, VirusTotal, and others to passively discover subdomains without direct interaction with the target's infrastructure. It supports verbose output for real-time monitoring, brute-force wordlist attacks for active discovery, and engine-specific queries to focus on reliable sources. This technique is useful in the initial phases of an engagement to expand the attack surface, identify misconfigurations, or find entry points like exposed APIs. The procedure assumes a Kali Linux or similar environment and requires internet access for external queries.

## Requirements

1. Internet access for querying search engines and services.
2. Python 3 installed on the system.
3. Sublist3r tool installed (see [[tools/Sublist3r]] for installation).
4. Optional: A wordlist for brute-force mode (e.g., subdomains-top1million-5000.txt from SecLists).

## Defense

- Implement DNS monitoring and logging to detect anomalous queries or subdomain registrations.
- Use certificate transparency logs (e.g., via crt.sh) to track and secure all subdomains proactively.
- Deploy web application firewalls (WAFs) and rate limiting on public-facing services to hinder automated enumeration attempts.
- Regularly audit and remove unused subdomains to minimize the attack surface.

## Objectives

1. Discover valid subdomains associated with the target domain to map the full asset inventory.
2. Identify potential entry points such as development, staging, or third-party hosted subdomains.
3. Collect output for further analysis, such as probing for live hosts or vulnerabilities.

## Instructions

### Step 1: Prepare the Target Domain

**Context**: Define the target domain and ensure Sublist3r is ready. This step sets up the enumeration scope.

Run a basic check to verify tool accessibility:

```bash
python3 sublist3r.py -h
```

> This displays the help menu, confirming installation. If errors occur, reinstall via git clone https://github.com/aboul3la/Sublist3r.git && cd Sublist3r && pip3 install -r requirements.txt.

### Step 2: Perform Verbose Enumeration

**Context**: Run a standard enumeration with real-time output to monitor progress and gather initial subdomains from default engines.

**Command** ([[commands/sublist3r-verbose-enumeration]]):
```bash
python3 sublist3r.py -v -d $_DOMAIN
```

> Replace $_DOMAIN with the target (e.g., example.com). The -v flag enables verbose mode for live results. This queries default engines like Google and Bing. Expected output includes a list of discovered subdomains printed to stdout as they are found.

### Step 3: Enable Brute-Force for Comprehensive Discovery

**Context**: If passive methods yield few results, activate brute-forcing to test common subdomain names against DNS records.

**Command** ([[commands/sublist3r-bruteforce-enumeration]]):
```bash
python3 sublist3r.py -b -d $_DOMAIN
```

> The -b flag enables the built-in wordlist for brute-forcing. This actively queries DNS, which may trigger alerts. Save output to a file with > subdomains.txt for later use. Success is indicated by additional subdomains beyond passive results.

### Step 4: Target Specific Engines

**Context**: Focus on high-confidence sources like VirusTotal or Yahoo to refine results and avoid rate limits on major engines.

**Command** ([[commands/sublist3r-specific-engines-enumeration]]):
```bash
python3 sublist3r.py -e $_ENGINES -d $_DOMAIN
```

> Specify $_ENGINES as a comma-separated list (e.g., google,yahoo,virustotal). This limits queries to selected engines, reducing noise. If an engine fails (e.g., due to API limits), Sublist3r will skip it. Combine outputs from multiple runs for a complete list.

### Step 5: Validate and Deduplicate Results

**Context**: Merge outputs from previous steps and remove duplicates to create a clean subdomain list for further reconnaissance.

Use standard Unix tools:

```bash
cat subdomains*.txt | sort -u > unique_subdomains.txt
```

> This aggregates and uniques the results. Verify with nslookup or dig on a few entries to confirm resolvability.

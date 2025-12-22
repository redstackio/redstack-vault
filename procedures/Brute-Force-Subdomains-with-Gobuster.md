---
type: procedure
description: >-
  Enumerate subdomains of a target domain using Gobuster's DNS brute-forcing
  mode with a wordlist.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - reconnaissance
  - subdomain-enumeration
  - dns-brute-force
commands:
  - '[[commands/gobuster-dns-subdomain-brute-force]]'
platforms:
  - Linux
  - Network
tools:
  - '[[tools/Gobuster]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Brute-Force-Subdomains-with-Gobuster

## Summary

This procedure uses Gobuster in DNS mode to perform brute-force enumeration of subdomains for a given target domain. It relies on a comprehensive wordlist to guess potential subdomains by querying DNS records, helping identify hidden or forgotten subdomains that expand the attack surface during reconnaissance.

## Description

Subdomain brute-forcing is a key reconnaissance technique to discover the full scope of a target's web presence. Gobuster's DNS mode sends DNS queries for each word in the provided wordlist prepended to the target domain (e.g., 'admin.example.com'). Successful resolutions indicate valid subdomains. This is particularly useful in early penetration testing phases to map the domain's structure. The procedure assumes access to a wordlist like the JHaddix subdomain list, which contains common subdomain names. It maps to MITRE ATT&CK's Reconnaissance tactic, specifically gathering victim host information via domain properties.

## Requirements

1. Gobuster tool installed on a Linux-based system (e.g., Kali Linux).
2. A comprehensive subdomain wordlist file (e.g., downloaded from JHaddix's gist: https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056).
3. Network access to perform DNS queries against the target domain (no authentication required, but firewalls may block aggressive querying).
4. Basic command-line proficiency.

## Defense

Defensive measures and detection strategies:

- Implement DNS rate limiting and query monitoring using tools like BIND or PowerDNS to detect and block brute-force patterns.
- Use DNS security extensions (DNSSEC) to prevent unauthorized queries and logging anomalies.
- Monitor for unusual DNS query volumes from external IPs using SIEM tools like Splunk or ELK Stack.
- Deploy web application firewalls (WAFs) that alert on reconnaissance patterns, though this is DNS-focused.

## Objectives

1. Discover valid subdomains to expand the target's attack surface.
2. Identify potentially misconfigured or forgotten subdomains hosting sensitive services.
3. Collect a list of resolvable subdomains for further enumeration (e.g., port scanning or vulnerability assessment).
4. Validate the completeness of the target's domain footprint.

## Instructions

### Step 1: Prepare the Wordlist

**Context**: Obtain or prepare a high-quality wordlist of potential subdomain names. This step ensures the brute-force attempt is effective by using a proven list of common subdomains.

Download the JHaddix subdomain wordlist if not already available:

```bash
git clone https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056.git subdomains-wordlist
# Or manually download all.txt from the gist and save as subdomains.txt
```

> This downloads a curated list of over 10,000 common subdomain permutations. If the wordlist is too large, filter it for relevance (e.g., using grep for specific patterns). Expected output: A text file with one subdomain guess per line.

### Step 2: Execute Gobuster DNS Brute-Force

**Context**: Run Gobuster to query DNS for each potential subdomain. This step performs the core enumeration, resolving valid subdomains based on DNS responses.

**Command** ([[commands/gobuster-dns-subdomain-brute-force]]):

```bash
gobuster dns -d example.com -w /path/to/subdomains.txt -t 50 -q
```

> Replace `example.com` with the target domain and `/path/to/subdomains.txt` with your wordlist path. The `-t 50` flag sets 50 threads for faster execution, and `-q` enables quiet mode to reduce verbosity. If the target has DNSSEC enabled, you may need to add `--wildcard` to handle wildcard resolutions. Expected output: Real-time display of found subdomains (e.g., `Found: admin.example.com`), with a summary at the end showing total queries, discoveries, and rate.

Decision point: If no subdomains are found after 10% of the wordlist, consider switching to a different wordlist or tool like dnsrecon, as the target may have strict DNS policies.

### Step 3: Analyze and Save Results

**Context**: Review the output to identify valid subdomains and save them for further use. This verifies success and prepares data for subsequent reconnaissance steps.

Redirect output to a file for analysis:

```bash
gobuster dns -d example.com -w /path/to/subdomains.txt -o subdomains-found.txt
```

> The `-o` flag saves output to `subdomains-found.txt`. Manually inspect the file for valid entries (e.g., using `cat subdomains-found.txt | grep Found`). Cross-reference with tools like `dig` or `nslookup` to confirm resolutions. Expected output: A text file listing discovered subdomains with their IP addresses if resolved.

Decision point: If fewer than expected subdomains are found, increase threads or use a larger wordlist; if rate-limited, add delays with `--delay` flag.

---
id: f808fa87-d2a7-42c3-89b2-44df72f3fc92
name: Brute-Force-Subdomains-with-Dnsrecon
type: procedure
verified: true
submitted: false
created_at: '2020-07-24T17:11:53.470032+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - reconnaissance
  - subdomain-enumeration
  - dns
  - bruteforce
commands:
  - '[[commands/dnsrecon-subdomain-bruteforce]]'
platforms:
  - Network
tools:
  - '[[tools/DNSRecon]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Brute-Force-Subdomains-with-Dnsrecon

## Summary

This procedure uses the dnsrecon tool to perform brute-force enumeration of subdomains for a target domain by testing potential subdomain names against a comprehensive wordlist. It is a key reconnaissance technique to map the attack surface by discovering hidden or forgotten subdomains that may host services or applications vulnerable to further exploitation.

## Description

Subdomain brute-forcing involves generating and querying DNS records for possible subdomain combinations derived from a wordlist. Dnsrecon automates this process by sending DNS queries for each potential subdomain and reporting those that resolve. This technique is particularly useful in the initial reconnaissance phase of penetration testing or red team engagements to identify the full scope of a target's web presence. The wordlist should be comprehensive, such as the one curated by Jason Haddix, which includes common subdomain names like 'admin', 'test', 'dev', and more. Success depends on the quality of the wordlist and the target's DNS configuration; it may not discover subdomains protected by wildcard DNS or those not publicly resolvable.

## Requirements

1. Network access to perform DNS queries against the target domain (no authentication required, but firewalls may block aggressive querying).
2. Dnsrecon tool installed on a Linux-based system (e.g., Kali Linux).
3. A subdomain wordlist file, such as the JHaddix all.txt from https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056.
4. Basic command-line proficiency.

## Defense

Defensive measures include rate-limiting DNS queries at the authoritative DNS server, implementing wildcard DNS to mask non-existent subdomains, and monitoring for anomalous DNS query patterns from unknown sources. Detection can involve logging high volumes of NXDOMAIN responses or using tools like DNS firewall services to block brute-force attempts.

## Objectives

1. Discover valid subdomains to expand the target's attack surface.
2. Identify potentially sensitive or misconfigured subdomains (e.g., admin portals).
3. Generate a list of resolvable subdomains for further enumeration or probing.

## Instructions

### Step 1: Obtain Subdomain Wordlist

**Context**: Download or prepare a comprehensive wordlist of potential subdomain names to use for brute-forcing. This ensures coverage of common and organization-specific subdomains.

Download the JHaddix wordlist using wget:

```bash
wget https://gist.githubusercontent.com/jhaddix/86a06c5dc309d08580a018c66354a056/raw/96f6d403e1b0e1d3d13a7066ae8c4e04b1cf6253/all.txt -O subdomains.txt
```

> This command fetches the wordlist and saves it as subdomains.txt. Verify the file size (should be around 2-3 MB) to ensure successful download.

### Step 2: Run Dnsrecon Brute-Force Enumeration

**Context**: Execute the dnsrecon tool with the subdomain brute-force module, specifying the target domain and wordlist. This step queries DNS for each subdomain in the list and collects responses for valid ones.

**Command** ([[commands/dnsrecon-subdomain-bruteforce]]):

```bash
dnsrecon -d $_TARGET_DOMAIN -D subdomains.txt -t brt -j
```

> Replace $_TARGET_DOMAIN with the target (e.g., example.com). The -t brt flag enables brute-force mode, -D specifies the dictionary file, and -j outputs in JSON for easier parsing. Expected output includes a list of discovered subdomains with their types (e.g., A, CNAME) if they resolve. Run time varies based on wordlist size (expect 10-60 minutes for large lists).

### Step 3: Parse and Verify Results

**Context**: Review the output to identify valid subdomains and optionally filter or export for further use, such as probing with tools like httpx.

If using JSON output, parse with jq:

```bash
cat dnsrecon_output.json | jq '.subdomains[] | select(.resolved == true) | .name'
```

> This extracts only resolved subdomain names. Manually verify a few by pinging or nslookup to confirm resolvability. If no subdomains are found, try a smaller wordlist or check for DNS rate-limiting.

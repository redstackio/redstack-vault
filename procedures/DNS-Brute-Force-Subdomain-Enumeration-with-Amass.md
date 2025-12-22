---
id: e36a27d8-7a78-4697-b41b-25d452eabd09
name: DNS-Brute-Force-Subdomain-Enumeration-with-Amass
type: procedure
verified: true
submitted: false
created_at: '2020-07-02T15:08:27.021843+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques:
  - '[[Hardware]]'
tags:
  - reconnaissance
  - subdomain-enumeration
  - dns
  - brute-force
  - amass
commands:
  - '[[commands/amass-enum-brute-force-subdomains]]'
  - '[[commands/amass-enum-active-brute-force-with-database]]'
platforms:
  - Linux
tools:
  - '[[tools/amass]]'
validated: true
---

# DNS-Brute-Force-Subdomain-Enumeration-with-Amass

## Summary

This procedure uses the OWASP Amass tool to perform brute-force DNS enumeration of subdomains for a target domain. It covers both a basic approach using Amass's built-in wordlist and an advanced method with a custom wordlist, active scanning, IP resolution, and structured output to files and a database for further analysis. This technique is useful in reconnaissance phases to map the attack surface by discovering hidden or forgotten subdomains.

## Description

DNS brute-force subdomain enumeration involves generating potential subdomain names based on a wordlist and querying DNS servers to check for their existence. Amass automates this process, combining brute-forcing with passive data sources for more comprehensive results. The basic method relies on Amass's default wordlist and performs passive enumeration alongside brute-forcing, resolving IPs for discovered subdomains. The advanced method allows customization with external wordlists (e.g., from SecLists), enables active DNS resolution, specifies sources, and outputs results to a directory for graph database storage and a clean results file. This is typically used in red team engagements or penetration tests to identify entry points like admin panels or API endpoints on subdomains. Prerequisites include network access to the target's DNS resolvers and installation of Amass. Expected outcomes include a list of valid subdomains with associated IPs, which can feed into further tools like httpx for live host probing.

## Requirements

1. Amass tool installed (see [[tools/amass]] for installation).
2. Network connectivity to public DNS resolvers or the target's authoritative DNS servers.
3. Optional: A custom wordlist file (e.g., subdomains-top1million-5000.txt from SecLists) for advanced enumeration.
4. Sufficient permissions to write to output directories and files.
5. Kali Linux or similar environment recommended for pre-installed dependencies.

## Defense

Defensive measures and detection strategies:

- Implement DNS rate limiting and query monitoring at the authoritative DNS server to detect high-volume brute-force attempts.
- Use DNS firewalls or response policy zones (RPZ) to block or log suspicious queries.
- Monitor for anomalous DNS traffic patterns, such as rapid queries for sequential subdomain names, using tools like Zeek or Suricata.
- Enable DNSSEC to prevent some enumeration but note it doesn't fully mitigate brute-forcing.

## Objectives

1. Discover valid subdomains through brute-force DNS queries to expand the target's attack surface.
2. Resolve IP addresses for discovered subdomains to identify hosting infrastructure.
3. Generate structured output for integration with other reconnaissance tools or visualization.
4. Expected outcome: A list of enumerated subdomains that can be used for subsequent vulnerability scanning or mapping.

## Instructions

### Step 1: Perform Basic Brute-Force Subdomain Enumeration

**Context**: This step uses Amass's built-in wordlist to brute-force subdomains while also querying passive data sources. The -ip flag resolves IP addresses for valid subdomains, providing immediate infrastructure details. This is ideal for quick reconnaissance without custom preparation.

**Command** ([[commands/amass-enum-brute-force-subdomains]]):
```bash
amass enum -ip -brute -d $_TARGET_DOMAIN
```

> This command initiates passive enumeration from multiple sources (e.g., Certificate Transparency logs, search engines) followed by brute-forcing. It queries DNS for each potential subdomain in the wordlist and verifies resolutions. Run this in a terminal with Amass installed. Replace $_TARGET_DOMAIN with the target (e.g., example.com). The process may take several minutes depending on the domain's complexity and network speed. Success is indicated by the discovery summary at the end, showing names found via brute-force.

### Step 2: Perform Advanced Brute-Force Enumeration with Custom Wordlist and Database Output

**Context**: For more control, use a custom wordlist to target specific patterns (e.g., admin, api). The -active flag enables direct DNS interactions, -src lists used sources, -dir creates a graph database for visualization, and -o outputs clean results to a file. This step builds on the basic method for deeper analysis and persistence of results.

**Command** ([[commands/amass-enum-active-brute-force-with-database]]):
```bash
amass enum -active -d $_TARGET_DOMAIN -brute -w $_WORDLIST -src -ip -dir $_OUTPUT_DIR -o $_OUTPUT_RESULTS_FILE
```

> Prepare by downloading a wordlist (e.g., wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-5000.txt -O $_WORDLIST). Create $_OUTPUT_DIR (e.g., mkdir /tmp/amass-output). Replace placeholders: $_TARGET_DOMAIN (e.g., example.com), $_WORDLIST (path to file), $_OUTPUT_DIR (e.g., /tmp/amass-output), $_OUTPUT_RESULTS_FILE (e.g., /tmp/amass-output/subdomains.txt). Execute the command; it will perform active brute-forcing, resolve IPs, and store data in a Cayley graph database in $_OUTPUT_DIR for tools like Amass Viz. If the wordlist is large, monitor resource usage. Verify by checking the output file for listed subdomains.

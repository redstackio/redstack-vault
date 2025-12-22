---
type: procedure
description: >-
  Generate potential subdomain variations by combining base subdomains with
  mutation words and resolve them to identify active hosts.
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Hardware]]'
sub_techniques: []
tags:
  - reconnaissance
  - subdomain-enumeration
  - dns
commands:
  - '[[commands/altdns-generate-and-resolve-subdomains]]'
platforms:
  - Linux
tools:
  - '[[tools/Altdns]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Mutate-Subdomain-Wordlist-for-DNS-Enumeration-Using-Altdns

## Summary

This procedure uses the altdns tool to mutate a list of known subdomains with a wordlist of common prefixes, suffixes, or variations, generating thousands of potential subdomain permutations. It then resolves these to identify which ones exist and are active, expanding the attack surface during reconnaissance phases of penetration testing or red team engagements.

## Description

Subdomain enumeration is a critical reconnaissance step to map the full domain footprint of a target organization. Tools like altdns automate the permutation of base subdomains (e.g., from prior enumeration) with mutation words (e.g., 'dev', 'staging', 'api') to create realistic variations that might not be discovered through brute-force alone. This procedure focuses on generating the permutations and resolving them via DNS queries to filter for live hosts. It is particularly useful when initial scans reveal partial subdomain coverage, helping uncover hidden assets like development environments or third-party integrations. The output can feed into further tools like httpx or masscan for service probing.

## Requirements

1. Linux environment (Kali or Ubuntu recommended) with internet access for DNS resolution.
2. Altdns tool installed ([[tools/Altdns]]).
3. Input files: A base subdomain wordlist (e.g., subdomains.txt with entries like 'mail.target.com') and a mutation wordlist (e.g., words.txt with entries like 'dev-', '-api', 'staging').
4. Sufficient disk space for output files, as permutations can generate large datasets (e.g., 10k+ entries).

## Defense

Defensive measures include DNS query rate limiting, anomaly detection on high-volume subdomain resolutions from single IPs, and monitoring for tools like altdns via process signatures or network patterns. Use DNS firewalls to block suspicious queries and implement certificate transparency logging to track subdomain registrations.

## Objectives

1. Generate a comprehensive list of potential subdomain permutations based on known subdomains and mutation patterns.
2. Resolve the generated subdomains to identify active DNS records.
3. Provide a filtered list of resolvable subdomains for further enumeration or targeting.
4. Expand the target's visible attack surface without alerting defenders through passive or low-volume queries.

## Instructions

### Step 1: Prepare Input Files

**Context**: Gather or create the base subdomain list from prior reconnaissance (e.g., using tools like subfinder or amass) and a mutation wordlist with common subdomain patterns. This ensures the mutations are relevant to the target environment.

Ensure subdomains.txt contains one subdomain per line (e.g., 'www.target.com', 'mail.target.com') and words.txt contains mutation elements (e.g., 'dev', 'test', 'api', '-', '.').

### Step 2: Run Altdns to Generate and Resolve Permutations

**Context**: Execute the altdns command to combine the inputs, generate permutations, and resolve them. This step performs the core mutation and DNS lookup in one pass, producing a results file with only resolvable subdomains.

**Command** ([[commands/altdns-generate-and-resolve-subdomains]]):
```bash
altdns -i subdomains.txt -o data_output -w words.txt -r -s results_output.txt
```

> This command reads from subdomains.txt (-i), outputs intermediate permutations to data_output (-o), uses words.txt for mutations (-w), enables DNS resolution (-r), and saves resolved results to results_output.txt (-s). The -r flag queries DNS for each permutation, filtering out non-resolving ones to reduce noise.

### Step 3: Review and Filter Output

**Context**: Inspect the results_output.txt for valid subdomains and optionally deduplicate or sort them for use in subsequent tools.

Use commands like `sort -u results_output.txt > unique_subdomains.txt` to clean the output. Verify a sample manually with `dig` or `nslookup` to confirm resolution.

## Expected Output

The results_output.txt file will contain a list of resolvable subdomains, one per line (e.g., 'dev-api.target.com', 'staging.mail.target.com'), along with any associated IP addresses if resolution includes A records. Intermediate data_output will have all permutations before resolution, useful for offline review if DNS queries are rate-limited.

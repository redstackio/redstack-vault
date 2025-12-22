---
id: 3e4a130a-44b2-4783-963a-d398ee5c5d74
name: Generate-and-Resolve-Domain-Name-Permutations
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:30.913532+00:00'
updated_at: '2023-05-26T00:48:53.058161+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - reconnaissance
  - dns
  - permutation
  - brute-force
commands:
  - '[[commands/dnsgen-massdns-generate-and-resolve-permutations]]'
platforms:
  - Linux
tools:
  - '[[tools/dnsgen]]'
  - '[[tools/massdns]]'
validated: true
---

# Generate-and-Resolve-Domain-Name-Permutations

## Summary

This procedure generates permutations of domain names from a provided input file using dnsgen and then resolves the generated domains using massdns to identify valid DNS records, aiding in reconnaissance for discovering subdomains or potential attack surfaces.

## Description

Domain permutation generation is a key reconnaissance technique used to brute-force variations of known domains, such as subdomains or alternative TLDs, to uncover hidden assets. dnsgen creates combinatorial variations based on wordlists or input domains, while massdns performs high-speed parallel DNS resolutions against a list of resolvers to validate which permutations resolve to IP addresses. This is particularly useful in red team engagements for mapping out an organization's digital footprint without relying on public databases. The procedure assumes a Unix-like environment and focuses on A record resolutions for efficiency.

## Requirements

1. A text file (e.g., domains.txt) containing base domains or words, one per line.
2. A resolvers file (e.g., resolvers.txt) with a list of public DNS resolvers in host:port format.
3. dnsgen and massdns tools installed on a Linux system.
4. Network access to perform DNS queries (no firewall blocking outbound UDP/TCP port 53).

## Defense

Defensive measures and detection strategies:

- Monitor DNS query volumes from internal networks for unusual spikes or patterns matching permutation generation.
- Implement DNS rate limiting and anomaly detection using tools like Suricata or Zeek to flag high-volume resolutions.
- Use DNS sinkholing to redirect suspicious queries and log attempted resolutions.

## Objectives

1. Generate a large set of domain permutations from base inputs to expand the reconnaissance scope.
2. Resolve permutations efficiently to filter valid domains and associated IP addresses.
3. Identify potential live assets for further enumeration or targeting.

## Instructions

### Step 1: Prepare Input File

**Context**: Create or verify the input file containing base domains or keywords. This step ensures the permutation generation starts with relevant data, such as known domains from passive recon.

No specific command is required here, but manually edit or generate domains.txt with entries like:

```
example.com
api
admin
mail
```

> This file serves as stdin for dnsgen. Ensure it has no extra whitespace or empty lines to avoid invalid permutations.

### Step 2: Generate and Resolve Permutations

**Context**: Pipe the input domains through dnsgen to create permutations, then directly into massdns for resolution. This chained approach avoids intermediate files for efficiency and produces output in JSON format for easy parsing.

**Command** ([[commands/dnsgen-massdns-generate-and-resolve-permutations]]):

```bash
cat domains.txt | dnsgen - | massdns -r /path/to/resolvers.txt -t A -o J --flush 2>/dev/null
```

> This command reads domains from stdin, generates permutations (e.g., api-example.com, admin.example.com), resolves A records in parallel, and outputs valid resolutions as JSON lines. The --flush option ensures immediate output, and 2>/dev/null suppresses errors for clean results. Redirect output to a file (e.g., > results.json) for analysis.

### Step 3: Analyze Results

**Context**: Review the resolved domains to identify valid ones. This step verifies success and prepares data for further recon, such as HTTP probing.

Use standard tools like grep or jq to parse the JSON output:

```bash
grep -o '"[a-zA-Z0-9.-]*"' results.json | sort -u
```

> Expected to yield a list of unique resolved domain names. If no resolutions occur, check resolvers.txt for validity or input file for errors.

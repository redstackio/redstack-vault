---
type: procedure
description: >-
  This procedure uses MassDNS to perform high-performance resolution of CNAME
  records for a list of subdomains, helping identify alias relationships in DNS
  configurations during reconnaissance.
verified: true
submitted: false
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Network Information]]'
  - '[[Domain Properties]]'
sub_techniques: []
tags:
  - dns-enumeration
  - reconnaissance
  - subdomain
  - cname
commands:
  - '[[commands/massdns-enumerate-cnames-for-subdomains]]'
tools:
  - '[[tools/massdns]]'
platforms:
  - Linux
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
---

# Enumerate-CNAME-Records-for-Subdomains-Using-MassDNS

## Summary

This procedure leverages MassDNS, a high-performance DNS stub resolver, to query CNAME records for a provided list of subdomains. CNAME records reveal domain aliases, which can expose hidden infrastructure, third-party services, or misconfigurations during reconnaissance phases of security assessments. It processes large subdomain lists efficiently by distributing queries across multiple resolvers to avoid rate limiting.

## Description

CNAME (Canonical Name) records map one domain to another, providing insights into a target's DNS structure without directly resolving to IP addresses. This technique is useful in passive reconnaissance to map out service integrations, CDNs, or load balancers associated with subdomains. MassDNS is particularly effective for bulk operations as it supports multithreading and custom resolver lists, reducing detection risk compared to sequential queries from a single source. The procedure assumes a Unix-like environment and focuses on offline processing of results for further analysis. It maps to MITRE ATT&CK under Reconnaissance for gathering victim network information via domain name resolution.

## Requirements

1. A list of subdomains in a text file (one per line, e.g., subdomains.txt) obtained from prior enumeration tools like Subfinder or Amass.
2. A list of public DNS resolvers (e.g., resolvers.txt) validated for reliability, ideally created using tools like dnsvalidator to ensure open resolvers.
3. MassDNS tool installed and accessible in the PATH.
4. Network access to perform outbound DNS queries (UDP/TCP port 53).
5. Basic command-line proficiency and a word processor for reviewing output files.

## Defense

Defensive measures include monitoring DNS query volumes from unusual sources, implementing rate limiting on authoritative DNS servers, and using DNS firewalls to block recursive queries. Detection can involve logging anomalous CNAME resolutions or integrating with SIEM for high-volume stub resolver traffic patterns.

## Objectives

1. Efficiently resolve CNAME records for hundreds or thousands of subdomains.
2. Identify alias domains that may point to external services or internal resources.
3. Generate a filtered output file for post-processing, excluding NXDOMAIN responses.
4. Minimize query failures by using a diverse resolver pool.

## Instructions

### Step 1: Prepare Subdomain List

**Context**: Ensure you have a clean list of subdomains to query. This step verifies the input file format, as MassDNS expects one subdomain per line without duplicates for optimal performance.

Review or generate your subdomains.txt file. If needed, deduplicate using:

```bash
sort -u subdomains.txt > unique-subdomains.txt
mv unique-subdomains.txt subdomains.txt
```

> This command sorts and removes duplicates, ensuring efficient querying. Expected output is a cleaned file with the same number of lines or fewer if duplicates existed.

### Step 2: Validate Resolver List

**Context**: A reliable resolver list prevents query timeouts and improves success rates. Use a pre-validated file like resolvers.txt containing open DNS servers (e.g., from dnsvalidator output).

Check the resolver file for validity:

```bash
wc -l resolvers.txt
head -5 resolvers.txt
```

> This displays the count and samples entries (e.g., 8.8.8.8). Expected output: A list of IP addresses, ideally 50+ for distribution. If invalid, regenerate using dnsvalidator.

### Step 3: Execute CNAME Enumeration

**Context**: Run MassDNS to query only CNAME records, outputting successful resolutions in a simple format for easy parsing.

**Command** ([[commands/massdns-enumerate-cnames-for-subdomains]]):

```bash
massdns -r $_RESOLVER_LIST -t CNAME -o S -w $_OUTPUT_FILE $_SUBDOMAINS_FILE
```

> This command distributes CNAME queries across resolvers, using simple output format (-o S) to list subdomain.CNAME.target records. Replace placeholders with actual files (e.g., resolvers.txt, output.cnames, subdomains.txt). Run time depends on list size; expect 1-5 minutes for 1000 subdomains. The -t CNAME limits to alias records, ignoring A/AAAA.

### Step 4: Review and Filter Results

**Context**: Post-process the output to extract valid CNAMEs, discarding errors like SERVFAIL or NXDOMAIN.

Use grep to filter successful responses:

```bash
grep -v "SERVFAIL\|NXDOMAIN" $_OUTPUT_FILE > valid-cnames.txt
wc -l valid-cnames.txt
```

> This removes failure lines, leaving only resolved CNAMEs. Expected output: A file with lines like "sub.example.com. CNAME alias.target.com." Success is indicated by non-zero lines in valid-cnames.txt, revealing potential reconnaissance targets.

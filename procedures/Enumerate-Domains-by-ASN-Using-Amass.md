---
id: 65aaca1d-d39a-49d9-ae18-f590e05a7609
name: Enumerate-Domains-by-ASN-Using-Amass
type: procedure
verified: true
submitted: false
created_at: '2020-06-29T16:38:40.350331+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[IP Addresses]]'
sub_techniques: []
tags:
  - reconnaissance
  - domain-enumeration
  - amass
  - asn
commands:
  - '[[commands/amass-intel-enumerate-domains-by-asn]]'
  - '[[commands/amass-intel-enumerate-domains-and-ips-by-asn]]'
platforms:
  - Linux
tools:
  - '[[tools/amass]]'
validated: true
---

# Enumerate-Domains-by-ASN-Using-Amass

## Summary

This procedure uses the Amass tool to enumerate domains and subdomains associated with a specific Autonomous System Number (ASN), which is uniquely allocated to organizations and linked to their public IP ranges. It is useful during reconnaissance phases to map an organization's digital footprint by discovering domains tied to their network infrastructure without direct interaction beyond public data sources.

## Description

An Autonomous System Number (ASN) is a unique identifier assigned to network operators, such as ISPs or large organizations, that manages a block of IP addresses. Tools like Amass leverage public databases (e.g., BGP data, certificate transparency logs) to reverse-lookup domains and subdomains registered under an ASN. This technique is passive in the basic mode, relying on existing intelligence data, or active when including IP resolution, which may generate minor network traffic. It is particularly effective for identifying attack surfaces in red team engagements or threat hunting, as it reveals interconnected domains that might host services, applications, or vulnerabilities. Prerequisites include knowing the target ASN (obtainable via WHOIS queries or tools like [[commands/whois-asn-lookup]]). The procedure supports both domain-only enumeration for stealth and combined domain/IP output for further targeting.

## Requirements

1. Amass tool installed and configured ([[tools/amass]]).
2. Knowledge of the target ASN (e.g., via public WHOIS lookup).
3. Network access to public internet for querying data sources.
4. Optional: Output file for saving results to enable chaining with other tools like [[commands/subfinder-enumerate]].

## Defense

Defensive measures and detection strategies:

- Monitor for unusual DNS or BGP data queries from internal networks using tools like Zeek or Suricata.
- Implement certificate transparency log monitoring to detect bulk domain discoveries.
- Use ASN-level network segmentation and rate-limiting on public-facing resolvers to hinder reconnaissance.
- Log and alert on Amass-like tool signatures in endpoint detection (e.g., process names, command-line arguments containing 'amass intel').

## Objectives

1. Identify all domains and subdomains associated with the target ASN to build a comprehensive asset inventory.
2. Optionally resolve associated IP addresses for service enumeration or vulnerability scanning.
3. Gather intelligence passively to minimize detection risk during initial reconnaissance.

## Instructions

### Step 1: Enumerate Domains by ASN

**Context**: Perform a passive lookup of domains tied to the ASN using Amass's intel module. This step queries public sources without generating active network traffic to the target, making it suitable for stealthy reconnaissance. It provides a list of discovered domains that can be used for further subdomain brute-forcing or service discovery.

**Command** ([[commands/amass-intel-enumerate-domains-by-asn]]):
```bash
amass intel -asn $_ASN
```

> This command outputs a list of domains associated with the specified ASN. Redirect output to a file (e.g., `> domains.txt`) for post-processing. If no domains are found, verify the ASN is correct and public-facing.

### Step 2: Enumerate Domains and IPs by ASN (Active Mode)

**Context**: Extend the enumeration to include IP address resolution for each discovered domain. The `-active` flag enables more aggressive querying (e.g., DNS resolution), which may produce detectable traffic but provides actionable IP targets for port scanning or exploitation. Use this when domain names alone are insufficient, such as for direct network mapping.

**Command** ([[commands/amass-intel-enumerate-domains-and-ips-by-asn]]):
```bash
amass intel -active -asn $_ASN -ip
```

> This command lists domains alongside their resolved IPs. Expect output in the format `domain IP`. If resolution fails for some domains, it could indicate DNS issues or private networks; retry with a different resolver or fall back to Step 1. Save results (e.g., `> domains-ips.txt`) for tools like [[commands/nmap-service-version-scan]].

### Step 3: Verify and Deduplicate Results

**Context**: After running the enumeration, clean the output to remove duplicates and validate domains. This ensures reliable input for subsequent procedures like [[procedures/Enumerate-Subdomains-Using-Subfinder]].

**Command** (using standard Unix tools, no specific command doc):
```bash
sort domains.txt | uniq > unique-domains.txt
```

> Manually verify a sample of domains via browser or [[commands/dig-lookup]] to confirm association with the target organization. If IPs were enumerated, cross-reference with ASN ownership using WHOIS.

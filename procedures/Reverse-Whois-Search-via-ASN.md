---
type: procedure
description: >-
  Perform reverse WHOIS lookup using the target's Autonomous System Number (ASN)
  to discover additional related domains, bypassing domain privacy protections,
  followed by subdomain enumeration.
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[IP Addresses]]'
sub_techniques: []
tags:
  - reconnaissance
  - domain-enumeration
  - asn-lookup
  - passive-recon
commands:
  - '[[commands/whois-get-asn]]'
  - '[[commands/amass-enum-from-asn]]'
platforms:
  - Linux
tools:
  - '[[tools/amass]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Reverse-Whois-Search-via-ASN

## Summary

This procedure enables the discovery of additional domains associated with a target organization by leveraging their Autonomous System Number (ASN). When standard WHOIS queries are blocked by privacy services, querying the ASN reveals IP ranges and related domains under the same network infrastructure. Subsequent subdomain enumeration on these domains expands the attack surface for further reconnaissance.

## Description

In scenarios where domain privacy protections (e.g., via registrars like GoDaddy or Namecheap) obscure ownership details, attackers can pivot to network-level intelligence. The ASN, assigned by regional internet registries, identifies the organization's internet routing domain. By querying reverse WHOIS databases or tools like Amass, related domains sharing the same ASN can be uncovered. This technique is passive, requiring no direct interaction with the target, and maps to MITRE ATT&CK's reconnaissance phase for gathering victim network information. It is particularly useful in initial reconnaissance to map the full asset inventory before active scanning.

## Requirements

1. Kali Linux or Ubuntu with internet access for WHOIS queries.
2. Installed tools: whois (standard on most Linux distros) and Amass.
3. Target domain name (e.g., example.com) with known public exposure.
4. No special credentials required, but rate limiting on public WHOIS servers should be respected to avoid blocks.

## Defense

Defensive measures include monitoring for unusual ASN queries via network logs, implementing domain privacy consistently across all assets, and using services like Cloudflare or Akamai to obscure infrastructure details. Detection can involve SIEM rules for high-volume WHOIS or Amass traffic from reconnaissance tools, and regular audits of exposed ASNs through tools like BGPView.

## Objectives

1. Identify the target's ASN to bypass WHOIS privacy.
2. Enumerate additional domains under the same ASN.
3. Expand subdomain discovery for a comprehensive asset map.
4. Achieve passive reconnaissance without alerting defenses.

## Instructions

### Step 1: Retrieve ASN from Target Domain

**Context**: Use the whois command to query the target's domain and extract the associated ASN, which represents the network provider or the organization's own routing block. This step provides the key input for reverse lookup.

**Command** ([[commands/whois-get-asn]]):
```bash
whois $_TARGET_DOMAIN | grep -i 'origin\|asn' | head -1
```

> This command performs a WHOIS lookup on the target domain and filters for ASN-related output. The grep pattern captures lines containing 'origin' or 'asn' (case-insensitive), and head limits to the first relevant line to avoid noise. Expected output includes the ASN number, e.g., 'AS12345'.

### Step 2: Enumerate Domains from ASN

**Context**: With the ASN identified, use Amass to passively enumerate all domains registered under that ASN. Amass queries multiple data sources (e.g., BGP tables, certificate transparency logs) to find related domains without direct target interaction, revealing hidden assets.

**Command** ([[commands/amass-enum-from-asn]]):
```bash
amass enum -passive -asn $_ASN -o output-domains.txt
```

> This invokes Amass in passive mode to avoid DNS queries that could trigger alerts. The -asn flag specifies the ASN number obtained in Step 1, and -o outputs results to a file for review. If the ASN yields many results, add -max 1000 to limit. Expected output is a list of domains in output-domains.txt, such as 'sub.example.com', 'related.org'.

### Step 3: Verify and Expand with Subdomain Enumeration

**Context**: For each discovered domain, run additional enumeration to find subdomains, creating a fuller picture of the attack surface. This step chains the ASN findings into actionable intelligence.

**Instructions**: Review output-domains.txt and select high-value domains. Then, for a specific domain:

**Command** ([[commands/amass-enum-from-asn]] variation for subdomains):
```bash
amass enum -passive -d $_DISCOVERED_DOMAIN -o subdomains.txt
```

> Reuse Amass but target individual domains from the ASN list. Replace $_DISCOVERED_DOMAIN with entries from output-domains.txt. This generates subdomains.txt with entries like 'api.related.org'. Cross-reference with tools like httpx for live hosts if needed.

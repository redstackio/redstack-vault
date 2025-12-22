---
type: procedure
description: >-
  Perform reverse DNS lookups on a list of IP addresses to discover associated
  subdomains belonging to a target organization.
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Domain Properties]]'
sub_techniques: []
tags:
  - reconnaissance
  - dns
  - subdomain-enumeration
  - passive-recon
commands:
  - '[[commands/hakrevdns-lookup-subdomains-from-ip-range]]'
  - '[[commands/hakrevdns-lookup-subdomain-with-custom-resolver]]'
platforms:
  - Linux
tools:
  - '[[tools/hakrevdns]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Reverse-DNS-Lookup-for-Subdomains-Using-Hakrevdns

## Summary

This procedure uses the hakrevdns tool to perform reverse DNS lookups on a range or list of IP addresses, identifying subdomains associated with a target organization. It is useful during the reconnaissance phase to map IP space to domain names without directly querying the target's DNS servers aggressively.

## Description

Reverse DNS lookup from IP addresses helps discover subdomains by resolving IPs back to hostnames, often revealing internal or forgotten subdomains. The procedure leverages hakrevdns, a fast tool built on masscan and dnsx, to handle large IP lists efficiently. It can process CIDR ranges via prips or read from files, making it suitable for passive reconnaissance on known IP blocks obtained from sources like ASN lookups or Shodan. This technique falls under MITRE ATT&CK Reconnaissance and is effective for expanding the attack surface by identifying potential entry points like web servers or APIs on subdomains.

## Requirements

1. Network access to public DNS resolvers (no target firewall blocking outbound DNS queries).
2. hakrevdns tool installed (see [[tools/hakrevdns]] for installation).
3. Optional: prips tool for generating IP ranges from CIDR notation (pre-installed on Kali Linux) or a text file containing IP addresses.
4. Basic bash environment on Linux.

## Defense

Defensive measures and detection strategies:

- Monitor DNS query logs for unusual reverse lookup patterns from external IPs.
- Implement DNS rate limiting on authoritative servers to prevent bulk reverse queries.
- Use DNSSEC to validate responses and detect spoofing attempts.
- Block or alert on high-volume reverse DNS queries targeting your IP ranges.

## Objectives

1. Identify subdomains linked to a target's IP address space to map the domain footprint.
2. Generate a list of resolvable hostnames for further enumeration or vulnerability scanning.
3. Avoid direct interaction with the target by using public resolvers, reducing detection risk.

## Instructions

### Step 1: Generate and Lookup Subdomains from IP Range

**Context**: Start by expanding a CIDR range into individual IPs using prips, then pipe them to hakrevdns for reverse DNS resolution. This step discovers subdomains by querying public DNS servers for PTR records. Use this when you have a known IP block (e.g., from WHOIS or ASN data) to systematically enumerate associated domains.

**Command** ([[commands/hakrevdns-lookup-subdomains-from-ip-range]]):
```bash
prips $_IP_RANGE | hakrevdns
```

> This command generates IPs from the specified range and performs reverse lookups. Replace $_IP_RANGE with a CIDR like 173.0.84.0/24. The output will list IPs with their resolved subdomains if PTR records exist. If no subdomains are found, only IPs without resolutions will appear.

### Step 2: Lookup Subdomain for Specific IP with Custom Resolver

**Context**: For targeted lookups on individual IPs or to bypass default OS resolvers (e.g., to avoid logging or use faster public DNS), specify a custom resolver like Cloudflare's 1.1.1.1. This optional step is useful for verifying specific IPs or testing different DNS paths without affecting system settings.

**Command** ([[commands/hakrevdns-lookup-subdomain-with-custom-resolver]]):
```bash
echo "$_IP" | hakrevdns -r $_RESOLVER
```

> Pipe a single IP via echo and use the -r flag for the resolver IP. This isolates the query to a trusted DNS server, reducing potential blocks from default resolvers. Expected output shows the IP and any resolved subdomain.

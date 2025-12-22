---
id: 874ec00a-0aff-4eaf-b7e9-25febb747fd7
name: Find-Domains-and-Netblocks-from-SPF-Records
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:28.277682+00:00'
updated_at: '2023-05-25T20:12:15.101840+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Domain Properties]]'
sub_techniques: []
tags:
  - reconnaissance
  - dns
  - spf
  - asset-discovery
  - domain-enumeration
commands:
  - '[[commands/assets-from-spf-basic-scan]]'
  - '[[commands/assets-from-spf-with-asn-to-jq]]'
platforms:
  - Linux
tools:
  - '[[tools/assets-from-spf]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Find-Domains-and-Netblocks-from-SPF-Records

## Summary

This procedure uses a Python script to parse Sender Policy Framework (SPF) DNS records for a target domain, extracting associated IP netblocks (CIDRs), IP addresses, and additional domains. It is useful during reconnaissance to expand the attack surface by identifying hidden or related assets that may not be directly discoverable through standard subdomain enumeration.

## Description

SPF records are DNS TXT records used to prevent email spoofing by specifying authorized IP addresses or domains that can send email on behalf of a domain. Attackers can abuse these records to discover internal or partner networks, cloud providers, or third-party services linked to the target. The 'assets-from-spf' script queries the SPF record, parses mechanisms like 'ip4:', 'ip6:', 'a', 'mx', 'include', and 'redirect', and outputs usable asset information. This technique maps to MITRE ATT&CK [[Reconnaissance]] Reconnaissance and [[Domain Properties]] Gather Victim Network Information: Domains, as it passively gathers network topology without direct interaction with the target beyond DNS queries. It is effective against organizations with complex email infrastructures and can reveal ASNs for further OSINT.

## Requirements

1. Linux environment with Python 3 installed.
2. Access to public DNS resolvers (no special privileges needed).
3. The 'assets-from-spf' tool installed (see [[tools/assets-from-spf]]).
4. For ASN output, jq installed for JSON parsing (sudo apt install jq).
5. Target domain name resolvable via DNS.

## Defense

Defensive measures and detection strategies:

- Monitor DNS query logs for unusual TXT record lookups on SPF entries from reconnaissance tools.
- Implement DNS rate limiting to prevent bulk queries.
- Use obfuscated SPF records or minimize 'include' mechanisms to reduce exposed assets.
- Deploy network monitoring for anomalous OSINT gathering patterns.

## Objectives

1. Extract IP netblocks and addresses from SPF mechanisms to identify network ranges.
2. Discover additional domains via 'include' or 'redirect' directives for further enumeration.
3. Optionally retrieve Autonomous System Numbers (ASNs) for ownership tracing.
4. Expand the target's asset inventory without alerting defenses.

## Instructions

### Step 1: Perform Basic SPF Asset Scan

**Context**: Start with a basic scan to retrieve IP addresses, CIDRs, and domains from the target's SPF record. This step queries DNS and parses the record without additional processing, providing a quick overview of exposed assets.

**Command** ([[commands/assets-from-spf-basic-scan]]):
```bash
python assets_from_spf.py $_DOMAIN
```

> Replace $_DOMAIN with the target domain (e.g., owasp.com). This command fetches the SPF TXT record, extracts mechanisms, and lists IPs/domains. It performs this step because SPF often includes third-party services, revealing hidden infrastructure.

### Step 2: Scan SPF Assets with ASN Information

**Context**: Enhance the output by including ASN details for each IP or netblock, which helps in identifying owning organizations (e.g., AWS, Azure). Pipe the JSON output to jq for formatted display. This step adds context to the assets for deeper OSINT.

**Command** ([[commands/assets-from-spf-with-asn-to-jq]]):
```bash
python assets_from_spf.py $_DOMAIN --asn | jq .
```

> The --asn flag queries WHOIS for ASN data. Use jq to pretty-print the JSON. Expected to show structured output with IPs, domains, and ASNs. If no ASN data is available, it falls back to basic info.

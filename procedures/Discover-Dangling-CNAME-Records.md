---
tags:
  - subdomain-takeover
  - dns
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-query]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:24.213Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: bfe9a6fa-150a-4c54-8002-d49f15a32692
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover-Dangling-CNAME-Records

## Summary

This procedure involves querying DNS records to detect CNAME entries pointing to third-party services that may be unclaimed, enabling subdomain takeover attacks. It is commonly used in reconnaissance to identify misconfigurations in domain management.

## Description

In this scenario, attackers query the DNS for subdomains like landing.udemy.com to find dangling CNAME records, such as those pointing to unbouncepages.com. A dangling record exists when the CNAME is set but the corresponding resource on the third-party service is not claimed or active. This allows an attacker to register the subdomain on the service and host malicious content, mimicking the parent domain for phishing or injecting XSS payloads. Prerequisites include access to DNS resolution tools; no authentication is needed for public queries. Expected outcomes include identification of vulnerable subdomains with low TTLs (e.g., 300 seconds) for quick exploitation.

## Requirements

1. DNS resolver access (e.g., public internet)
2. Basic knowledge of DNS record types (CNAME, TTL)
3. Tool like dig or nslookup installed

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated scanners
- Implement domain monitoring tools to alert on unclaimed third-party pointers
- Use short TTLs and verify third-party claims during service decommissioning

## Objectives

1. Identify misconfigured DNS records pointing to unclaimed services
2. Gather evidence for potential takeover without performing it
3. Assess risk of subdomain spoofing for phishing or XSS

## Instructions

### Step 1: Query CNAME Record

**Context**: Perform a DNS lookup specifically for CNAME records on the target subdomain to detect pointers to third-party platforms.

**Command** ([[commands/dig-cname-query]]):
```bash
dig +short landing.udemy.com CNAME
```

> This command queries the authoritative DNS server for the CNAME record. Expected output: "pages.unbounce.com." or similar, indicating a third-party pointer. If no record or an A record is returned instead, the subdomain is not vulnerable via CNAME takeover.

### Step 2: Analyze TTL and Resolution

**Context**: Check the TTL to understand how quickly changes propagate and confirm the record is dangling by attempting full resolution.

**Command** ([[commands/dig-cname-query]]):
```bash
dig landing.udemy.com
```

> Review the ANSWER section for CNAME details and TTL (e.g., 300). A dangling record will resolve to the third-party but show no further hosting details. Success is confirmed if the CNAME points to a known takeover-prone service like Unbounce.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/dig-cname-query]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[Reconnaissance]]

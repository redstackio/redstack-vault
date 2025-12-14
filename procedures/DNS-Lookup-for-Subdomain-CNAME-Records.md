---
tags:
  - dns
  - reconnaissance
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-lookup]]'
platforms:
  - Web
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9325946f-0518-4fd6-a7e7-3856992698fe
created_at: '2025-12-14T04:38:49.855Z'
updated_at: '2025-12-14T04:38:49.855Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# DNS-Lookup-for-Subdomain-CNAME-Records

## Summary

This procedure performs a DNS query to identify CNAME records for target subdomains, revealing potential misconfigurations like dangling pointers to external services such as AWS CloudFront, which can lead to subdomain takeover opportunities.

## Description

In a subdomain takeover attack, attackers scan for DNS records where a subdomain's CNAME points to a third-party service (e.g., *.cloudfront.net) that is no longer claimed by the original owner. This procedure uses DNS lookup tools to extract the CNAME value, allowing verification of takeover feasibility. It's typically used during reconnaissance phases against domains like grab.com to find exploitable subdomains such as cdn.grab.com. Prerequisites include internet access and basic DNS knowledge; no target credentials are needed.

## Requirements

1. Network access to public DNS resolvers
2. Installed DNS tools like dig
3. Target subdomain name (e.g., cdn.grab.com)

## Defense

Defensive measures and detection strategies:

- Monitor DNS records for dangling CNAMEs using automated tools like DNSdiff or certificate transparency logs
- Implement DNS monitoring alerts for changes to critical subdomains
- Regularly audit third-party service integrations and reclaim unused resources

## Objectives

1. Extract CNAME record for the target subdomain
2. Identify if it points to an external, potentially unclaimed service
3. Flag for further verification in takeover attempts

## Instructions

### Step 1: Query CNAME Record

**Context**: Use dig to perform a specific query for the CNAME record of the subdomain, focusing on authoritative responses.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig cdn.grab.com CNAME +short
```

> This command queries the DNS for the CNAME and outputs only the target (e.g., d1234567890.cloudfront.net). Successful output confirms the record; if none, the subdomain may not be vulnerable.

### Step 2: Full DNS Resolution

**Context**: If needed, get detailed resolution info to understand TTL and authoritative nameservers.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig cdn.grab.com
```

> Provides full DNS response including TTL, which helps assess propagation time for takeovers. Look for cloudfront.net in the ANSWER section.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/dig-cname-lookup]]

## Tools Used


## Tags

- [[DNS]]
- [[Reconnaissance]]
- [[subdomain-takeover]]

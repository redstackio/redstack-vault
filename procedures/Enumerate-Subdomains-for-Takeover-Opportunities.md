---
id: proc-enum-subdomains-takeover
tags:
  - subdomain-enumeration
  - reconnaissance
  - dns
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.325Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Enumerate Subdomains for Takeover Opportunities

## Summary

This procedure involves scanning a target domain to identify subdomains, focusing on those with DNS records pointing to third-party services that may be vulnerable to takeover due to misconfigurations.

## Description

In the context of subdomain takeover attacks, enumeration reveals subdomains like course.oberlo.com whose DNS (e.g., CNAME) points to services such as Kajabi. This step is crucial for reconnaissance to uncover potential dangling records where the third-party configuration is abandoned but DNS remains active, allowing attackers to claim control.

## Requirements

1. Access to DNS resolution tools like dig or online enumerators
2. Target domain name (e.g., oberlo.com)
3. Basic knowledge of DNS records

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated scanners
- Implement DNS monitoring for changes and third-party integrations
- Use services like DNSSEC to prevent unauthorized claims

## Objectives

1. Discover all subdomains associated with the target
2. Identify DNS pointers to external services
3. Flag potential takeover candidates

## Instructions

### Step 1: Perform Subdomain Enumeration

**Context**: Use passive or active methods to list subdomains, such as certificate transparency logs or brute-forcing.

No specific command provided; manually query or use tools like Sublist3r. For verification:

```bash
dig course.oberlo.com ANY
```

> This command queries all DNS records for the subdomain, revealing CNAME to Kajabi.

### Step 2: Analyze DNS Records

**Context**: Review results for third-party pointers.

Browse to the subdomain or use nslookup to confirm resolution.

```bash
nslookup course.oberlo.com
```

> Expected output shows IP or CNAME to Kajabi servers, indicating potential vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[subdomain-enumeration]]
- [[Reconnaissance]]

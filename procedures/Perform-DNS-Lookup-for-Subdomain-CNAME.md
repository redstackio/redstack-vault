---
id: proc-uuid-1
tags:
  - dns-recon
  - cname-discovery
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:39.855Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Perform-DNS-Lookup-for-Subdomain-CNAME

## Summary

This procedure uses DNS lookup tools to query a subdomain and reveal CNAME records that may indicate a dangling pointer to an unregistered domain, a key indicator for subdomain takeover vulnerabilities.

## Description

In subdomain takeover attacks, organizations often leave CNAME records pointing to third-party services after decommissioning them without removing the DNS entry. This procedure targets military or government subdomains (e.g., under .mil) to check for such misconfigurations. By resolving the subdomain, attackers can identify exploitable dangling records. Prerequisites include internet access and basic command-line knowledge. Expected outcomes: Identification of vulnerable CNAMEs leading to potential domain hijacking for malicious content hosting or traffic interception.

## Requirements

1. Internet-connected host with DNS resolution capabilities
2. Installation of dig tool (part of BIND utilities)
3. Target subdomain name (e.g., example-subdomain.mil)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or custom scripts
- Implement DNS monitoring with anomaly detection for unresolved CNAMEs
- Use domain monitoring services to alert on availability of referenced domains

## Objectives

1. Discover CNAME records in target subdomain DNS
2. Identify if the CNAME points to an external, potentially controllable domain
3. Gather evidence for takeover feasibility

## Instructions

### Step 1: Query Subdomain DNS Records

**Context**: Perform a comprehensive DNS lookup to retrieve all records, focusing on CNAMEs that may be dangling.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig example-subdomain.mil
```

> This command queries the DNS for the specified subdomain, returning sections like ANSWER (CNAME details) and AUTHORITY (SOA records). Look for a CNAME without a valid A record chain. Successful output includes the dangling target, e.g., CNAME to peosol-lg.example-domain.us.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[dns-recon]]
- [[subdomain-takeover]]

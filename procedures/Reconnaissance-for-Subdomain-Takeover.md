---
id: proc-recon-subdomain-takeover
tags:
  - reconnaissance
  - dns
  - subdomain-enumeration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T05:32:31.434Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Reconnaissance-for-Subdomain-Takeover

## Summary

This procedure involves enumerating subdomains of a target domain to identify potential takeover vulnerabilities, such as dangling DNS records pointing to unclaimed third-party services. It is a foundational step in subdomain takeover attacks, as seen in the OWOX kiosk.owox.com vulnerability.

## Description

In the context of the OWOX vulnerability, reconnaissance revealed that kiosk.owox.com was misconfigured, likely with a CNAME or NS record pointing to a service without proper authentication. This procedure uses DNS queries to map the attack surface, targeting web platforms where subdomains can be hijacked for malicious hosting or phishing. Expected outcomes include a list of subdomains and their DNS configurations, highlighting takeover candidates.

## Requirements

1. Internet access for DNS queries.
2. Basic knowledge of DNS records (CNAME, NS).
3. Target domain (e.g., owox.com).

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like DNS linter.
- Implement domain shadowing protections and monitor for unauthorized claims on third-party services.

## Objectives

1. Discover subdomains like kiosk.owox.com.
2. Identify misconfigurations for takeover potential.
3. Gather data for further verification.

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the target subdomain to retrieve its DNS records and identify any misconfigurations.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig kiosk.owox.com
```

> This command resolves the DNS for kiosk.owox.com, showing records like CNAME to a third-party service. Expected output includes authority and additional sections revealing unclaimed pointers.

### Step 2: Analyze Response

**Context**: Review the dig output for indicators of vulnerability, such as unresolved or dangling CNAMEs.

No command needed; manual inspection. Look for responses indicating the record points to a reclaimable resource.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- None

## Tags

- [[Reconnaissance]]
- [[DNS]]

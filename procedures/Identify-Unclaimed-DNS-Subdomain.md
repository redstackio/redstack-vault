---
id: proc-identify-unclaimed-dns
tags:
  - dns
  - recon
  - subdomain-takeover
type: procedure
tools: []
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T05:32:23.430Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Unclaimed DNS Subdomain

## Summary

This procedure detects subdomains with DNS records pointing to external services like DYN but lacking active configuration, enabling subdomain takeover attacks.

## Description

In a typical scenario, organizations configure DNS entries to delegate to third-party services (e.g., DYN) but fail to claim or set up the hostname, leaving it vulnerable. This procedure involves DNS resolution to identify such dangling records, confirming resolution to the service's infrastructure without hosted content. Prerequisites include public DNS access; outcomes reveal takeover opportunities leading to phishing or malware hosting.

## Requirements

1. Internet access for DNS queries
2. Knowledge of target domain and suspected DNS provider
3. DNS lookup tool like dig

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling delegations using automated scanners
- Implement monitoring for unclaimed hostnames on third-party platforms
- Use DNS security extensions (DNSSEC) to prevent unauthorized claims

## Objectives

1. Confirm DNS points to unconfigured external service
2. Identify potential takeover vectors
3. Document evidence for reporting

## Instructions

### Step 1: Perform DNS Resolution

**Context**: Query the subdomain's DNS to check for delegation to DYN infrastructure.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig web.mopub.com
```

> This command resolves the subdomain and displays NS or A records. Look for DYN-specific indicators like dyn.com nameservers or IPs in known DYN ranges. Expected output includes authority section pointing to DYN without CNAME or active hosts.

### Step 2: Validate Lack of Configuration

**Context**: Confirm no active content by attempting access and checking for default or error pages.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig +trace web.mopub.com
```

> The +trace option shows the full resolution path. Success if it delegates to DYN but returns no configured response.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used


## Tags

- [[DNS]]
- [[recon]]
- [[subdomain-takeover]]

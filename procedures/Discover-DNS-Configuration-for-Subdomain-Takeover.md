---
id: proc-uuid-001
name: Discover-DNS-Configuration-for-Subdomain-Takeover
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.315Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - dns
  - recon
  - subdomain-takeover
platforms:
  - Web
commands:
  - '[[commands/dig-lookup]]'
tools:
  - '[[tools/dig]]'
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---

# Discover-DNS-Configuration-for-Subdomain-Takeover

## Summary

This procedure identifies misconfigured DNS records, such as dangling CNAMEs pointing to unregistered cloud storage like AWS S3, enabling subdomain takeover attacks.

## Description

In scenarios where organizations configure subdomains to point to cloud services but fail to register the corresponding resources, attackers can discover these via DNS queries. This step reveals the CNAME chain, identifying potential takeover targets like unused S3 buckets. Prerequisites include public DNS access; expected outcome is a traceable DNS resolution path to a claimable endpoint.

## Requirements

1. Access to DNS resolution tools like dig
2. Target subdomain name (e.g., s3.shopify.com)
3. Internet connectivity for queries

## Defense

Defensive measures and detection strategies:

- Monitor DNS records for dangling CNAMEs using automated scanners
- Regularly audit cloud resource registrations matching DNS configs
- Implement DNSSEC to prevent unauthorized resolutions

## Objectives

1. Uncover DNS misconfigurations leading to takeover vectors
2. Map the resolution chain to cloud providers
3. Identify unregistered resources for exploitation

## Instructions

### Step 1: Perform Basic DNS Lookup

**Context**: Query the target subdomain to retrieve initial records.

**Command** ([[commands/dig-lookup]]):
```bash
dig s3.shopify.com +short
```

> This returns the immediate CNAME or A record. Look for AWS S3 patterns like *.s3.amazonaws.com.

### Step 2: Trace Full DNS Chain

**Context**: Follow the resolution path to detect endpoint details.

**Command** ([[commands/dig-trace]]):
```bash
dig s3.shopify.com +trace
```

> Outputs the full chain, e.g., s3.shopify.com -> shopify-assets.s3.amazonaws.com -> IP. Success if chain ends at a generic S3 IP without custom content.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/dig-lookup]]
- [[commands/dig-trace]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[recon]]
- [[subdomain-takeover]]

---
tags:
  - dns
  - cname
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
platforms:
  - Web
techniques:
  - '[[Gather Victim Org Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 666a008e-8319-45bc-9bec-35665c2cdf4b
created_at: '2025-12-14T05:32:31.145Z'
updated_at: '2025-12-14T05:32:31.145Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Org Information]]'
---
# Inspect-DNS-for-Subdomain-Takeover

## Summary

This procedure involves querying DNS records of target subdomains to identify misconfigurations like dangling CNAMEs pointing to cloud services such as AWS S3, which can enable subdomain takeover attacks.

## Description

In a subdomain takeover scenario, attackers scan for subdomains with CNAME records that resolve to non-existent resources in third-party services. For AWS S3, a CNAME like example.s3-website-us-east-1.amazonaws.com indicates static hosting intent. If the bucket is deleted without removing the DNS entry, the subdomain becomes hijackable. This procedure uses DNS lookup tools to detect such records, focusing on the target's infrastructure like websummit.net subdomains.

## Requirements

1. Internet access for public DNS queries
2. DNS resolution tools like dig installed
3. Knowledge of common cloud CNAME patterns (e.g., S3 endpoints)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated scanners like dnsdumpster or subjack
- Implement DNS monitoring alerts for changes to subdomain records
- Use domain registrar locks and multi-factor authentication for DNS management

## Objectives

1. Discover subdomains with cloud service CNAMEs
2. Identify potential takeover candidates
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Query Subdomain DNS

**Context**: Perform a DNS lookup to retrieve the CNAME record for the target subdomain.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig gameday.websummit.net +short
```

> This command outputs the CNAME target, such as gameday.websummit.net.s3-website-eu-west-1.amazonaws.com, confirming the S3 configuration.

### Step 2: Analyze Record Type

**Context**: Verify if the CNAME points to a known takeover-prone service like AWS S3.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig gameday.websummit.net CNAME
```

> Look for S3-specific patterns in the output to flag the subdomain as vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Org Information]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used


## Tags

- [[DNS]]
- [[recon]]

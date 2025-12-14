---
tags:
  - dns
  - reconnaissance
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Org Information]]'
updated_at: '2025-12-14T04:51:10.547Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 63faaa58-46cc-4d80-a40f-643a9c669e09
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Org Information]]'
---
# DNS Reconnaissance for Subdomain Takeover

## Summary

This procedure uses DNS queries to identify subdomains pointing to cloud services like AWS S3, revealing potential takeover opportunities if the associated bucket is unclaimed.

## Description

In subdomain takeover attacks, the first step is reconnaissance to check DNS records. A CNAME pointing to an S3 website endpoint (e.g., bucket.s3-website-us-east-1.amazonaws.com) without an active bucket indicates vulnerability. This procedure targets AWS S3 in US East 1, common for such misconfigurations, allowing attackers to claim the bucket and control the subdomain for malicious hosting.

## Requirements

1. Access to a DNS resolver tool like dig
2. Knowledge of the target subdomain
3. Internet connectivity for DNS queries

## Defense

Defensive measures and detection strategies:

- Monitor DNS records for dangling CNAMEs to cloud services
- Use automated tools like dnsdumpster or subjack to scan for takeover risks
- Implement DNSSEC to prevent unauthorized resolutions

## Objectives

1. Discover CNAME records linked to S3 endpoints
2. Identify unclaimed buckets for potential takeover
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Query Subdomain DNS

**Context**: Perform an A record lookup to reveal underlying CNAME chains pointing to S3.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig example-subdomain.target.com
```

> This command queries the DNS for the subdomain's A record, outputting the CNAME chain to s3-website-us-east-1.amazonaws.com if vulnerable. Expected output includes IP resolution and query details.

### Step 2: Analyze Response

**Context**: Review the dig output for S3 indicators.

No specific command; manually inspect for CNAME to *-website-us-east-1.amazonaws.com.

> Success if no active resolution errors but clear S3 pointer.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Org Information]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[Reconnaissance]]

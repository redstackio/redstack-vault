---
tags:
  - dns
  - recon
  - subdomain
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:38:49.163Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c767847c-ae8b-49b0-ba6c-887e4b1aa4f2
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
---

# Enumerate-Subdomain-DNS-Records

## Summary

This procedure involves querying DNS records for a target subdomain to identify misconfigurations, such as CNAMEs pointing to unclaimed cloud resources like AWS S3, enabling subdomain takeover opportunities.

## Description

In scenarios where a subdomain like media.vine.co has a DNS CNAME aliasing to a cloud service endpoint (e.g., vines.s3.amazonaws.com) without a corresponding claimed resource, attackers can detect this during reconnaissance. The procedure uses standard DNS lookup tools to reveal these records, highlighting mismatches that violate cloud provider rules, such as AWS S3 requiring a bucket name to match the custom domain.

## Requirements

1. Access to public DNS resolvers
2. Target subdomain name (e.g., media.vine.co)
3. Basic networking knowledge

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs
- Monitor for unclaimed cloud resources via automated scans
- Implement DNSSEC to prevent unauthorized changes

## Objectives

1. Identify CNAME records pointing to cloud services
2. Detect potential takeover vectors
3. Gather intelligence for further exploitation

## Instructions

### Step 1: Query CNAME Record

**Context**: Perform a DNS lookup to retrieve the CNAME for the subdomain, checking for cloud service aliases.

**Command** ([[commands/dig-dns-query]]):
```bash
dig media.vine.co CNAME
```

> This command queries the authoritative DNS server and outputs the alias record. Look for responses like "media.vine.co. 300 IN CNAME vines.s3.amazonaws.com." indicating a potential S3 mismatch.

### Step 2: Analyze Response

**Context**: Review the output for cloud provider indicators and name mismatches.

No specific command; manually inspect for AWS S3 patterns (e.g., *.s3.amazonaws.com) where the subdomain prefix doesn't match an existing bucket.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-query]]

## Tools Used


## Tags

- [[DNS]]
- [[recon]]
- [[subdomain]]

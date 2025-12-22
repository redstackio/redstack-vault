---
tags:
  - dns-recon
  - subdomain-takeover
  - aws
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:26.503Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 5ff73144-deb0-4577-acb4-c991505706aa
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover Subdomain Takeover with DNS Lookup

## Summary

This procedure uses DNS queries to identify subdomain takeover vulnerabilities where a CNAME record points to an orphaned or deleted cloud resource, such as an AWS S3 bucket, allowing potential hijacking.

## Description

In this attack scenario, attackers scan for subdomains with DNS records linking to non-existent services. For test.www.midigator.com, a CNAME chains to s3-website-us-west-1.amazonaws.com, indicating an unmanaged S3 bucket. This reconnaissance step uncovers the misconfiguration without alerting defenses, setting up for takeover. Prerequisites include basic networking knowledge and access to DNS tools; expected outcome is confirmation of an available resource for claiming.

## Requirements

1. Internet access for DNS queries
2. Installation of DNS lookup tools like dig
3. Target subdomain name (e.g., test.www.midigator.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs to deleted resources
- Use automated tools like Subjack or dnsdumpster to scan for takeover risks
- Implement DNS monitoring for anomalous resolutions

## Objectives

1. Identify misconfigured subdomains vulnerable to takeover
2. Gather evidence of orphaned cloud references
3. Prepare for resource claiming without direct interaction

## Instructions

### Step 1: Perform DNS Query

**Context**: Query the target's subdomain to retrieve CNAME and A records, revealing if it points to an external service like AWS S3.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig test.www.midigator.com
```

> This command performs a DNS lookup, outputting the ANSWER SECTION with CNAME records. Look for chains ending in s3-website-us-west-1.amazonaws.com, which suggests an S3 bucket reference. Successful output confirms the misconfiguration if the final A record points to AWS IPs without a live bucket.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[dns-recon]]
- [[subdomain-takeover]]

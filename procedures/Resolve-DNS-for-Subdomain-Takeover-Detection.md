---
tags:
  - dns-recon
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-a-record-lookup]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.397Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ab1c3e30-80cb-43b6-a52d-698d5f704deb
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Resolve-DNS-for-Subdomain-Takeover-Detection

## Summary

This procedure uses DNS queries to detect dangling records pointing to cloud services like AWS S3, identifying potential subdomain takeover opportunities.

## Description

In a subdomain takeover attack, attackers scan for DNS records that point to deleted or unclaimed cloud resources. By resolving the A record of a target subdomain, the CNAME chain reveals if it points to an S3 website endpoint. If unclaimed, the attacker can register the resource. This step is reconnaissance-focused and requires no privileges.

## Requirements

1. Access to a DNS resolver like Google's 8.8.8.8
2. Target subdomain name (e.g., a2.bime.io)
3. dig tool installed

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs to cloud providers
- Use automated tools like dnsdumpster or subjack to scan for takeovers
- Monitor for unexpected S3 bucket creations in your organization

## Objectives

1. Identify backend service (e.g., S3) via DNS
2. Confirm CNAME to cloud endpoint
3. Flag for further verification

## Instructions

### Step 1: Perform A Record Lookup

**Context**: Query the DNS to trace the subdomain's resolution path.

**Command** ([[commands/dig-dns-a-record-lookup]]):
```bash
dig A a2.bime.io @8.8.8.8
```

> This command queries Google's DNS for the A record, showing the CNAME chain to S3 and the IP address.

### Step 2: Analyze Output

**Context**: Parse the response for S3 indicators.

**Command** (Manual inspection):
No command needed; review output for 's3-website' in CNAME.

> Expected: CNAME bimeio.s3-website-us-east-1.amazonaws.com and IP in 52.216.0.0/15 range.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-a-record-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[dns-recon]]
- [[subdomain-takeover]]

---
id: proc-discover-s3-takeover
tags:
  - subdomain-takeover
  - dns
  - reconnaissance
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup-for-subdomain]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.852Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover Unclaimed S3 Subdomain via DNS Lookup

## Summary

This procedure uses DNS queries to identify subdomains with CNAME records pointing to unclaimed AWS S3 buckets, enabling subdomain takeover attacks by revealing dangling DNS configurations.

## Description

In this attack scenario, attackers scan target domains for subdomains like news-static.semrush.com where the CNAME chains to s3.amazonaws.com but no bucket exists. This allows claiming the subdomain for malicious hosting. Prerequisites include internet access and basic DNS knowledge; expected outcomes are confirmation of takeover eligibility, leading to phishing or XSS impacts on trusted domains.

## Requirements

1. Network access to public DNS resolvers (e.g., 8.8.8.8)
2. Installed DNS tool like dig
3. Target subdomain name (e.g., news-static.semrush.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or AWS CLI
- Monitor S3 bucket creations for sensitive names via CloudTrail
- Implement DNSSEC and subdomain monitoring alerts

## Objectives

1. Identify unclaimed S3 endpoints via DNS resolution
2. Confirm vulnerability for takeover
3. Gather evidence for reporting or exploitation

## Instructions

### Step 1: Perform DNS A Record Query

**Context**: Query the target's A record to reveal the CNAME chain and detect S3 pointers.

**Command** ([[commands/dig-dns-lookup-for-subdomain]]):
```bash
dig A news-static.semrush.com @8.8.8.8
```

> This command resolves the A record using Google's DNS server, showing the CNAME path. Expected output includes the chain to s3.amazonaws.com, indicating an unclaimed bucket if no custom content loads.

### Step 2: Verify Subdomain Access

**Context**: Attempt HTTP access to confirm the bucket is unclaimed.

**Instructions**: Open http://news-static.semrush.com in a browser; expect an AWS XML error like 'NoSuchBucket'.

> Success confirms the takeover opportunity.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domain

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup-for-subdomain]]

## Tools Used

- [[tools/dig]]

## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[aws-s3]]

---
tags:
  - dns
  - enumeration
  - cloudfront
  - s3
type: procedure
tools:
  - '[[tools/dig]]'
  - '[[tools/host]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-studio-redditinc-cname]]'
  - '[[commands/host-ns-s3-endpoint]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:13.055Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f194d909-d442-49f9-b6ef-86996efbde03
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
---

# DNS-Enumeration-to-Identify-S3-Bucket

## Summary

This procedure uses DNS queries to enumerate and identify an underlying AWS S3 bucket aliased behind a CloudFront distribution, enabling discovery of misconfigured storage resources.

## Description

In cloud environments, domains like studio.redditinc.com often resolve to CloudFront CDNs, which front S3 buckets. By querying CNAME and NS records, attackers can reverse-engineer the S3 bucket name (e.g., s3-r-w) and region (ap-east-1). This reconnaissance step is crucial for identifying exploitable misconfigurations like public write access, without direct interaction with AWS services. Prerequisites include basic DNS resolution tools and knowledge of AWS naming conventions.

## Requirements

1. Internet access for public DNS queries
2. DNS tools like dig or host installed
3. Target domain that uses CloudFront for S3 hosting

## Defense

Defensive measures and detection strategies:

- Implement DNS query logging and monitor for anomalous enumerations on CDN/S3 endpoints
- Use private DNS zones or restrict NS record exposure for internal cloud resources
- Regularly audit CloudFront origins for exposed S3 aliases

## Objectives

1. Resolve target domain to CloudFront CNAME
2. Derive S3 bucket name from regional endpoint NS records
3. Identify potential misconfigured buckets for further exploitation

## Instructions

### Step 1: Resolve Domain CNAME

**Context**: Query DNS to obtain the CloudFront distribution CNAME associated with the target domain.

**Command** ([[commands/dig-studio-redditinc-cname]]):
```bash
dig studio.redditinc.com
```

> This command performs a DNS lookup, revealing the CNAME d326d3e45wj426.cloudfront.net, indicating an AWS CDN-backed service.

### Step 2: Query S3 Endpoint NS Records

**Context**: Use the CloudFront ID to construct the S3 regional endpoint and query its NS records to alias the bucket name.

**Command** ([[commands/host-ns-s3-endpoint]]):
```bash
host -t ns d326d3e45wj426.s3.ap-east-1.amazonaws.com
```

> This reveals the alias s3-r-w.ap-east-1.amazonaws.com and authoritative AWS name servers, confirming the bucket name.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/dig-studio-redditinc-cname]]
- [[commands/host-ns-s3-endpoint]]

## Tools Used

- [[tools/dig]]
- [[tools/host]]

## Tags

- [[DNS]]
- [[enumeration]]
- [[aws]]
- [[cloudfront]]

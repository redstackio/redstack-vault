---
tags:
  - dns
  - reconnaissance
  - cname
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-check]]'
  - '[[commands/aws-bucket-check]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:39:01.930Z'
sub_techniques: []
id: 23bafd0a-9dcd-422d-89db-9e4dfc506739
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover Dangling CNAME Record

## Summary

This procedure identifies dangling DNS CNAME records pointing to unclaimed cloud resources, such as AWS S3 buckets, enabling subdomain takeover attacks.

## Description

In this attack scenario, query the target's DNS for subdomains to find CNAME records that point to decommissioned or unclaimed services like S3 buckets. Verify the resource's availability by attempting access; if unclaimed, it can be registered. This reconnaissance step uncovers misconfigurations from improper decommissioning without DNS cleanup, targeting environments with cloud integrations.

## Requirements

1. Access to DNS resolution tools like dig or nslookup
2. AWS CLI configured for bucket checks (optional but recommended)
3. Target subdomain suspected of misconfiguration

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like dnsdumpster or automated scripts
- Implement monitoring for unclaimed cloud resource attempts via AWS GuardDuty
- Use DNS security extensions (DNSSEC) to prevent unauthorized takeovers

## Objectives

1. Locate CNAME records pointing to cloud services
2. Confirm the pointed resource is unclaimed
3. Prepare for takeover by documenting the vulnerability

## Instructions

### Step 1: Query DNS for CNAME

**Context**: Resolve the subdomain to extract the CNAME target.

**Command** ([[commands/dig-cname-check]]):
```bash
dig CNAME storybook.lystit.com
```

> This command queries the DNS server for the CNAME record. Expected output includes the alias pointing to 'storybook.lystit.com' S3 endpoint.

### Step 2: Verify Bucket Availability

**Context**: Check if the S3 bucket is unclaimed by attempting a head request.

**Command** ([[commands/aws-bucket-check]]):
```bash
aws s3api head-bucket --bucket storybook.lystit.com 2>&1 | grep 'NoSuchBucket'
```

> If the bucket returns 'NoSuchBucket', it is unclaimed and available for creation. Success indicates a dangling record.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/dig-cname-check]]
- [[commands/aws-bucket-check]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[DNS]]
- [[Reconnaissance]]
- [[cname]]

---
id: uuid-1
tags:
  - aws-s3
  - bucket-creation
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-mb-create-bucket]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.160Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Unclaimed-AWS-S3-Bucket

## Summary

This procedure involves registering an unclaimed AWS S3 bucket using a subdomain name that resolves to an S3 endpoint, allowing an attacker to claim ownership and redirect traffic to their controlled storage.

## Description

In a subdomain takeover scenario, if a target's DNS records point a subdomain (e.g., delivery.yelp.com) to an AWS S3 service without a corresponding bucket, an attacker can create a bucket with that exact name. This exploits the cloud provider's naming uniqueness, enabling control over the subdomain's content. The procedure assumes the attacker has an AWS account and verifies the bucket is unclaimed via DNS resolution showing an S3 error.

## Requirements

1. AWS account with S3 bucket creation permissions
2. AWS CLI installed and configured with access keys
3. Target subdomain confirmed to resolve to unclaimed S3 endpoint (e.g., via dig delivery.yelp.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records and claim associated cloud resources (e.g., create S3 buckets preemptively)
- Monitor for new bucket creations with sensitive names using AWS CloudTrail logs
- Implement DNSSEC and strict subdomain policies to prevent dangling records

## Objectives

1. Gain ownership of the unclaimed S3 bucket matching the subdomain
2. Redirect subdomain traffic to attacker-controlled storage
3. Enable further exploitation like content hosting

## Instructions

### Step 1: Verify Unclaimed Bucket

**Context**: Confirm the subdomain points to an unclaimed S3 bucket by checking DNS resolution and attempting access, which should return a "NoSuchBucket" error.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig delivery.yelp.com
```

> This command resolves the subdomain's CNAME or A record, showing if it points to s3.amazonaws.com. Expected output includes S3 endpoint details.

### Step 2: Create the S3 Bucket

**Context**: Use AWS CLI to create the bucket with the exact subdomain name in the appropriate region (often us-east-1 for global access).

**Command** ([[commands/aws-s3-mb-create-bucket]]):
```bash
aws s3 mb s3://delivery.yelp.com --region us-east-1
```

> This creates the bucket. Expected output: "make_bucket: delivery.yelp.com". If the name is taken, the attack fails.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]
- [[commands/aws-s3-mb-create-bucket]]

## Tools Used


## Tags

- aws-s3
- bucket-creation

---
id: 123e4567-e89b-12d3-a456-426614174002
name: Claim Unconfigured AWS S3 Bucket
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.530Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - subdomain-takeover
  - aws-s3
  - bucket-claim
commands:
  - '[[commands/aws-create-s3-bucket]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Claim Unconfigured AWS S3 Bucket

## Summary

This procedure claims ownership of an unconfigured AWS S3 bucket by creating it with the exact name matching the dangling subdomain, redirecting traffic to the attacker's control.

## Description

Once a dangling S3 endpoint is identified, any AWS user can create a bucket with the subdomain's name (e.g., users.tweetdeck.com) in the appropriate region, instantly taking over the resolution. This grants full control over HTTP requests to the subdomain, as S3 serves content from the bucket.

## Requirements

1. AWS account with S3 create permissions
2. AWS CLI installed and configured with credentials
3. Knowledge of the target bucket name and region from DNS recon

## Defense

Defensive measures and detection strategies:

- Pre-provision all S3 buckets referenced in DNS
- Monitor AWS for bucket creations matching known subdomains
- Use AWS Organizations to restrict bucket naming

## Objectives

1. Create the matching S3 bucket
2. Configure for website hosting
3. Verify control redirection

## Instructions

### Step 1: Create the Bucket

**Context**: Use AWS CLI to make the bucket, ensuring the region matches the DNS endpoint.

**Command** ([[commands/aws-create-s3-bucket]]):
```bash
aws s3 mb s3://users.tweetdeck.com --region us-east-1
```

> Output: make_bucket: users.tweetdeck.com. Success if no naming conflict.

### Step 2: Enable Website Hosting

**Context**: Configure the bucket to serve static content.

**Command** ([[commands/aws-s3-website]]):
```bash
aws s3 website s3://users.tweetdeck.com --index-document index.html --region us-east-1
```

> This sets up the endpoint for HTTP access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/aws-create-s3-bucket]]
- [[commands/aws-s3-website]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[subdomain-takeover]]
- [[aws-exploit]]

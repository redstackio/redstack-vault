---
tags:
  - aws-s3
  - bucket-claim
  - initial-access
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-create-bucket]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:01.926Z'
sub_techniques: []
id: 9e116b6c-1d3d-46dd-898b-58d80c704708
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Unclaimed S3 Bucket

## Summary

This procedure claims an unclaimed AWS S3 bucket by creating it with a specific name derived from a dangling DNS record, establishing ownership for subdomain takeover.

## Description

Once a dangling CNAME is identified pointing to an unclaimed S3 bucket, use AWS credentials to create the bucket. S3 bucket names are globally unique, so if unclaimed, creation succeeds, redirecting the subdomain traffic to the attacker's controlled bucket. This targets AWS environments where resources were deleted without DNS updates.

## Requirements

1. AWS account with S3 create permissions
2. AWS CLI installed and configured with access keys
3. Exact bucket name from DNS CNAME

## Defense

Defensive measures and detection strategies:

- Monitor S3 bucket creation events via CloudTrail for suspicious names matching subdomains
- Automate DNS cleanup during resource decommissioning
- Use bucket naming policies to prevent subdomain-like names

## Objectives

1. Secure ownership of the unclaimed bucket
2. Enable redirection of subdomain traffic
3. Set stage for content hosting

## Instructions

### Step 1: Create the S3 Bucket

**Context**: Register the bucket to claim it before others can.

**Command** ([[commands/aws-create-bucket]]):
```bash
aws s3 mb s3://storybook.lystit.com --region us-east-1
```

> This makes a new bucket. Expected output: 'make_bucket: storybook.lystit.com'. Use us-east-1 for global DNS compatibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/aws-create-bucket]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[aws-s3]]
- [[bucket-claim]]
- [[initial-access]]

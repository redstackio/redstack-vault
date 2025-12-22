---
id: proc-uuid-2
tags:
  - cloud
  - s3
  - takeover
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
updated_at: '2025-12-14T04:38:39.719Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Dangling S3 Bucket

## Summary

This procedure claims control of a dangling S3 bucket by creating it with the exact name revealed in the discovery phase, in the us-east-1 region, thereby hijacking the associated subdomain.

## Description

Once the bucket name is known from the error response, an attacker with an AWS account can create the bucket if it's unclaimed. S3 bucket names are globally unique, so the first to create it gains control. The subdomain's DNS will then route traffic to the new bucket, allowing static content hosting under the legitimate domain.

## Requirements

1. AWS credentials with S3 create permissions
2. Installed and configured [[tools/AWS-CLI]]
3. Bucket name from prior discovery step

## Defense

Defensive measures and detection strategies:

- Reserve critical bucket names in all regions
- Monitor for unexpected S3 bucket creations via CloudTrail
- Use DNS monitoring tools to alert on resolution changes

## Objectives

1. Secure ownership of the dangling bucket name
2. Enable content serving on the subdomain
3. Prepare for content upload and verification

## Instructions

### Step 1: Create the Bucket

**Context**: Use AWS CLI to make the bucket in the specified region.

**Command** ([[commands/aws-create-bucket]]):
```bash
aws s3 mb s3://affirm-prod-www-cms█████████ --region us-east-1
```

> This creates the bucket. Expected output: 'make_bucket: affirm-prod-www-cms█████████'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/aws-create-bucket]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- cloud
- takeover
- s3

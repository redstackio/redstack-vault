---
id: proc-claim-s3-bucket
name: Claim Subdomain by Creating AWS S3 Bucket
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.667Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - aws-s3
  - initial-access
commands:
  - '[[commands/aws-create-s3-bucket]]'
  - '[[commands/aws-s3-website-config]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Claim Subdomain by Creating AWS S3 Bucket

## Summary

This procedure claims control of a dangling subdomain by creating an S3 bucket with the matching name, hijacking the DNS resolution since the CNAME now points to the attacker's resource.

## Description

Targeting AWS S3 misconfigurations, this step requires an AWS account and uses the exact bucket name from the dangling CNAME. Once created, the subdomain resolves to the attacker's bucket, granting full control. This is effective in cloud-heavy environments and can lead to impersonation or malicious hosting.

## Requirements

1. AWS account with permissions to create S3 buckets
2. AWS CLI installed and configured with access keys
3. Identified dangling bucket name from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Monitor for new S3 bucket creations matching known DNS aliases
- Use AWS Config rules to alert on unused DNS-cloud linkages
- Implement bucket naming policies to prevent squatting

## Objectives

1. Secure the subdomain by owning the underlying cloud resource
2. Enable static hosting on the hijacked domain
3. Establish persistence for further attacks

## Instructions

### Step 1: Create the S3 Bucket

**Context**: Instantiate the bucket using the subdomain-derived name to match the CNAME.

**Command** ([[commands/aws-create-s3-bucket]]):
```bash
aws s3 mb s3://happymondays.starbucks.com --region us-east-1
```

> Output: 'make_bucket: happymondays.starbucks.com'. Bucket is now yours if the name was available.

### Step 2: Configure Static Website Hosting

**Context**: Enable public website serving to make the subdomain functional for content delivery.

**Command** ([[commands/aws-s3-website-config]]):
```bash
aws s3 website s3://happymondays.starbucks.com --index-document index.html --error-document error.html
```

> Output confirms website configuration. Set bucket policy for public read if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/aws-create-s3-bucket]]
- [[commands/aws-s3-website-config]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[subdomain-takeover]]
- [[aws-s3]]
- [[initial-access]]

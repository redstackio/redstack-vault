---
tags:
  - aws-s3
  - bucket-takeover
  - cloud-misconfiguration
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-create-bucket]]'
  - '[[commands/aws-s3-upload-file]]'
platforms:
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 668ee841-05a4-4111-afdb-ecc2c9b3be29
created_at: '2025-12-14T04:51:26.419Z'
updated_at: '2025-12-14T04:51:26.419Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-via-AWS-S3-Bucket-Creation

## Summary

This procedure claims control of a subdomain by creating an unclaimed AWS S3 bucket that matches a dangling CNAME record, allowing the attacker to host arbitrary content.

## Description

Following discovery of a dangling CNAME (e.g., blog.gnipcentral.com pointing to testcloudfrontbug.s3-us-west-2.amazonaws.com), the attacker uses AWS credentials to create the exact bucket name in the specified region. Static website hosting is enabled, and content is uploaded to mirror the expected path. This redirects traffic from the trusted subdomain to the attacker's content, enabling phishing or defacement. Requires an AWS account; assumes the bucket name is globally unique and unclaimed.

## Requirements

1. Valid AWS IAM credentials with S3 create/upload permissions
2. Identified dangling CNAME with exact bucket name and region
3. AWS CLI installed and configured

## Defense

Defensive measures and detection strategies:

- Monitor for new S3 bucket creations matching known dangling records
- Implement bucket naming policies to avoid conflicts
- Use AWS Config rules to detect unclaimed buckets linked to domains

## Objectives

1. Secure control over the subdomain's resolution
2. Host malicious or proof-of-concept content
3. Demonstrate impact of the misconfiguration

## Instructions

### Step 1: Create the Matching S3 Bucket

**Context**: Instantiate the unclaimed bucket to intercept the CNAME traffic.

**Command** ([[commands/aws-s3-create-bucket]]):
```bash
aws s3 mb s3://testcloudfrontbug --region us-west-2
```

> This creates the bucket if unclaimed. Success confirms takeover feasibility.

### Step 2: Configure and Upload Content

**Context**: Enable website hosting and upload a file to the specified path for redirection.

**Command** ([[commands/aws-s3-upload-file]]):
```bash
aws s3 website s3://testcloudfrontbug --index-document index.html
echo '<h1>POC Takeover</h1>' > index.html
aws s3 cp index.html s3://testcloudfrontbug/asd/index.html
```

> Enables hosting and uploads content. The subdomain will now serve this file.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-create-bucket]]
- [[commands/aws-s3-upload-file]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[aws-s3]]
- [[bucket-takeover]]

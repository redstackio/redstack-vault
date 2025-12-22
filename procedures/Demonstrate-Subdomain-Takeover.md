---
tags:
  - subdomain-takeover
  - aws
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6d6f7bc7-bda9-448c-87eb-e9a8aa464117
created_at: '2025-12-14T04:51:10.528Z'
updated_at: '2025-12-14T04:51:10.528Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Subdomain Takeover

## Summary

This procedure simulates claiming a subdomain by creating the referenced AWS S3 bucket, gaining full control to host arbitrary content and demonstrating reputation risks.

## Description

Once verified, an attacker creates the exact S3 bucket name (e.g., 'uwn-images') in the specified region (us-west-1) and configures it as a static website. This redirects the CNAME traffic to attacker-controlled content, as in the Ubiquiti report where screenshots showed the error and potential for malicious hosting.

## Requirements

1. AWS account with S3 permissions
2. Bucket name from CNAME (e.g., uwn-images)
3. Region match (us-west-1)

## Defense

Defensive measures and detection strategies:

- Proactively create and lock S3 buckets matching DNS records
- Enable S3 bucket policies denying public creation
- Monitor DNS changes and S3 bucket creations via CloudTrail

## Objectives

1. Create and configure the S3 bucket
2. Upload proof-of-concept content
3. Verify subdomain serves attacker content

## Instructions

### Step 1: Create S3 Bucket

**Context**: Use AWS CLI to instantiate the bucket in the correct region.

**Command** (AWS CLI):
```bash
aws s3 mb s3://uwn-images --region us-west-1
```

> This creates the bucket if available; success indicates takeover possible.

### Step 2: Enable Static Website and Upload Content

**Context**: Configure hosting and add an index file.

**Command** (AWS CLI):
```bash
echo '<h1>PoC Takeover</h1>' > index.html
aws s3 website s3://uwn-images/ --index-document index.html --region us-west-1
aws s3 cp index.html s3://uwn-images/ --region us-west-1
```

> After propagation, access https://assets.goubiquiti.com to see the PoC page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[subdomain-takeover]]
- [[aws]]

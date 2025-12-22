---
tags:
  - aws-s3
  - bucket-takeover
  - cloud-misconfig
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.499Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ca7ee1e0-eaa0-42ee-81e2-861cdc9d82c7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Orphaned AWS S3 Bucket

## Summary

This procedure involves registering an available AWS S3 bucket that was previously deleted but still referenced in a DNS CNAME record, granting control over the associated subdomain.

## Description

Attackers exploit cloud misconfigurations where a subdomain's DNS points to a non-existent S3 bucket endpoint. By creating a new bucket with the exact name (e.g., test.www.midigator.com in us-west-1), the attacker can configure it for static hosting. This requires an AWS account and assumes the bucket name is unclaimed. The outcome is ownership of the resource, enabling further exploitation like content hosting. Target environment is AWS us-west-1; no prior access to the victim is needed.

## Requirements

1. Active AWS account with permissions to create S3 buckets
2. AWS CLI installed and configured with credentials
3. Knowledge of the exact bucket name from DNS recon (e.g., test.www.midigator.com)

## Defense

Defensive measures and detection strategies:

- Delete associated DNS records when decommissioning S3 buckets
- Monitor for new bucket creations matching known dangling references
- Use AWS Config rules to alert on orphaned DNS pointers

## Objectives

1. Secure control over the orphaned S3 resource
2. Enable static website hosting on the bucket
3. Bridge the gap between DNS and cloud control for subdomain hijacking

## Instructions

### Step 1: Create the S3 Bucket

**Context**: Use AWS CLI or console to instantiate the bucket, ensuring the region matches the DNS endpoint (us-west-1).

**Command**:
```bash
aws s3 mb s3://test.www.midigator.com --region us-west-1
```

> This creates the bucket if available. Expected output: "make_bucket: test.www.midigator.com". If it fails due to existence, the takeover is not possible.

### Step 2: Configure for Static Hosting

**Context**: Enable website hosting to allow public serving of content via the subdomain.

**Command**:
```bash
aws s3 website s3://test.www.midigator.com --index-document index.html --error-document error.html --region us-west-1
```

> This sets up the bucket as a static site. Expected output confirms configuration. Wait for DNS propagation (up to 60 seconds as per TTL).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[aws-s3]]
- [[bucket-takeover]]

---
tags:
  - aws
  - s3
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - AWS
  - Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 907bb2da-d178-4904-940a-14d6201d266e
created_at: '2025-12-14T05:32:31.167Z'
updated_at: '2025-12-14T05:32:31.167Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Unclaimed AWS S3 Bucket

## Summary

This procedure outlines claiming an unclaimed AWS S3 bucket identified via a dangling DNS CNAME record, allowing takeover of the associated subdomain for malicious hosting.

## Description

After identifying a dangling CNAME in DNS enumeration, this step involves using an AWS account to register the unclaimed S3 bucket. AWS allows creation of buckets with specific names if unclaimed. Once claimed, the DNS record now points to attacker-controlled storage, enabling content serving on the subdomain. This targets AWS environments where resources were deprovisioned without DNS cleanup. Prerequisites include an active AWS account; outcomes enable subdomain hijacking for phishing, SSRF, or policy bypass.

## Requirements

1. Active AWS account with S3 permissions
2. Identified unclaimed bucket name from DNS recon
3. AWS CLI or console access

## Defense

Defensive measures and detection strategies:

- Automate cleanup of DNS records upon resource deletion using IaC tools like Terraform
- Monitor for new S3 bucket creations matching known dangling patterns
- Use AWS GuardDuty to alert on anomalous bucket claims

## Objectives

1. Secure control over the unclaimed bucket
2. Redirect subdomain traffic to controlled storage
3. Prepare for hosting exploitative content

## Instructions

### Step 1: Verify Bucket Availability

**Context**: Confirm the bucket is unclaimed by attempting access or creation check.

No command; use AWS console to search for the bucket name. If it doesn't exist or is available, proceed.

> Expected: No existing bucket or 404 on access attempt.

### Step 2: Create and Claim Bucket

**Context**: Register the bucket in your AWS account.

Use AWS CLI or console: In console, navigate to S3 > Create bucket, enter the exact name from the CNAME (e.g., the-bucket-name.s3.amazonaws.com endpoint parsed).

```bash
aws s3 mb s3://unclaimed-bucket-name --region us-east-1
```

> This creates the bucket; adjust region as needed. Success: Bucket listed in your account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[aws]]
- [[s3]]
- [[subdomain-takeover]]

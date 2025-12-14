---
tags:
  - aws-s3
  - bucket-takeover
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
updated_at: '2025-12-14T04:38:39.985Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0dae60e4-558b-4402-842b-d7ed4c99baff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Dangling-AWS-S3-Bucket

## Summary

This procedure registers a deleted AWS S3 bucket matching a dangling DNS record, granting control over the associated subdomain for serving content.

## Description

When an S3 bucket is deleted without removing its DNS CNAME, anyone can create a bucket with the exact name (global namespace) to hijack traffic. This targets AWS's S3 service, requiring an AWS account with create permissions. The process uses the AWS Console or CLI to instantiate the bucket in the correct region (e.g., us-east-1). Outcomes include subdomain control, enabling malicious hosting; ethical use is for reporting only.

## Requirements

1. AWS account with S3 bucket creation permissions
2. Exact bucket name from DNS (e.g., assets.crossinstall.com)
3. Knowledge of S3 naming rules (lowercase, no underscores)

## Defense

Defensive measures and detection strategies:

- Audit and remove dangling DNS records post-resource deletion
- Use AWS Config rules to monitor unused buckets/DNS
- Enable S3 access logging and alert on unexpected creations

## Objectives

1. Secure control over the dangling resource
2. Demonstrate subdomain hijacking potential
3. Highlight cloud misconfiguration risks

## Instructions

### Step 1: Access AWS S3 Console

**Context**: Log in to AWS Management Console and navigate to S3 service.

**Command** (Manual via Console):
No CLI command; use web interface to create bucket.

> Enter bucket name 'assets.crossinstall.com', select us-east-1 region, unblock public access for demo, and create.

### Step 2: Confirm Bucket Endpoint

**Context**: Verify the new bucket's endpoint matches the DNS resolution.

**Command** (AWS CLI if available):
```bash
aws s3 ls s3://assets.crossinstall.com
```

> Expected: Bucket listed without errors, confirming claim success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

None

## Tools Used

None

## Tags

- [[subdomain-takeover]]
- [[aws-misconfig]]

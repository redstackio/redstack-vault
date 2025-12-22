---
tags:
  - s3-creation
  - infrastructure-compromise
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Web Services]]'
updated_at: '2025-12-14T04:38:49.383Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: b34f71ff-5d9e-42fd-8ff6-0253fd03a591
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Web Services]]'
---
# Create-S3-Bucket-for-Takeover

## Summary

This procedure creates an AWS S3 bucket with the exact name of the dangling DNS target to claim control of the subdomain.

## Description

S3 bucket names are globally unique. If unclaimed, anyone can create it in the matching region (US East 1 for this endpoint). This grants control over the DNS-resolved URL.

## Requirements

1. AWS account with S3 create permissions
2. Exact bucket name from DNS (e.g., a2.bime.io)
3. Correct region: US East (N. Virginia)

## Defense

Defensive measures and detection strategies:

- Pre-emptively create buckets for all DNS-pointed resources
- Monitor AWS for bucket creations matching DNS patterns
- Use IAM policies to restrict bucket naming

## Objectives

1. Secure the bucket name
2. Establish infrastructure control
3. Enable subsequent hosting

## Instructions

### Step 1: Create Bucket via Console

**Context**: Use AWS Management Console for creation.

Navigate to S3 > Create bucket > Enter 'a2.bime.io' > Select US East 1 > Uncheck ACLs if needed.

> Bucket created successfully.

### Step 2: Verify Creation

**Context**: Confirm via AWS CLI or console.

```bash
aws s3 ls s3://a2.bime.io
```

> Lists bucket if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Web Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[s3-creation]]
- [[infrastructure-compromise]]

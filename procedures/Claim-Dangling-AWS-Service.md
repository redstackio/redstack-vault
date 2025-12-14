---
id: proc-uuid-2
tags:
  - aws
  - cloud
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/aws-cli]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-create-s3]]'
verified: false
platforms:
  - Cloud (AWS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1583.001]]'
updated_at: '2025-12-14T05:32:23.077Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Claim Dangling AWS Service

## Summary

This procedure claims control over an unclaimed AWS resource (e.g., S3 bucket or CloudFront) referenced by a dangling DNS record, allowing takeover of the associated subdomain.

## Description

Targeting a dangling DNS record pointing to an AWS service no longer controlled by the domain owner (e.g., Mozilla), this procedure involves creating the exact resource name in your AWS account. The DNS will then resolve to your service. Prerequisites: AWS account and CLI setup. Expected outcome: Full control over the subdomain traffic.

## Requirements

1. AWS account with permissions to create S3/CloudFront
2. Knowledge of the dangling record's service type
3. AWS CLI installed

## Defense

Defensive measures and detection strategies:

- Monitor for new resource creations matching old DNS names
- Implement AWS Config rules for unused resources
- Regularly clean up deleted services' DNS entries

## Objectives

1. Provision the dangling service
2. Route subdomain traffic to controlled resource
3. Verify takeover

## Instructions

### Step 1: Identify Service Type

**Context**: From DNS query, note the service (e.g., S3 bucket name).

### Step 2: Create AWS Resource

**Context**: Use AWS CLI to create the resource matching the dangling name.

**Command** ([[commands/aws-create-s3]]):
```bash
aws s3 mb s3://dangling-bucket-name --region us-east-1
```

> Creates an S3 bucket. Expected output: Bucket created confirmation.

### Step 3: Configure Access

**Context**: Enable public access and website hosting if needed.

```bash
aws s3api put-bucket-policy --bucket dangling-bucket-name --policy file://policy.json
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1583.001]]

### Sub-Techniques


## Commands Used

- [[commands/aws-create-s3]]

## Tools Used

- [[tools/aws-cli]]

## Tags

- [[aws]]
- [[cloud]]

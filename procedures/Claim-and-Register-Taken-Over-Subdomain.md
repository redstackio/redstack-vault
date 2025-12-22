---
tags:
  - initial-access
  - aws
  - resource-claim
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-create-s3-bucket]]'
verified: false
platforms:
  - AWS
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 02223f03-8394-4c52-807c-4312d5757055
created_at: '2025-12-14T04:38:49.446Z'
updated_at: '2025-12-14T04:38:49.446Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim and Register Taken-Over Subdomain

## Summary

This procedure details how to claim control of a subdomain by registering the dangling resource on the provider's platform, such as creating an S3 bucket matching the DNS CNAME target.

## Description

Once a dangling DNS record is identified (e.g., CNAME to an AWS S3 endpoint), the attacker creates a new resource with the exact name on their own account, hijacking the subdomain resolution. This targets cloud misconfigurations in AWS environments. No target credentials are needed, only an attacker-controlled account on the service. Outcomes: Full DNS resolution to attacker's resource.

## Requirements

1. AWS account with permissions to create resources (e.g., S3 buckets)
2. AWS CLI installed and configured with access keys
3. Identified dangling record details from reconnaissance

## Defense

Defensive measures and detection strategies:

- Monitor for new resource creations matching known dangling DNS targets
- Use AWS Config rules to detect unused DNS pointers
- Implement least-privilege policies for resource naming

## Objectives

1. Create the matching resource on the service provider
2. Verify DNS now resolves to the new resource
3. Establish initial control over the subdomain

## Instructions

### Step 1: Prepare AWS Environment

**Context**: Ensure AWS CLI is set up for resource creation.

Run `aws configure` to set credentials if not already done.

### Step 2: Create the Resource

**Context**: Register the dangling endpoint by creating the bucket or equivalent.

**Command** ([[commands/aws-create-s3-bucket]]):
```bash
aws s3 mb s3://subdomain.mozaws.net --region us-east-1
```

> This creates an S3 bucket with the subdomain name. Expected output: "make_bucket: subdomain.mozaws.net". S3 names are globally unique, so if dangling, it's available.

### Step 3: Validate Claim

**Context**: Confirm the subdomain resolves to your resource.

Query DNS and access the endpoint; it should now be under your control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/aws-create-s3-bucket]]

## Tools Used


## Tags

- [[initial-access]]
- [[aws]]
- [[subdomain-takeover]]

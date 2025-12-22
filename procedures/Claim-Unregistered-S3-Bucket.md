---
id: proc-uuid-003
name: Claim-Unregistered-S3-Bucket
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.309Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - aws-s3
  - takeover
platforms:
  - AWS
commands:
  - '[[commands/aws-create-bucket]]'
tools:
  - '[[tools/aws-cli]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Claim-Unregistered-S3-Bucket

## Summary

This procedure registers an unregistered AWS S3 bucket in the attacker's account, hijacking control over any subdomain pointing to it.

## Description

Using an AWS account, create the bucket matching the dangling DNS CNAME. This grants full control over content served at the subdomain. Requires AWS credentials; outcomes include redirection of traffic to attacker-hosted files, enabling further exploits.

## Requirements

1. AWS account with S3 permissions
2. Installed AWS CLI
3. Bucket name from prior recon (e.g., shopify-assets)

## Defense

Defensive measures and detection strategies:

- Audit and delete unused DNS records
- Monitor AWS for unexpected bucket creations
- Use Route 53 or DNS providers with takeover alerts

## Objectives

1. Gain ownership of the S3 resource
2. Redirect subdomain traffic to attacker control
3. Enable content serving from hijacked domain

## Instructions

### Step 1: Configure AWS CLI

**Context**: Set up credentials for bucket creation.

**Command** ([[commands/aws-configure]]):
```bash
aws configure
```

> Enter access key, secret, region (e.g., us-east-1), output format.

### Step 2: Create the Bucket

**Context**: Register the bucket to claim it.

**Command** ([[commands/aws-create-bucket]]):
```bash
aws s3 mb s3://shopify-assets --region us-east-1
```

> Success: "make_bucket: shopify-assets".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/aws-configure]]
- [[commands/aws-create-bucket]]

## Tools Used

- [[tools/aws-cli]]

## Tags

- [[aws-s3]]
- [[takeover]]

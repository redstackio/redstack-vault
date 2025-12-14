---
tags:
  - aws-s3
  - bucket-claim
  - takeover
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-mb-create]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.157Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 481527b6-9368-4532-be25-cc0d138a6f32
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Claim-AWS-S3-Bucket

## Summary

This procedure creates an AWS S3 bucket with a name matching the vulnerable subdomain, effectively hijacking control due to the dangling DNS CNAME.

## Description

Once verified unclaimed, creating the bucket routes traffic from the subdomain to the attacker's S3 resource. Restrictions apply: Buckets for custom domains must be in specific regions like us-east-1 for www root access.

## Requirements

1. AWS account with S3 create permissions
2. AWS CLI configured
3. Bucket name from subdomain (e.g., media.vine.co)

## Defense

Defensive measures and detection strategies:

- Monitor DNS changes and claim buckets preemptively
- Use AWS Organizations to restrict bucket naming
- Alert on new bucket creations matching domains

## Objectives

1. Secure ownership of the subdomain
2. Enable content hosting on hijacked domain
3. Establish persistent access

## Instructions

### Step 1: Create the Bucket

**Context**: Initiate bucket creation in the appropriate region.

**Command** ([[commands/aws-s3-mb-create]]):
```bash
aws s3 mb s3://media.vine.co --region us-east-1
```

> Output: "make_bucket: media.vine.co". Wait for DNS propagation (TTL-dependent).

### Step 2: Verify Ownership

**Context**: Test access post-creation.

Use [[commands/aws-s3-ls-bucket-check]] again:

```bash
aws s3 ls s3://media.vine.co
```

> Now succeeds with empty list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-mb-create]]
- [[commands/aws-s3-ls-bucket-check]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[aws-s3]]
- [[bucket-claim]]
- [[takeover]]

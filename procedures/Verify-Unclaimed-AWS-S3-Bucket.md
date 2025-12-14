---
tags:
  - aws-s3
  - bucket
  - verification
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/aws-s3-ls-bucket-check]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:49.160Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bc9126c1-9e4e-4d26-8682-34a810b681be
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
---

# Verify-Unclaimed-AWS-S3-Bucket

## Summary

This procedure checks for the existence of an AWS S3 bucket matching a subdomain name, confirming if it's unclaimed and vulnerable to takeover due to DNS misconfigurations.

## Description

AWS S3 custom domains require a bucket with an exact name match to the CNAME. If a DNS record points to an S3 endpoint but no such bucket exists, anyone can claim it. This step uses AWS CLI to attempt listing the bucket, revealing its absence.

## Requirements

1. AWS CLI installed and configured with credentials
2. Subdomain-derived bucket name (e.g., media.vine.co)
3. Permissions to query S3 (read access not needed if unclaimed)

## Defense

Defensive measures and detection strategies:

- Proactively claim all potential buckets matching DNS records
- Use AWS Config to monitor bucket creations
- Scan for dangling DNS pointers regularly

## Objectives

1. Confirm bucket non-existence
2. Validate takeover feasibility
3. Prepare for claiming step

## Instructions

### Step 1: List Bucket Attempt

**Context**: Try to list objects in the presumed bucket to check existence.

**Command** ([[commands/aws-s3-ls-bucket-check]]):
```bash
aws s3 ls s3://media.vine.co
```

> Expect an error like "NoSuchBucket" or "AccessDenied" if unclaimed. Success if no error and empty list, but unclaimed typically errors.

### Step 2: Interpret Results

**Context**: Analyze the error to confirm unclaimed status.

Manual review: AWS errors indicate availability for creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-ls-bucket-check]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[aws-s3]]
- [[bucket]]
- [[verification]]

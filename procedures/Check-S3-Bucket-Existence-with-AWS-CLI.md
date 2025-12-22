---
tags:
  - aws
  - s3
  - recon
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/aws-s3-list-bucket]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:23:42.061Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9cbd4b15-467c-4262-aa17-d09728f66fb2
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Check-S3-Bucket-Existence-with-AWS-CLI

## Summary

This procedure uses AWS CLI to probe an S3 bucket's existence, confirming if it's unclaimed and available for hijacking in supply chain attacks.

## Description

The attacker runs an AWS CLI command to list objects in the target bucket, receiving a NoSuchBucket error that indicates it's unclaimed. This targets AWS environments and requires AWS credentials. Expected outcome: Confirmation of bucket availability for creation and payload upload, enabling RCE via installer hijacking.

## Requirements

1. AWS CLI installed and configured with credentials
2. Permissions to access S3 (read/list)
3. Target bucket name from script analysis

## Defense

Defensive measures and detection strategies:

- Pre-claim critical S3 buckets used in public scripts
- Log and alert on NoSuchBucket probes in AWS CloudTrail
- Implement bucket policies to prevent unauthorized creation

## Objectives

1. Verify bucket unclaimed status
2. Confirm public accessibility for claiming
3. Identify hijack opportunity

## Instructions

### Step 1: Run Bucket List Command

**Context**: Attempt to list bucket contents to check existence.

**Command** ([[commands/aws-s3-list-bucket]]):

```bash
aws s3 ls s3://rocketchatbuild
```

> If the bucket does not exist, outputs NoSuchBucket error, confirming it's unclaimed and can be created by anyone.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-list-bucket]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- s3
- recon

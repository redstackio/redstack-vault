---
tags:
  - s3
  - list
  - discovery
  - aws
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-s3-ls-list]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T05:32:13.049Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5e3eac1f-14d7-4375-8fc6-8ad26f290902
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
---

# List-Contents-of-S3-Bucket

## Summary

This procedure lists all objects in a publicly accessible AWS S3 bucket to verify control and scout for sensitive data.

## Description

After uploading files, listing the bucket contents confirms public read/list permissions and reveals existing files. In the Reddit case, it showed uploaded test files alongside non-sensitive marketing assets. This step aids in assessing impact, such as data exposure or further exploitation opportunities.

## Requirements

1. S3 bucket URI with public list access (s3://s3-r-w)
2. AWS CLI installed
3. Prior successful upload to validate

## Defense

Defensive measures and detection strategies:

- Block public list/get permissions in bucket policies
- Use S3 Inventory for internal auditing instead of public access
- Alert on unusual list operations via CloudWatch

## Objectives

1. Enumerate bucket objects to confirm access
2. Identify any sensitive or valuable data
3. Validate exploitation success post-upload

## Instructions

### Step 1: List Bucket Objects

**Context**: Retrieve a directory listing of all files in the S3 bucket.

**Command** ([[commands/aws-s3-ls-list]]):
```bash
aws s3 ls s3://s3-r-w
```

> Outputs a list of objects, including timestamps and sizes, verifying presence of uploaded files like dinesh.jpg.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-ls-list]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[s3]]
- [[Discovery]]
- [[aws]]
- [[listing]]

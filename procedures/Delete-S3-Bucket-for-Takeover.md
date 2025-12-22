---
tags:
  - s3
  - delete
  - takeover
  - aws
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/aws-s3-rb-delete]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Destruction]]'
updated_at: '2025-12-14T05:32:13.044Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a93dbb9c-8da5-49fa-93f9-5555ec45f6d6
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Data Destruction]]'
---
---

# Delete-S3-Bucket-for-Takeover

## Summary

This procedure demonstrates deleting a misconfigured S3 bucket to enable takeover, allowing an attacker to claim the name and associate it with malicious content.

## Description

If public delete permissions are enabled (rare but possible via policy misconfigs), attackers can remove the bucket entirely using AWS CLI. In this hypothetical for the s3-r-w bucket, deletion would disrupt the studio.redditinc.com service and allow recreation under attacker control, potentially hijacking the CloudFront origin. Not executed in the report, but highlights severe impact of write/delete access.

## Requirements

1. S3 bucket with public delete permissions
2. AWS CLI configured for the operation
3. Force flag for recursive deletion of contents

## Defense

Defensive measures and detection strategies:

- Explicitly deny s3:DeleteBucket and s3:DeleteObject in policies
- Enable MFA Delete and versioning to prevent accidental removals
- Monitor CloudTrail for delete API calls from unknown IPs

## Objectives

1. Remove existing bucket contents and structure
2. Enable bucket name squatting for persistence
3. Disrupt legitimate service access

## Instructions

### Step 1: Recursively Delete Bucket

**Context**: Force-remove the bucket and all objects to takeover the namespace.

**Command** ([[commands/aws-s3-rb-delete]]):
```bash
aws s3 rb s3://s3-r-w --force
```

> This recursively deletes objects first, then the bucket, confirming removal if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Data Destruction]] Data Destruction

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-rb-delete]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[s3]]
- [[deletion]]
- [[takeover]]
- [[aws]]

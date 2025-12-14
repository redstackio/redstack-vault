---
tags:
  - s3
  - upload
  - misconfiguration
  - aws
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-cp-upload]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.052Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4538acd6-f139-4422-ae4f-f54e03eff40f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
---

# Upload-Files-to-Misconfigured-S3-Bucket

## Summary

This procedure exploits public write permissions on an AWS S3 bucket to upload arbitrary files, demonstrating data tampering capabilities on misconfigured cloud storage.

## Description

Once the S3 bucket name (s3-r-w) is identified, attackers can use AWS CLI to upload files without authentication if the bucket policy allows public writes. In this scenario, files like images and HTML were uploaded to studio.redditinc.com's bucket, which contained non-sensitive marketing content. This can lead to defacement, malware hosting, or further chaining attacks. Requires AWS CLI configured, but exploits rely on the bucket's improper access controls.

## Requirements

1. Identified S3 bucket URI (s3://s3-r-w)
2. AWS CLI installed and optionally configured (public write bypasses auth)
3. Local files to upload (e.g., test images or scripts)

## Defense

Defensive measures and detection strategies:

- Enforce bucket policies denying public writes (use IAM conditions)
- Enable S3 access logging and monitor for unauthorized uploads via CloudTrail
- Scan buckets regularly with tools like Prowler for public access

## Objectives

1. Upload arbitrary files to gain persistence or tamper data
2. Verify write access on the misconfigured bucket
3. Potentially host malicious content via the fronting CloudFront

## Instructions

### Step 1: Copy Local File to Bucket

**Context**: Transfer a local file to the S3 bucket to test and exploit write permissions.

**Command** ([[commands/aws-s3-cp-upload]]):
```bash
aws s3 cp dinesh.jpg s3://s3-r-w
```

> This uploads the file dinesh.jpg, confirming success if no permission errors occur. Repeat for other files like dinesh.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-cp-upload]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[s3]]
- [[upload]]
- [[aws]]
- [[exploitation]]

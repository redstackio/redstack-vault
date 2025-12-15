---
id: proc-uuid-1
tags:
  - aws
  - s3
  - public-access
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-ls-root]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.513Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Public-S3-Bucket-URL

## Summary

This procedure demonstrates initial access to a misconfigured AWS S3 bucket by directly accessing its public URL, allowing unauthenticated viewing of contents without any credentials.

## Description

In scenarios where an S3 bucket is incorrectly set to public read access, attackers can navigate to the bucket's HTTPS endpoint to browse and download files. This targets cloud storage misconfigurations common in environments like the U.S. Department of Defense, exposing sensitive data in root and subdirectories. Prerequisites include only internet access; no AWS account is needed.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Known public S3 bucket URL (e.g., https://██████.s3.amazonaws.com/)
3. No authentication or VPN required

## Defense

Defensive measures and detection strategies:

- Regularly audit S3 bucket policies using AWS Config or IAM Access Analyzer to disable public access
- Enable S3 Block Public Access at account and bucket levels
- Monitor CloudTrail logs for anonymous GetObject API calls

## Objectives

1. Verify unauthenticated access to the bucket
2. Identify exposed directory structure
3. Prepare for deeper enumeration

## Instructions

### Step 1: Navigate to Public URL

**Context**: Directly access the S3 bucket endpoint to confirm public readability.

**Command** ([[commands/aws-s3-ls-root]]):
```bash
# No command needed for browser access; use URL: https://██████.s3.amazonaws.com/
```

> Open the URL in a browser. Successful access shows a listing of bucket contents. If redirected or denied, the bucket is not public.

### Step 2: Browse Root Contents

**Context**: Inspect initial files to gauge sensitivity.

**Command** (Browser Navigation):
```bash
# Manually click into directories like admin or production
```

> Expected output includes visible files such as manuals and media. Download any item to validate access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-ls-root]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- s3
- initial-access

---
id: proc-verify-s3-upload
name: Verify Control by Uploading Files to S3 Bucket
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.661Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Remote File Copy]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - aws-s3
  - execution
commands:
  - '[[commands/aws-s3-cp-upload]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---

# Verify Control by Uploading Files to S3 Bucket

## Summary

This procedure uploads test files to the claimed S3 bucket and accesses them via the subdomain URL to confirm ownership and functionality for arbitrary content hosting.

## Description

After claiming the bucket, uploading files demonstrates control, as the subdomain now serves content from the attacker's storage. This verifies the takeover and enables further exploitation like phishing pages. Targets AWS S3 with website hosting enabled.

## Requirements

1. Owned S3 bucket from prior step
2. AWS CLI configured
3. Local files prepared for upload (e.g., HTML proof-of-concept)

## Defense

Defensive measures and detection strategies:

- Monitor S3 access logs for unexpected uploads
- Set bucket policies to require MFA for critical actions
- Use AWS GuardDuty to detect anomalous bucket activity

## Objectives

1. Confirm subdomain resolution to attacker's bucket
2. Validate content serving capability
3. Enable malicious payload deployment

## Instructions

### Step 1: Prepare and Upload Files

**Context**: Create simple files and sync them to the bucket root to test accessibility.

**Command** ([[commands/aws-s3-cp-upload]]):
```bash
echo "<h1>Proof of Takeover</h1>" > index.html
echo "Test file content" > poc.txt
aws s3 cp index.html s3://happymondays.starbucks.com/
aws s3 cp poc.txt s3://happymondays.starbucks.com/
```

> Output: 'upload: index.html to s3://...'. Files are now in the bucket.

### Step 2: Access via Subdomain

**Context**: Browse to the subdomain to load the uploaded content, confirming control.

No command needed; use a web browser to visit http://happymondays.starbucks.com/index.html and verify the page displays.

> Expected: Custom HTML loads, proving takeover success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-cp-upload]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[subdomain-takeover]]
- [[aws-s3]]
- [[Execution]]

---
id: proc-uuid-execute-takeover
tags:
  - subdomain-takeover
  - aws-s3
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-create-bucket]]'
  - '[[commands/aws-s3-upload-file]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.834Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Subdomain-Takeover-via-S3

## Summary

This procedure executes the takeover of a vulnerable subdomain by claiming the unused AWS S3 bucket and configuring it to demonstrate control.

## Description

Once a dangling S3 bucket is confirmed, an attacker with an AWS account can create the bucket, upload content, and hijack the subdomain's traffic. This grants control for hosting phishing pages or spoofing legitimate content, potentially damaging reputation. The attack relies on the DNS propagation delay and assumes ethical disclosure post-exploitation. Requires AWS CLI setup with valid credentials.

## Requirements

1. AWS account with S3 permissions.
2. Installed AWS CLI.
3. Vulnerable bucket name from prior steps.

## Defense

Defensive measures and detection strategies:

- Rotate and monitor S3 bucket names in DNS.
- Use AWS IAM policies to restrict public bucket creation.
- Detect anomalous uploads via S3 access logs.

## Objectives

1. Claim ownership of the unused bucket.
2. Redirect subdomain traffic to attacker-controlled content.
3. Enable follow-on attacks like phishing.

## Instructions

### Step 1: Create the S3 Bucket

**Context**: Register the dangling bucket name to gain control.

**Command** ([[commands/aws-s3-create-bucket]]):
```bash
aws s3 mb s3://bucket-name --region us-east-1
```

> This creates the bucket. Expected output: 'make_bucket: bucket-name' confirmation.

### Step 2: Upload Proof-of-Control Content

**Context**: Serve custom content to verify takeover.

**Command** ([[commands/aws-s3-upload-file]]):
```bash
aws s3 cp index.html s3://bucket-name/
```

> Upload an HTML file with a message like 'Subdomain Taken Over'. Expected output: Upload complete; access via subdomain URL to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-create-bucket]]
- [[commands/aws-s3-upload-file]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[exploitation]]

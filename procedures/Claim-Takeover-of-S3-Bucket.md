---
id: proc-uuid-9012
tags:
  - subdomain-takeover
  - aws-s3
  - bucket-hijacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.673Z'
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
# Claim Takeover of S3 Bucket

## Summary

This procedure demonstrates claiming an orphaned AWS S3 bucket name exposed by a dangling DNS record, allowing control over the associated subdomain for malicious purposes.

## Description

When a DNS record points to a deleted S3 bucket, the bucket name becomes available for registration. An attacker with an AWS account can create the bucket, configure it for static hosting, and inherit traffic intended for the original domain. This leads to impersonation risks, as seen in the s3.websummit.net case where the record pointed to dws-content.s3-website-eu-west-1.amazonaws.com. Prerequisites include an AWS account with S3 permissions in the relevant region (eu-west-1).

## Requirements

1. Valid AWS account with S3 create permissions
2. Identified dangling bucket name from prior reconnaissance
3. Access to AWS CLI or console

## Defense

Defensive measures and detection strategies:

- Delete DNS records immediately upon resource deletion
- Monitor for new bucket creations with sensitive names via AWS CloudTrail
- Use S3 bucket naming policies to reserve critical names

## Objectives

1. Secure ownership of the exposed bucket name
2. Redirect subdomain traffic to attacker-controlled content
3. Enable further exploitation like content injection

## Instructions

### Step 1: Verify Bucket Availability

**Context**: Confirm the bucket name is unclaimed by attempting creation or using AWS API checks.

**Command**:
```bash
aws s3api head-bucket --bucket s3.websummit.net --region eu-west-1
```

> If it returns 404 NoSuchBucket, the name is available. Proceed to creation.

### Step 2: Create and Configure Bucket

**Context**: Create the S3 bucket and enable static website hosting to match the DNS setup.

**Command**:
```bash
aws s3 mb s3://s3.websummit.net --region eu-west-1
aws s3 website s3://s3.websummit.net/ --index-document index.html --error-document error.html
```

> Bucket is now created and configured. Set public ACL if needed for hosting.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[aws-s3]]
- [[bucket-hijacking]]

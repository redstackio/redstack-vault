---
tags:
  - aws-s3
  - file-upload
  - poc
type: procedure
tools:
  - '[[tools/aws-cli]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/aws-s3-upload-file]]'
platforms:
  - AWS
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5a50b62e-5613-4f16-984d-111a2705a818
created_at: '2025-12-14T05:32:24.295Z'
updated_at: '2025-12-14T05:32:24.295Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-POC-Content-to-S3-Bucket

## Summary

This procedure uploads proof-of-concept files to the hijacked S3 bucket, making them publicly accessible to demonstrate subdomain control.

## Description

With the bucket created, upload HTML or other files and set public-read ACL. This enables the subdomain to serve attacker-controlled content, simulating phishing or defacement. For gameday.websummit.net, a simple index.html proves the takeover.

## Requirements

1. Created S3 bucket with website hosting enabled
2. Local POC file prepared (e.g., HTML page)
3. AWS CLI access

## Defense

Defensive measures and detection strategies:

- Enforce bucket policies denying public access by default
- Scan S3 uploads for malicious content using AWS GuardDuty
- Alert on unexpected public ACL changes

## Objectives

1. Deploy demonstrable malicious content
2. Enable public serving via S3
3. Validate content delivery over subdomain

## Instructions

### Step 1: Prepare and Upload File

**Context**: Copy a local POC file to the bucket with public permissions.

**Command** ([[commands/aws-s3-upload-file]]):
```bash
aws s3 cp poc.html s3://gameday.websummit.net/ --region eu-west-1 --acl public-read
```

> Uploads the file as index.html equivalent for root access.

### Step 2: Set Bucket Policy for Public Access

**Context**: Ensure the bucket policy allows GetObject for anonymous users.

**Command** ([[commands/aws-s3-upload-file]]):
```bash
echo '{"Version":"2012-10-17","Statement":[{"Sid":"PublicRead","Effect":"Allow","Principal":"*","Action":"s3:GetObject","Resource":"arn:aws:s3:::gameday.websummit.net/*"}]}' | aws s3api put-bucket-policy --bucket gameday.websummit.net --policy file://policy.json --region eu-west-1
```

> Applies policy to make content publicly viewable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-upload-file]]

## Tools Used

- [[tools/aws-cli]]

## Tags

- [[aws-s3]]
- [[file-upload]]

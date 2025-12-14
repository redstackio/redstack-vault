---
tags:
  - aws-s3
  - bucket-creation
type: procedure
tools:
  - '[[tools/aws-cli]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-create-bucket]]'
platforms:
  - AWS
techniques:
  - '[[Create Account]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Local Account]]'
id: b2af50bd-0b39-42a4-ba1e-de5ebb16713f
created_at: '2025-12-14T05:32:31.138Z'
updated_at: '2025-12-14T05:32:31.138Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Create Account]]'
---
# Create-Malicious-AWS-S3-Bucket

## Summary

This procedure creates a new AWS S3 bucket using a name derived from a dangling DNS CNAME, allowing the attacker to claim control over the associated subdomain.

## Description

Bucket names in S3 are globally unique, so a deleted bucket's name becomes available. By creating a bucket named gameday.websummit.net in eu-west-1, the attacker hijacks the resolution. Enable static website hosting post-creation for full takeover.

## Requirements

1. AWS account with S3 create permissions
2. AWS CLI configured with credentials
3. Target bucket name availability confirmed

## Defense

Defensive measures and detection strategies:

- Reserve critical bucket names in a holding account
- Monitor CloudTrail for S3 bucket creations matching domain patterns
- Use AWS Organizations to restrict bucket naming

## Objectives

1. Secure the dangling bucket name
2. Prepare for content hosting
3. Establish subdomain control foundation

## Instructions

### Step 1: Create the Bucket

**Context**: Use AWS CLI to make the bucket in the specific region.

**Command** ([[commands/aws-s3-create-bucket]]):
```bash
aws s3 mb s3://gameday.websummit.net --region eu-west-1
```

> Success returns a confirmation; failure indicates name taken.

### Step 2: Enable Website Hosting

**Context**: Configure the bucket for static website serving.

**Command** ([[commands/aws-s3-create-bucket]]):
```bash
aws s3 website s3://gameday.websummit.net --index-document index.html --region eu-west-1
```

> This sets up the endpoint to match the CNAME.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Create Account]]

### Sub-Techniques

- [[Local Account]]

## Commands Used

- [[commands/aws-s3-create-bucket]]

## Tools Used

- [[tools/aws-cli]]

## Tags

- [[aws-s3]]
- [[bucket-creation]]

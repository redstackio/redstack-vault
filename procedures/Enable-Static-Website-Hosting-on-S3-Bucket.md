---
tags:
  - aws-s3
  - static-hosting
  - execution
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/aws-enable-website-hosting]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T04:39:01.914Z'
sub_techniques: []
id: 76bcc884-8208-4977-a821-ce0125c199c0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Enable Static Website Hosting on S3 Bucket

## Summary

This procedure configures an S3 bucket for static website hosting, allowing it to serve HTTP content via the hijacked subdomain CNAME.

## Description

After claiming the bucket, enable static website hosting to make it respond to HTTP requests on port 80, mimicking a web server. This requires setting index and error documents and ensuring public read access. In the attack, this bridges the DNS CNAME to serve attacker content on the subdomain.

## Requirements

1. Owned S3 bucket
2. AWS CLI access
3. Basic HTML files for index/error (create if needed)

## Defense

Defensive measures and detection strategies:

- Restrict S3 public access policies
- Monitor configuration changes via AWS Config
- Audit website hosting enables on subdomain-named buckets

## Objectives

1. Activate HTTP serving capability
2. Align with CNAME for subdomain resolution
3. Prepare for content delivery

## Instructions

### Step 1: Configure Website Hosting

**Context**: Set the bucket to host static sites.

**Command** ([[commands/aws-enable-website-hosting]]):
```bash
aws s3 website s3://storybook.lystit.com --index-document index.html --error-document error.html
```

> This enables hosting. Expected output: Configuration details. Ensure bucket policy allows s3:GetObject for public access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (adapted for cloud config)

### Sub-Techniques


## Commands Used

- [[commands/aws-enable-website-hosting]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[aws-s3]]
- [[static-hosting]]
- [[Execution]]

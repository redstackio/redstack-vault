---
id: proc-s3-host-poc-001
tags:
  - aws-s3
  - phishing-poc
  - content-hosting
type: procedure
tools:
  - '[[tools/AWS-S3]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:38:39.690Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host Proof-of-Concept Content on S3 Origin

## Summary

This procedure uploads and configures malicious content, such as a fake login page, to an S3 bucket serving as the origin for the hijacked CloudFront distribution, demonstrating content control.

## Description

Once the domain is claimed, attackers host phishing assets on S3 to impersonate legitimate sites. This targets AWS storage, enabling delivery of arbitrary HTML/JS for credential theft via the subdomain.

## Requirements

1. AWS S3 bucket configured as CloudFront origin
2. HTML file for PoC (e.g., fake login)
3. Public read access on bucket

## Defense

Defensive measures and detection strategies:

- Enable S3 bucket versioning and MFA delete
- Monitor S3 access logs for unauthorized uploads
- Use AWS WAF to block suspicious content patterns

## Objectives

1. Upload PoC files to origin
2. Verify serving via subdomain
3. Enable phishing simulation

## Instructions

### Step 1: Create and Configure S3 Bucket

**Context**: Set up the bucket if not done, and make it public.

In [[tools/AWS-S3]], create bucket 'attacker-poc-bucket', enable static website hosting, and set bucket policy for public read.

### Step 2: Upload Content

**Context**: Add the fake login page.

Upload via console or CLI:

```bash
aws s3 cp login.html s3://attacker-poc-bucket/login.html --acl public-read
```

> Access http://partners.ubnt.com/login to see the page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-S3]]

## Tags

- [[tools/AWS-S3]]
- [[phishing-poc]]

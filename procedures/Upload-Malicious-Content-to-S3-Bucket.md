---
id: proc-upload-to-s3
tags:
  - subdomain-takeover
  - aws-s3
  - malware-distribution
  - phishing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:51:26.846Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload Malicious Content to S3 Bucket

## Summary

This procedure involves uploading arbitrary files to a claimed S3 bucket, allowing attackers to host phishing sites, XSS payloads, or malware under a trusted subdomain.

## Description

Once the bucket is claimed, files uploaded become accessible via the subdomain (e.g., http://news-static.semrush.com/poc.html), exploiting the *.semrush.com trust for attacks like cross-origin policy bypasses. Targets web/cloud environments; outcomes include content delivery for phishing or malware. Requires AWS credentials post-claim.

## Requirements

1. Claimed S3 bucket with public access
2. AWS CLI configured or console access
3. Malicious file prepared (e.g., HTML with XSS)

## Defense

Defensive measures and detection strategies:

- Scan for subdomain takeovers using tools like Subjack
- Monitor S3 access logs for anomalous uploads
- Enforce bucket naming policies and WAF rules

## Objectives

1. Transfer malicious payloads to the bucket
2. Make content publicly accessible
3. Demonstrate impact like XSS or phishing

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create content exploiting the subdomain trust.

**Instructions**: Craft poc.html with phishing form or <script>alert('XSS')</script> for proof-of-concept.

> Save as poc.html locally.

### Step 2: Upload via AWS Console or CLI

**Context**: Ingest the file into the public bucket.

**Instructions**: In S3 console, select bucket, upload poc.html, set ACL to public-read. Or via CLI:

```bash
aws s3 cp poc.html s3://news-static.semrush.com/poc.html --acl public-read
```

> Assumes AWS CLI installed and configured with `aws configure`.

### Step 3: Verify Upload and Impact

**Context**: Test accessibility and attack viability.

**Instructions**: Access http://news-static.semrush.com/poc.html; confirm load and execute (e.g., alert pops for XSS).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[aws-s3]]
- [[xss]]
- [[Phishing]]

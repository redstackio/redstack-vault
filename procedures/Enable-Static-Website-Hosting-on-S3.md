---
id: uuid-3
tags:
  - aws-s3
  - static-hosting
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-s3-website-enable]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.142Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable-Static-Website-Hosting-on-S3

## Summary

This procedure configures an S3 bucket for static website hosting, allowing the uploaded malicious content to be served publicly over the website endpoint, completing the subdomain takeover.

## Description

S3 buckets can be enabled as static websites, exposing content via a special endpoint (e.g., bucket.s3-website-region.amazonaws.com). This makes the malicious HTML accessible, and if the subdomain's DNS points to S3, it effectively hijacks the subdomain for serving attacker content, leading to impersonation.

## Requirements

1. S3 bucket with uploaded content
2. AWS CLI access
3. Bucket policy allowing public read access

## Defense

Defensive measures and detection strategies:

- Disable static website hosting on non-production buckets
- Monitor S3 access logs for unexpected website endpoint traffic
- Use Route 53 or DNS monitoring to detect takeovers promptly

## Objectives

1. Activate static hosting on the bucket
2. Serve malicious content via S3 website endpoint
3. Achieve full subdomain control for phishing

## Instructions

### Step 1: Set Bucket Policy for Public Access

**Context**: Ensure the bucket allows public reads for website serving.

**Command** (policy application):
```bash
aws s3api put-bucket-policy --bucket delivery.yelp.com --policy file://public-policy.json
```

> Assumes a JSON policy file with public read permissions. Expected output: Policy applied successfully.

### Step 2: Enable Website Hosting

**Context**: Configure the bucket as a static website with index.html as the default document.

**Command** ([[commands/aws-s3-website-enable]]):
```bash
aws s3 website s3://delivery.yelp.com --index-document index.html
```

> Enables hosting. Expected output: Website endpoint URL provided. Test by curling the endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/aws-s3-website-enable]]

## Tools Used


## Tags

- aws-s3
- static-hosting

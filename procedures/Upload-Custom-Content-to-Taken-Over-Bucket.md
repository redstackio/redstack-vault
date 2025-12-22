---
tags:
  - s3-upload
  - malicious-content
type: procedure
tools: []
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
updated_at: '2025-12-14T04:38:39.983Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 54adc797-7dfc-449c-bd6f-b57ab13afef1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Custom-Content-to-Taken-Over-Bucket

## Summary

This procedure uploads arbitrary files to a hijacked S3 bucket, allowing the subdomain to serve custom or malicious content to visitors.

## Description

Post-takeover, S3 buckets can host static websites or files publicly. This involves uploading an index.html or other files via Console/CLI, setting public read ACLs. In attacks, this enables phishing, malware, or defacement; for reporting, use benign proofs like comments. Targets AWS S3; requires prior bucket control. Outcomes: Subdomain serves attacker content, risking TLS cert issuance or whitelist bypass.

## Requirements

1. Control of the S3 bucket
2. File to upload (e.g., index.html with proof)
3. Public access enabled on bucket

## Defense

Defensive measures and detection strategies:

- Restrict S3 public access policies
- Monitor bucket uploads via CloudTrail logs
- Scan for anomalous content on subdomains

## Objectives

1. Demonstrate full subdomain control
2. Serve proof-of-concept content
3. Simulate malicious payload delivery

## Instructions

### Step 1: Prepare Content File

**Context**: Create a simple HTML file with identifiable content for verification.

**Command** (Local file creation):
```bash
echo '<!-- hackerone/ian bugcrowd/iangcarroll -->' > index.html
```

> This generates a minimal file for upload.

### Step 2: Upload to Bucket

**Context**: Transfer the file to S3 root for subdomain serving.

**Command** (AWS CLI):
```bash
aws s3 cp index.html s3://assets.crossinstall.com/
```

> Expected: Upload complete; set ACL if needed: aws s3api put-object-acl --bucket assets.crossinstall.com --key index.html --acl public-read.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques

- None

## Commands Used

None

## Tools Used

None

## Tags

- [[content-upload]]
- [[s3-hijack]]

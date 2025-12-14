---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Access-Public-AWS-S3-Bucket
tags:
  - aws
  - s3
  - information-disclosure
  - cloud-misconfig
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-s3-bucket]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:24:47.374Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
---
---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Access-Public-AWS-S3-Bucket
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T12:00:00Z
updated_at: 2023-10-01T12:00:00Z
tactics: [[Initial Access]], [[Collection]]
techniques: [[Exploit Public-Facing Application]], [[Data from Cloud Storage]]
sub_techniques: []
tags: aws, s3, information-disclosure, cloud-misconfig
commands: [[commands/curl-access-s3-bucket]]
platforms: AWS, Cloud
tools: []
---

# Access-Public-AWS-S3-Bucket

## Summary

This procedure exploits a misconfigured AWS S3 bucket with public read access to unauthorizedly retrieve sensitive files, such as iOS application source code, configuration files, and test data, demonstrating information disclosure in cloud environments.

## Description

In this attack scenario, the target is an AWS S3 bucket incorrectly set to public without access restrictions, allowing anonymous users to read objects. Typical in bug bounty hunting, the attacker uses enumeration to identify the bucket (e.g., via common naming conventions like 'company-ios-test'). Upon access, files reveal proprietary code and internal details. The procedure assumes no authentication is needed due to the misconfiguration. Expected outcomes include downloading sensitive data, highlighting risks of improper bucket policies. This was observed in a Slack vulnerability where iOS test app assets were exposed, rated critical for proprietary info leakage.

## Requirements

1. Internet connectivity to reach AWS S3 endpoints
2. Knowledge of suspected bucket names (e.g., from domain reconnaissance or public sources)
3. Basic HTTP client (curl or browser) for testing access

## Defense

Defensive measures and detection strategies:

- Implement least-privilege S3 bucket policies: Deny public read access using IAM conditions
- Enable AWS Config rules to monitor for public buckets and alert on changes
- Use S3 Block Public Access settings at account and bucket levels
- Log S3 access via CloudTrail and monitor for anomalous anonymous requests

## Objectives

1. Gain unauthorized read access to S3 bucket contents
2. Exfiltrate proprietary files like source code and configs
3. Assess impact of cloud misconfigurations on data exposure

## Instructions

### Step 1: Enumerate and Test Bucket Accessibility

**Context**: Identify a potential S3 bucket and verify if it allows public read access without credentials.

**Command** ([[commands/curl-access-s3-bucket]]):
```bash
curl -I http://suspected-bucket-name.s3.amazonaws.com/
```

> This sends a HEAD request to check for public access. Expected output: HTTP/1.1 200 OK if public; 403 Forbidden if restricted. No authentication headers are needed.

### Step 2: List and Download Bucket Contents

**Context**: If accessible, retrieve the list of objects and download sensitive files.

**Command** ([[commands/curl-access-s3-bucket]]):
```bash
curl http://suspected-bucket-name.s3.amazonaws.com/ -o bucket-listing.xml
curl http://suspected-bucket-name.s3.amazonaws.com/path/to/source-code.zip -o source-code.zip
```

> The first command fetches the bucket index (XML format listing objects). The second downloads a specific file. Expected output: XML with object keys or binary file content. Inspect for iOS source code, configs, and test data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Data from Cloud Storage]] Data from Cloud Storage Object

### Sub-Techniques


## Commands Used

- [[commands/curl-access-s3-bucket]]

## Tools Used


## Tags

- aws
- s3
- information-disclosure
- cloud-misconfig

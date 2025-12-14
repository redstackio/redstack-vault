---
id: tool-aws-s3-001
url: 'https://s3.console.aws.amazon.com/s3/home'
tags:
  - s3
  - storage
  - hosting
type: tool
verified: false
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.684Z'
validated: true
submitted: true
---
# AWS S3

**Status**: Unverified

## Overview

AWS S3 is object storage used to host static content like phishing pages, configured as origins for CloudFront in takeover attacks to serve malicious files via hijacked subdomains.

## Description

S3 buckets can be made public for web hosting, enabling attackers to upload and deliver arbitrary content. In red teaming, it's paired with CloudFront for scalable, low-cost malicious delivery.

## Features

- Feature 1: Static website hosting with public ACLs
- Feature 2: Integration as CloudFront origins
- Feature 3: CLI support for uploads (aws s3 cp)

## Installation

### Requirements

- AWS account with S3 permissions

### Install Commands

Install AWS CLI: `pip install awscli`

## Basic Usage

```bash
aws s3 ls
```

### Common Options

| Option | Description |
|--------|-------------|
| --acl public-read | Make objects publicly accessible |
| cp | Copy files to/from bucket |

## Examples

### Example 1: Basic Usage

```bash
aws s3 cp login.html s3://bucket/ --acl public-read
```

### Example 2: Advanced Usage

```bash
aws s3 sync . s3://bucket/ --acl public-read --delete
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[T1566.001]] Phishing: Spearphishing Attachment

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- S3 access logs showing uploads from unknown IPs
- Public bucket scans with tools like S3Scanner

## Related Procedures


## Related Tools

- [[tools/AWS-CloudFront-Console]]

## References

- Official documentation: https://docs.aws.amazon.com/s3/
- Related resources: AWS S3 Security Checklist

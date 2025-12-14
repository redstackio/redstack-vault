---
id: tool-uuid-001
url: 'https://aws.amazon.com/cloudfront/'
tags:
  - cloud
  - cdn
  - exploit
type: tool
verified: false
platforms:
  - AWS
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.993Z'
validated: true
submitted: true
---
# AWS CloudFront

**Status**: Unverified

## Overview

AWS CloudFront is a content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency. In security testing, it's commonly used to exploit subdomain takeovers via dangling CNAME records, allowing attackers to host arbitrary content on victim domains.

## Description

CloudFront enables edge caching and distribution from origins like S3. For offensive security, attackers create distributions with alternate domain names matching vulnerable subdomains, claiming control without owning the domain. Features include global edge locations, HTTPS support, and integration with AWS services. In takeover scenarios, it's abused due to lax validation on CNAMEs.

## Features

- Feature 1: Alternate Domain Names (CNAMEs) for custom subdomains
- Feature 2: Integration with S3/EC2 origins for hosting PoC content
- Feature 3: Automatic HTTPS with ACM certificates (though not required for basic takeovers)

## Installation

### Requirements

- AWS account with IAM permissions for CloudFront
- AWS CLI installed for automation (optional)

### Install Commands

```bash
# Install AWS CLI
pip install awscli
aws configure
```

## Basic Usage

```bash
aws cloudfront create-distribution --distribution-config file://config.json
```

### Common Options

| Option | Description |
|--------|-------------|
| `--distribution-config` | JSON file defining distribution settings |
| `--profile` | AWS profile for credentials |
| `--region` | AWS region (CloudFront is global) |

## Examples

### Example 1: Basic Usage

Create a distribution via console or CLI for a simple S3 origin.

### Example 2: Advanced Usage

```bash
aws cloudfront create-distribution --distribution-config '{"Origins": {"Quantity":1,"Items":[{"Id":"S3-origin","DomainName":"bucket.s3.amazonaws.com","CustomOriginConfig":{"HTTPPort":80}}]}, "Aliases": {"Quantity":1,"Items":["rider.uber.com"]}}'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for new CloudFront distributions with external CNAMEs via AWS CloudTrail
- Scan DNS for dangling records pointing to cloudfront.net
- Alert on anomalous traffic to subdomains from CloudFront edge locations

## Related Procedures


## Related Tools

- [[AWS-S3]]
- [[AWS-CLI]]

## References

- Official documentation: https://docs.aws.amazon.com/cloudfront/
- Related resources: https://hackerone.com/reports/175070

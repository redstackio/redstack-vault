---
id: tool-aws-cloudfront-console
url: 'https://console.aws.amazon.com/cloudfront'
tags:
  - cloud
  - cd n
type: tool
verified: false
platforms:
  - Web
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.876Z'
validated: true
submitted: true
---
# AWS CloudFront Console

**Status**: Unverified

## Overview

The AWS CloudFront Console is a web-based interface for managing content delivery networks, used in attacks to claim unowned distributions and hijack subdomains via alternate domain names.

## Description

Part of AWS Management Console, it allows creation of distributions, configuration of origins, and assignment of CNAMEs. Attackers exploit unclaimed hostnames to serve malicious content on legitimate subdomains, as in the Uber saostatic takeover.

## Features

- Feature 1: Create distributions with custom origins
- Feature 2: Add alternate domain names (CNAMEs) for subdomain claiming
- Feature 3: HTTPS support with ACM certificates

## Installation

### Requirements

- AWS account with CloudFront access

### Install Commands

```bash
# Browser-based; no install needed
```

## Basic Usage

```bash
# Access via browser: https://console.aws.amazon.com/cloudfront
```

### Common Options

| Option | Description |
|--------|-------------|
| Distributions | Create/manage CDN setups |
| Origins | Link to S3/EC2 for content |

## Examples

### Example 1: Basic Usage

Browse to console, create distribution, add origin.

### Example 2: Advanced Usage

Add saostatic.uber.com as CNAME, deploy for takeover.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1078.004]] Valid Accounts: Cloud Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- CloudTrail logs of new distribution creations
- Unauthorized CNAME additions

## Related Procedures

- [[procedures/Claim-Unclaimed-AWS-CloudFront-Distribution]]

## Related Tools

- [[AWS CLI]]

## References

- Official documentation: https://docs.aws.amazon.com/cloudfront

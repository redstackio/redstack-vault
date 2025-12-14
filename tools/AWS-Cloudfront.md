---
id: tool-aws-cloudfront
url: 'https://aws.amazon.com/cloudfront/custom-ssl-domains/'
tags:
  - cdn
  - takeover
type: tool
verified: false
platforms:
  - AWS
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:43.033Z'
validated: true
submitted: true
---
# AWS-Cloudfront

**Status**: Unverified

## Overview

Amazon's CDN service for distributing content, exploited here by creating distributions to claim dangling hostnames for traffic hijacking.

## Description

Cloudfront allows adding custom CNAMEs to distributions, enabling subdomain takeovers when originals are unclaimed.

## Features

- Feature 1: Global edge locations
- Feature 2: Custom domain support
- Feature 3: HTTPS with ACM

## Installation

### Requirements

- AWS account

### Install Commands

Web console or AWS CLI: pip install awscli

## Basic Usage

```bash
aws cloudfront create-distribution --distribution-config file://config.json
```

### Common Options

| Option | Description |
|--------|-------------|
| --aliases | Add CNAMEs |

## Examples

### Example 1: Basic Usage

Create via console: New Distribution > Origin Domain > CNAMEs

### Example 2: Advanced Usage

CLI for scripting takeovers

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1133.003]] Cloud Services

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- New distributions with external CNAMEs
- AWS CloudTrail logs

## Related Procedures

- [[procedures/Create-AWS-Cloudfront-Distribution-for-Takeover]]

## Related Tools


## References

- AWS docs

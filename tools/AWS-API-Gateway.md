---
url: 'https://aws.amazon.com/api-gateway/'
tags:
  - cloud
  - proxy
  - aws
type: tool
platforms:
  - Web
  - Cloud
description: >-
  AWS service for creating APIs that can proxy requests and rotate IPs for
  bypassing rate limits.
id: e36525ca-7e17-4a17-b3d2-7ffe85be4b77
created_at: '2025-12-14T17:30:26.689Z'
updated_at: '2025-12-14T17:30:26.689Z'
verified: false
validated: true
submitted: true
---
# AWS-API-Gateway

**Status**: Unverified

## Overview

AWS API Gateway manages APIs at scale, used here to proxy and rotate IP addresses in attacks by creating endpoints that forward to targets.

## Description

Configure integrations to backend like MoPub, leveraging AWS's IP pool for rotation without local proxies.

## Features

- Feature 1: Proxy integrations to HTTP endpoints
- Feature 2: Custom domains and throttling
- Feature 3: Lambda for dynamic routing

## Installation

### Requirements

- AWS account

### Install Commands

```bash
# Use AWS CLI
aws configure
# Create via console or CLI: aws apigateway create-rest-api --name MoPubProxy
```

## Basic Usage

```bash
aws apigateway get-rest-apis
```

### Common Options

| Option | Description |
|--------|-------------|
| --integration-http-method | POST for login |
| --uri | Target endpoint URL |

## Examples

### Example 1: Basic Usage

Create API and deploy to proxy requests.

### Example 2: Advanced Usage

```bash
curl -X POST https://your-api.execute-api.us-east-1.amazonaws.com/prod/login -d payload
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy
- [[Protocol Tunneling]] Protocol Tunneling

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Traffic from AWS IP ranges to login endpoints
- API Gateway logs showing high request volumes

## Related Procedures

- [[procedures/Alternative-Bypass-with-AWS-API-Gateway-or-Bash-Proxy-Script]]

## Related Tools

- [[tools/IPRotate-Burp-Extension]]

## References

- AWS Docs: https://docs.aws.amazon.com/apigateway/

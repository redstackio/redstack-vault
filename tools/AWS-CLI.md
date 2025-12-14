---
url: 'https://aws.amazon.com/cli/'
tags:
  - aws
  - cloud
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  Command Line Interface for AWS services, used for managing S3 buckets and
  uploads.
id: 0c9cd3f6-8f9e-4745-97d1-a03403fa4a09
created_at: '2025-12-14T05:32:24.257Z'
updated_at: '2025-12-14T05:32:24.257Z'
verified: false
validated: true
submitted: true
---
# aws-cli

**Status**: Unverified

## Overview

AWS CLI is the official tool for interacting with AWS services from the command line, commonly used in security testing for resource creation, configuration, and exploitation in cloud environments like S3 subdomain takeovers.

## Description

It provides full access to S3 operations such as bucket management (mb/rm), file uploads (cp/sync), and policy setting. In offensive security, it's key for claiming dangling resources and deploying payloads.

## Features

- Feature 1: S3 bucket creation and deletion
- Feature 2: File upload with ACL control
- Feature 3: Website hosting configuration

## Installation

### Requirements

- Python 3.6+
- AWS credentials configured

### Install Commands

```bash
# Installation command
pip install awscli
```

## Basic Usage

```bash
aws --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--region` | Specify AWS region |
| `--profile` | Use specific credential profile |

## Examples

### Example 1: Basic Usage

```bash
aws s3 ls
```

### Example 2: Advanced Usage

```bash
aws s3 mb s3://test-bucket --region us-east-1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Create Account]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- CloudTrail logs showing S3 API calls from unknown IPs
- Unusual bucket creations in specific regions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html
- Related resources: AWS Security Best Practices

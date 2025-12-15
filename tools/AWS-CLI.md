---
id: tool-001
url: 'https://docs.aws.amazon.com/cli/'
tags:
  - aws
  - cli
  - cloud
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.415Z'
validated: true
submitted: true
---
# AWS-CLI

**Status**: Unverified

## Overview

The AWS Command Line Interface (CLI) is a unified tool for managing AWS services, including Cognito for user pool interactions like attribute retrieval and updates in security testing.

## Description

AWS CLI allows programmatic access to AWS APIs without SDKs, ideal for exploiting cloud misconfigurations. In this attack, it's used for Cognito endpoints to manipulate user emails without verification.

## Features

- Feature 1: Direct API calls to services like cognito-idp
- Feature 2: Token-based authentication for temporary access
- Feature 3: JSON output for parsing in scripts

## Installation

### Requirements

- Python 3.6+ or standalone installer
- AWS account (not needed for token auth here)

### Install Commands

```bash
# Via pip
pip install awscli

# Or download from AWS
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

## Basic Usage

```bash
aws --version
aws cognito-idp help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `--region` | Specify region |
| `--output json` | JSON format |

## Examples

### Example 1: Basic Usage

```bash
aws cognito-idp list-user-pools --region us-east-1
```

### Example 2: Advanced Usage

```bash
aws cognito-idp get-user --region us-east-1 --access-token <token>
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1078.004]] Cloud Accounts
- [[Account Manipulation]] Account Manipulation

### Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor AWS CloudTrail for cognito-idp API calls from CLI user agents
- Detect unusual get-user or update-user-attributes from non-standard IPs
- Alert on token usage in CLI commands

## Related Procedures

- [[procedures/Retrieve-Cognito-User-Attributes]]
- [[procedures/Update-Cognito-Email-to-Case-Variant]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html
- Cognito CLI reference: https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/

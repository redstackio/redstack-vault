---
id: i9j0k1l2-m3n4-5678-ijkl-901234567890
url: >-
  https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html
tags:
  - aws
  - deployment
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:27.392Z'
validated: true
submitted: true
---
# AWS-SAM-CLI

**Status**: Unverified

## Overview

AWS SAM CLI is a command-line tool for building, testing, and deploying serverless applications using AWS Lambda and SAM templates, commonly used in security testing to replicate and exploit misconfigured deployments.

## Description

SAM CLI extends AWS CLI for serverless workflows, supporting local invocation, packaging, and deployment of CloudFormation templates. In offensive security, it's used to deploy sample apps like aws-lambda-ecs-run-task to identify IAM misconfigurations leading to privilege escalation.

## Features

- Feature 1: Local Lambda testing with sam local invoke
- Feature 2: Guided deployment with sam deploy --guided
- Feature 3: Template validation and build optimization

## Installation

### Requirements

- Python 3.8+
- AWS CLI v2

### Install Commands

```bash
pip install aws-sam-cli
```

## Basic Usage

```bash
sam --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--debug` | Enable debug mode |

## Examples

### Example 1: Basic Usage

```bash
sam build
```

### Example 2: Advanced Usage

```bash
sam deploy --stack-name vuln-stack --capabilities CAPABILITY_IAM
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- CloudTrail logs showing SAM CLI API calls (e.g., CreateStack)
- Unusual serverless deployments from non-standard IPs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/AWS-CLI]]

## References

- Official documentation: https://docs.aws.amazon.com/serverless-application-model/

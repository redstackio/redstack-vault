---
url: 'https://aws.amazon.com/serverless/sam/'
tags:
  - aws
  - serverless
type: tool
verified: false
platforms:
  - AWS
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.645Z'
id: e289c4b4-b05c-441a-9e18-b0873da4928f
validated: true
submitted: true
---
# SAM-CLI

**Status**: Unverified

## Overview

AWS SAM CLI is a tool for building, testing, and deploying Serverless Applications, useful for local simulation and deployment in vulnerability assessment.

## Description

Extends AWS CLI for Serverless, allowing quick deployment of Lambda-based apps like the target experimental application.

## Features

- Feature 1: Local invocation of Lambda functions
- Feature 2: Deployment via sam deploy
- Feature 3: Integration with CloudFormation

## Installation

### Requirements

- AWS CLI
- Docker (for local testing)

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
| `-h, --help` | Help |
| `--debug` | Debug mode |

## Examples

### Example 1: Basic Usage

```bash
sam deploy --stack-name my-app
```

### Example 2: Advanced Usage

```bash
sam local invoke ExtractCarbonEmissionsFunction
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[External Remote Services]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- CloudTrail events from sam cli deployments
- Local Docker containers mimicking Lambda

## Related Procedures

- [[procedures/Deploy-AWS-Serverless-Application]]

## Related Tools

- [[tools/AWS-CLI]]

## References

- Official documentation: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html

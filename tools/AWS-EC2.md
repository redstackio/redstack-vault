---
id: tool-885539-aws-ec2
url: 'https://aws.amazon.com/ec2'
tags:
  - cloud
  - deployment
  - scaling
type: tool
verified: false
platforms:
  - Cloud
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.339Z'
validated: true
submitted: true
---
# AWS EC2

**Status**: Unverified

## Overview

Amazon EC2 (Elastic Compute Cloud) provides scalable virtual servers in the AWS cloud, used for deploying PoC scripts and running resource-intensive tasks like brute-forcing.

## Description

For security testing, EC2 instances host scripts (e.g., Ruby for timing attacks) to avoid local resource limits and IP blocking. Launch t2.micro or larger, install dependencies, and run remotely via SSH. Ideal for evading detection by distributing load.

## Features

- Feature 1: On-demand instance scaling.
- Feature 2: AMI support for quick setups.
- Feature 3: Security groups for network control.

## Installation

### Requirements

- AWS account.
- SSH client.

### Install Commands

```bash
# Launch via AWS CLI
echo 'run-instances --image-id ami-0abcdef1234567890 --count 1 --instance-type t2.micro' | aws ec2
ssh -i key.pem ec2-user@ip ruby twileak.rb
```

## Basic Usage

```bash
aws ec2 run-instances --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--instance-type` | VM size (t2.micro) |
| `--key-name` | SSH key pair |

## Examples

### Example 1: Basic Usage

```bash
# Launch instance and deploy script
aws ec2 run-instances --image-id ami-ubuntu --count 1
```

### Example 2: Advanced Usage

```bash
# Run brute-force script on instance
scp twileak.rb ec2-user@ip:/tmp/
ssh ec2-user@ip 'ruby /tmp/twileak.rb'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Modify Cloud Compute Infrastructure]] Tool Identification (cloud deployment)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- New EC2 instances querying target APIs.
- AWS logs showing script executions.

## Related Procedures

- [[procedures/Brute-Force-Private-List-IDs-with-Timing-Differences]]

## Related Tools

- [[tools/GCP-Compute-Engine]]

## References

- Official documentation: https://docs.aws.amazon.com/ec2

---
id: tool-uuid-1
url: null
tags:
  - automation
  - aws
  - elb
  - brute-force
type: tool
verified: false
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:24.102Z'
validated: true
submitted: true
---
# Automated-ELB-Creation-Script

**Status**: Unverified

## Overview

A custom script to automate the creation of multiple AWS Application Load Balancers with varying numeric suffixes, aimed at matching a dangling ELB DNS name for subdomain takeover attacks.

## Description

This tool uses the AWS SDK (e.g., boto3 in Python) to iteratively create ALBs with a fixed prefix and randomized or sequential suffixes until a match is found for the target CNAME. It's essential for overcoming the randomness in ELB naming, reducing manual trial-and-error in takeover exploits.

## Features

- Feature 1: Prefix-based ELB name generation
- Feature 2: Suffix brute-forcing (e.g., 000000000 to 999999999)
- Feature 3: Automatic deletion of non-matching ELBs to avoid costs

## Installation

### Requirements

- Python 3.x
- AWS CLI configured with credentials
- boto3 library

### Install Commands

```bash
pip install boto3
```

## Basic Usage

```bash
python elb_bruteforce.py --prefix a0e7eaaaa82f611e9b1cc0e9ccd15f3e --target-suffix 557536140 --region us-west-2
```

### Common Options

| Option | Description |
|--------|-------------|
| `--prefix` | Base name for ELB |
| `--region` | AWS region to target |
| `--max-attempts` | Limit on creation tries |

## Examples

### Example 1: Basic Usage

```bash
python elb_bruteforce.py --prefix exampleprefix --region us-west-2
```

### Example 2: Advanced Usage

```bash
python elb_bruteforce.py --prefix a0e7eaaaa82f611e9b1cc0e9ccd15f3e --target-suffix 557536140 --max-attempts 1000 --delete-on-fail
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1583.001]] Domains
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Spike in ELB creation/deletion events in CloudTrail
- Detection method 2: Anomalous boto3 API calls from unknown IPs

## Related Procedures


## Related Tools

- [[tools/AWS-CLI]]
- [[tools/Boto3]]

## References

- AWS ELB Documentation
- Boto3 ELB API Reference

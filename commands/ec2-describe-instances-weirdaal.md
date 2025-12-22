---
id: 33d51195-8a08-4f1e-8d59-a0e55ea3d70c
type: command
executor: bash
data: python3 weirdAAL.py -m ec2_describe_instances -t demo
output: null
created_at: '2023-04-06T03:56:08.939743+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - ec2
  - weirdaal
verified: true
validated: true
---

# EC2 Describe Instances WeirdAAL

## Command

```bash
python3 weirdAAL.py -m ec2_describe_instances -t demo
```

## Description

Uses WeirdAAL to describe EC2 instances in target account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m ec2_describe_instances | Module | Yes |
| -t demo | Target profile | Yes |

## Examples

### Basic Usage

```bash
python3 weirdAAL.py -m ec2_describe_instances -t demo
```

## Expected Output

Instances: i-12345678 in us-east-1

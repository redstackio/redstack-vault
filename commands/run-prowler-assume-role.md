---
id: fb98ec17-c0f9-44c8-a2d3-a0cdf141ddd2
type: command
executor: bash
data: ./prowler -A 123456789012 -R ProwlerRole
output: null
created_at: '2023-04-06T03:56:08.938508+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - prowler
  - assume-role
verified: true
validated: true
---

# Run Prowler Assume Role

## Command

```bash
./prowler -A 123456789012 -R ProwlerRole
```

## Description

Runs Prowler assuming an IAM role via STS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -A 123456789012 | Account ID | Yes |
| -R ProwlerRole | Role name | Yes |

## Examples

### Basic Usage

```bash
./prowler -A 123456789012 -R ProwlerRole
```

## Expected Output

Assuming role... Audit started.

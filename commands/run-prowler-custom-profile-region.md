---
id: 152ce2cc-a0c3-42a2-896c-daa27d332b74
type: command
executor: bash
data: ./prowler -p custom-profile -r us-east-1 -c check11
output: null
created_at: '2023-04-06T03:56:08.938501+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - prowler
  - profile
verified: true
validated: true
---

# Run Prowler Custom Profile Region

## Command

```bash
./prowler -p custom-profile -r us-east-1 -c check11
```

## Description

Runs specific check in a region using custom profile.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p custom-profile | AWS profile | Yes |
| -r us-east-1 | Region | Yes |
| -c check11 | Check ID | Yes |

## Examples

### Basic Usage

```bash
./prowler -p custom-profile -r us-east-1 -c check11
```

## Expected Output

check11 [PASS] in us-east-1

---
id: 87d656a7-bf2a-4d2a-a062-35ba6094f887
type: command
executor: bash
data: python s3-objects-check.py -p whitebox-profile -e blackbox-profile
output: null
created_at: '2023-04-06T03:56:08.939328+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - s3
  - permissions
verified: true
validated: true
---

# Run S3 Objects Check Profiles

## Command

```bash
python s3-objects-check.py -p whitebox-profile -e blackbox-profile
```

## Description

Runs permission check using whitebox and blackbox AWS profiles.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p whitebox-profile | Internal profile | Yes |
| -e blackbox-profile | External profile | Yes |

## Examples

### Basic Usage

```bash
python s3-objects-check.py -p whitebox-profile -e blackbox-profile
```

## Expected Output

Bucket: mybucket
Public objects: 5

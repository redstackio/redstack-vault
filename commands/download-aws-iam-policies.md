---
id: 7192a51a-9bab-4646-8c4e-bfbc45ed93f0
type: command
executor: bash
data: cloudsplaining download --profile myawsprofile
output: null
created_at: '2023-04-06T03:56:08.939567+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - iam
  - download
verified: true
validated: true
---

# Download AWS IAM Policies

## Command

```bash
cloudsplaining download --profile myawsprofile
```

## Description

Downloads IAM policies from AWS to local JSON for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --profile myawsprofile | AWS profile name | Yes |

## Examples

### Basic Usage

```bash
cloudsplaining download --profile myawsprofile
```

## Expected Output

Downloaded to default.json

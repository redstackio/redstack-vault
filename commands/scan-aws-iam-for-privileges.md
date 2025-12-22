---
id: 75dbbb5b-38d0-4c17-8e7b-c952c3fdb986
type: command
executor: bash
data: cloudsplaining scan --input-file default.json
output: null
created_at: '2023-04-06T03:56:08.939615+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - iam
  - scan
verified: true
validated: true
---

# Scan AWS IAM for Privileges

## Command

```bash
cloudsplaining scan --input-file default.json
```

## Description

Scans downloaded IAM policies for least privilege violations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --input-file default.json | JSON file path | Yes |

## Examples

### Basic Usage

```bash
cloudsplaining scan --input-file default.json
```

## Expected Output

High risk policies: admin-full-access

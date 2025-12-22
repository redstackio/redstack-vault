---
id: ffb012c0-afa4-4475-acf6-511d01924ae6
type: command
executor: bash
data: pipenv run python cloudmapper.py audit
output: null
created_at: '2023-04-06T03:56:08.940271+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - audit
  - cloudmapper
verified: true
validated: true
---

# Audit AWS Account CloudMapper

## Command

```bash
pipenv run python cloudmapper.py audit
```

## Description

Audits the AWS account for misconfigurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| audit | Audit mode | Yes |

## Examples

### Basic Usage

```bash
pipenv run python cloudmapper.py audit
```

## Expected Output

Misconfigs found: 3 high risk

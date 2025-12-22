---
id: ff96d571-b4a4-428b-8c51-bebc2ccba5c6
type: command
executor: bash
data: pipenv run python cloudmapper.py iam_report
output: null
created_at: '2023-04-06T03:56:08.940201+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - iam
  - report
verified: true
validated: true
---

# Generate CloudMapper IAM Report

## Command

```bash
pipenv run python cloudmapper.py iam_report
```

## Description

Creates HTML report on IAM configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| iam_report | IAM mode | Yes |

## Examples

### Basic Usage

```bash
pipenv run python cloudmapper.py iam_report
```

## Expected Output

IAM report: iam_report.html

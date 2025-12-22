---
id: 5b37d322-c489-4a9c-bbda-0044a6892df6
type: command
executor: bash
data: pipenv run python cloudmapper.py report
output: null
created_at: '2023-04-06T03:56:08.940167+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - report
  - html
verified: true
validated: true
---

# Generate CloudMapper HTML Report

## Command

```bash
pipenv run python cloudmapper.py report
```

## Description

Generates an HTML report summarizing AWS accounts and findings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| report | Report mode | Yes |

## Examples

### Basic Usage

```bash
pipenv run python cloudmapper.py report
```

## Expected Output

Report generated: report.html

---
id: dec22327-1915-4a28-bd0d-9330f792c204
type: command
executor: bash
data: pipenv run python cloudmapper.py collect
output: null
created_at: '2023-04-06T03:56:08.940349+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - metadata
  - collect
verified: true
validated: true
---

# Collect AWS Metadata CloudMapper

## Command

```bash
pipenv run python cloudmapper.py collect
```

## Description

Collects metadata about the AWS account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| collect | Collect mode | Yes |

## Examples

### Basic Usage

```bash
pipenv run python cloudmapper.py collect
```

## Expected Output

Metadata collected to data/

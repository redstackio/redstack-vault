---
id: 642ea753-2d9d-4105-92aa-c2df63aa9c38
type: command
executor: bash
data: python3 -m venv env && source env/bin/activate
output: null
created_at: '2023-04-06T03:56:08.939078+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - venv
  - python
verified: true
validated: true
---

# Create Activate Python Venv

## Command

```bash
python3 -m venv env && source env/bin/activate
```

## Description

Creates and activates a Python virtual environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| env | Environment name | Yes |

## Examples

### Basic Usage

```bash
python3 -m venv env && source env/bin/activate
```

## Expected Output

(env) user@host:~/s3_objects_check$

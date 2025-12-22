---
id: 6ab8becc-4d13-44c5-8b69-0b20ffcf2873
type: command
executor: bash
data: pip install -r requirements.txt
output: null
created_at: '2023-04-06T03:56:08.939176+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - install
  - deps
verified: true
validated: true
---

# Install S3 Objects Check Deps

## Command

```bash
pip install -r requirements.txt
```

## Description

Installs dependencies from requirements.txt for S3 Objects Check.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r requirements.txt | Requirements file | Yes |

## Examples

### Basic Usage

```bash
pip install -r requirements.txt
```

## Expected Output

Successfully installed boto3-... awscli-...

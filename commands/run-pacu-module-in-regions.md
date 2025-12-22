---
id: a60e00aa-728f-4c60-bd80-58efdf6556dc
type: command
executor: bash
data: 'run <module_name> --regions eu-west-1,us-west-1'
output: null
created_at: '2023-04-06T03:56:08.937546+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - regions
  - module
verified: true
validated: true
---

# Run Pacu Module in Specific Regions

## Command

```bash
run <module_name> --regions eu-west-1,us-west-1
```

## Description

Runs a Pacu module limited to specified AWS regions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <module_name> | Module name | Yes |
| --regions | Comma-separated regions | Yes |

## Examples

### Basic Usage

```bash
run s3__enum --regions us-east-1,eu-west-1
```

## Expected Output

Scanning regions... Buckets found in us-east-1.

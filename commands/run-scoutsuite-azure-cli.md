---
id: 27c5e82e-eea0-4694-b586-8232ddf5f41f
type: command
executor: bash
data: python scout.py azure --cli
output: null
created_at: '2023-04-06T03:56:08.938960+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - azure
  - scoutsuite
verified: true
validated: true
---

# Run ScoutSuite Azure CLI

## Command

```bash
python scout.py azure --cli
```

## Description

Runs ScoutSuite on Azure using CLI authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cli | Use Azure CLI login | Yes |

## Examples

### Basic Usage

```bash
python scout.py azure --cli
```

## Expected Output

Auditing Azure... Report in azure_report/

---
id: 4ed6f484-72ae-49e5-a0f8-421a872972d7
type: command
executor: bash
data: python3 weirdAAL.py -m lambda_get_account_settings -t demo
output: null
created_at: '2023-04-06T03:56:08.939809+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - lambda
  - weirdaal
verified: true
validated: true
---

# Lambda Get Account Settings WeirdAAL

## Command

```bash
python3 weirdAAL.py -m lambda_get_account_settings -t demo
```

## Description

Retrieves Lambda account settings via WeirdAAL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m lambda_get_account_settings | Module | Yes |
| -t demo | Target | Yes |

## Examples

### Basic Usage

```bash
python3 weirdAAL.py -m lambda_get_account_settings -t demo
```

## Expected Output

Account limit: 1000 functions

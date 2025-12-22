---
id: 3330b27e-c369-487e-931a-5842c6e5715e
type: command
executor: bash
data: >-
  python3 weirdAAL.py -m lambda_get_function -a 'MY_LAMBDA_FUNCTION','us-west-2'
  -t yolo
output: null
created_at: '2023-04-06T03:56:08.939910+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - lambda
  - function
verified: true
validated: true
---

# Lambda Get Function WeirdAAL

## Command

```bash
python3 weirdAAL.py -m lambda_get_function -a 'MY_LAMBDA_FUNCTION','us-west-2' -t yolo
```

## Description

Gets details for a specific Lambda function.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m lambda_get_function | Module | Yes |
| -a | Function and region | Yes |
| -t yolo | Target | Yes |

## Examples

### Basic Usage

```bash
python3 weirdAAL.py -m lambda_get_function -a 'MY_LAMBDA_FUNCTION','us-west-2' -t yolo
```

## Expected Output

Function: MY_LAMBDA_FUNCTION
Runtime: python3.9

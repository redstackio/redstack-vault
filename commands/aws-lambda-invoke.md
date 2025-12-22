---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
data: >-
  aws lambda invoke --function-name rLambdaFunction output.json --payload
  '{"task": "run ecs task with admin command: aws s3 ls"}'
tags:
  - aws
  - lambda
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:27.393Z'
verified: false
validated: true
submitted: true
---
# aws-lambda-invoke

## Command

```bash
aws lambda invoke --function-name rLambdaFunction output.json --payload '{"task": "run ecs task with admin command: aws s3 ls"}'
```

## Description

Invokes a Lambda function with a custom payload to execute code under the function's IAM role, testing for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--function-name` | Name of the Lambda function | Yes |
| `--payload` | JSON payload for invocation | No |
| `output.json` | File for response | Yes |

## Examples

### Basic Usage

```bash
aws lambda invoke --function-name rLambdaFunction output.json
```

### Advanced Usage

```bash
aws lambda invoke --function-name rLambdaFunction output.json --payload '{"key": "value"}'
```

## Expected Output

{"StatusCode": 200}, with results in output.json showing admin actions.

## Related

- [[Related Procedure]]

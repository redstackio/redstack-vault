---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: |-
  sam build
  sam deploy --guided
tags:
  - aws
  - deployment
  - sam
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:27.406Z'
verified: false
validated: true
submitted: true
---
# sam-build-deploy

## Command

```bash
sam build
sam deploy --guided
```

## Description

Builds the AWS SAM application template and deploys it to AWS, creating resources like Lambda functions and IAM roles for testing misconfigurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--guided` | Interactive deployment prompts | No |

## Examples

### Basic Usage

```bash
sam build
sam deploy --guided
```

### Advanced Usage

```bash
sam build --use-container
sam deploy --stack-name test-stack --capabilities CAPABILITY_IAM
```

## Expected Output

Build succeeded. Deployment: Stack update complete, with resource ARNs in outputs.

## Related

- [[Related Procedure]]

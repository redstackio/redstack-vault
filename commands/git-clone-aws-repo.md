---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: |-
  git clone https://github.com/awslabs/aws-lambda-ecs-run-task.git
  cd aws-lambda-ecs-run-task
tags:
  - deployment
  - git
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:27.407Z'
verified: false
validated: true
submitted: true
---
# git-clone-aws-repo

## Command

```bash
git clone https://github.com/awslabs/aws-lambda-ecs-run-task.git
cd aws-lambda-ecs-run-task
```

## Description

Clones the AWS Labs aws-lambda-ecs-run-task repository from GitHub and changes into the project directory, preparing for SAM deployment in an AWS vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/awslabs/aws-lambda-ecs-run-task.git` | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/awslabs/aws-lambda-ecs-run-task.git
cd aws-lambda-ecs-run-task
```

### Advanced Usage

```bash
git clone --depth 1 https://github.com/awslabs/aws-lambda-ecs-run-task.git
cd aws-lambda-ecs-run-task
```

## Expected Output

Cloning into 'aws-lambda-ecs-run-task'... done. Directory change confirmation via prompt.

## Related

- [[Related Procedure]]

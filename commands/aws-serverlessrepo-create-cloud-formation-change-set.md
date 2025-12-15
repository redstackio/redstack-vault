---
data: >-
  aws serverlessrepo create-cloud-formation-change-set --application-id
  arn:aws:serverlessrepo:us-east-1:123456789012:applications~experimental-programmatic-access-ccft
  --stack-name experimental-app --capabilities CAPABILITY_IAM
tags:
  - deployment
  - aws
type: command
output: null
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.666Z'
id: abf92871-3caf-4c3f-aefb-83c446773107
verified: false
validated: true
submitted: true
---
# aws-serverlessrepo-create-cloud-formation-change-set

## Command

```bash
aws serverlessrepo create-cloud-formation-change-set --application-id arn:aws:serverlessrepo:us-east-1:123456789012:applications~experimental-programmatic-access-ccft --stack-name experimental-app --capabilities CAPABILITY_IAM
```

## Description

Deploys a Serverless Application Repository application by creating a CloudFormation change set, enabling IAM resource creation for the Lambda role.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--application-id` | ARN of the Serverless application | Yes |
| `--stack-name` | Name for the CloudFormation stack | Yes |
| `--capabilities` | Permissions like CAPABILITY_IAM for role creation | Yes |

## Examples

### Basic Usage

```bash
aws serverlessrepo create-cloud-formation-change-set --application-id arn:... --stack-name my-app --capabilities CAPABILITY_IAM
```

### Advanced Usage

```bash
aws serverlessrepo create-cloud-formation-change-set --application-id arn:... --stack-name my-app --capabilities CAPABILITY_IAM --parameter-overrides ParameterKey=Region,ParameterValue=us-west-2
```

## Expected Output

JSON response with ApplicationId, ChangeSetId, and StackId upon successful initiation.

## Related

- [[commands/aws-cloudformation-describe-stacks]]

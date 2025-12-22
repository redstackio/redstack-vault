---
id: c7391960-4fb7-4d52-a280-f187e717695e
name: aws-ecr-get-repository-policy
type: command
executor: bash
data: >-
  aws ecr get-repository-policy --repository-name $_REPOSITORY_NAME --region
  $_REGION
output: null
created_at: '2023-04-06T03:56:12.557986+00:00'
updated_at: '2023-04-10T20:20:34.882779+00:00'
platforms:
  - AWS
tags:
  - cloud
  - aws
  - ecr
  - enumeration
verified: true
validated: true
---

# aws-ecr-get-repository-policy

## Command

```bash
aws ecr get-repository-policy --repository-name $_REPOSITORY_NAME --region $_REGION
```

## Description

This AWS CLI command retrieves the JSON resource-based policy attached to a specified Amazon ECR repository. It is used during cloud discovery to enumerate permissions granted to principals (users, roles, accounts) for actions like image pulls or pushes, helping identify access paths without alerting monitoring tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --repository-name $_REPOSITORY_NAME | The name of the ECR repository (e.g., 'my-app-repo') | Yes |
| --region $_REGION | The AWS region where the repository is located (e.g., 'us-east-1') | Yes |

## Examples

### Basic Usage

```bash
aws ecr get-repository-policy --repository-name my-app-repo --region us-east-1
```

### Usage with Output Formatting

```bash
aws ecr get-repository-policy --repository-name my-app-repo --region us-east-1 --output json | jq '.policyText'
```

## Expected Output

Successful execution returns a JSON response like:

```json
{
    "registryId": "123456789012",
    "repositoryName": "my-app-repo",
    "policyText": "{\n  \"Version\": \"2008-10-17\",\n  \"Statement\": [\n    {\n      \"Sid\": \"\",\n      \"Effect\": \"Allow\",\n      \"Principal\": {\n        \"AWS\": [\n          \"arn:aws:iam::111122223333:root\"\n        ]\n      },\n      \"Action\": [\n        \"ecr:GetDownloadUrlForLayer\",\n        \"ecr:BatchGetImage\"\n      ]\n    }\n  ]\n}"
}
```

The `policyText` field contains the raw JSON policy detailing permissions. Errors like 'AccessDenied' indicate insufficient privileges.

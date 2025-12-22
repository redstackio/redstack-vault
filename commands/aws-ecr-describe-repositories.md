---
id: 323c3775-bc76-4cff-a60d-9b09e9de622e
name: aws-ecr-describe-repositories
type: command
executor: bash
data: aws ecr describe-repositories
output: null
created_at: '2023-04-06T03:56:13.046118+00:00'
updated_at: '2023-04-10T20:20:18.756304+00:00'
platforms:
  - AWS
tags:
  - cloud
  - enumeration
  - ecr
verified: true
validated: true
---

# aws-ecr-describe-repositories

## Command

```bash
aws ecr describe-repositories
```

## Description

This command queries the AWS Elastic Container Registry (ECR) to list all repositories in the current region, returning details such as repository names, ARNs, URIs, creation dates, and image counts. It is used for discovery of container assets in an AWS environment, requiring authenticated AWS CLI access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region to query (e.g., us-west-2); defaults to configured region | No |
| `--repository-names` | Specific repository names to describe (comma-separated); if omitted, lists all | No |
| `--output` | Output format (json, text, table); defaults to json | No |

## Examples

### Basic Usage

List all ECR repositories in the default region:

```bash
aws ecr describe-repositories
```

### Advanced Usage

List repositories in a specific region with table output:

```bash
aws ecr describe-repositories --region us-east-1 --output table
```

### Filtered Usage

Describe a specific repository:

```bash
aws ecr describe-repositories --repository-names my-repo
```

## Expected Output

Successful execution returns a JSON object with a "repositories" array:

```json
{
    "repositories": [
        {
            "repositoryArn": "arn:aws:ecr:us-east-1:123456789012:repository/my-repo",
            "registryId": "123456789012",
            "repositoryName": "my-repo",
            "repositoryUri": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-repo",
            "createdAt": "2023-01-01T00:00:00+00:00",
            "imageTagMutability": "MUTABLE",
            "imageScanningConfiguration": {
                "scanOnPush": false
            },
            "encryptionConfiguration": {
                "encryptionType": "AES256"
            }
        }
    ]
}
```

If no repositories exist, returns an empty "repositories" array. Errors include AccessDenied if permissions are insufficient.

## Related

- [[Related Procedure: Enumerate-AWS-ECR-Repositories]]
- [[Related Tool: aws-cli]]

---
id: 52f1acc2-b2d1-4eda-9c0f-922cda1648a4
name: aws-ecr-list-images
type: command
executor: bash
data: aws ecr list-images --repository-name $_REPOSITORY_NAME
output: null
created_at: '2023-04-06T03:56:13.070019+00:00'
updated_at: '2023-04-10T20:20:47.103490+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - ecr
  - enumeration
verified: true
validated: true
---

# AWS ECR List Images

## Command

```bash
aws ecr list-images --repository-name $_REPOSITORY_NAME
```

## Description

This command lists all Docker images stored in a specific Amazon ECR repository. It is used during discovery to inventory container assets, helping identify potential targets for vulnerability exploitation or further reconnaissance in AWS environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REPOSITORY_NAME | The name of the ECR repository to query (e.g., 'my-app-repo') | Yes |
| --region | AWS region where the repository is located (default: us-east-1) | No |
| --max-results | Maximum number of results to return per call (1-1000, default: 1000) | No |
| --next-token | Pagination token from previous response for large repositories | No |

## Examples

### Basic Usage

```bash
aws ecr list-images --repository-name my-repo
```

### Paginated Usage for Large Repositories

```bash
aws ecr list-images --repository-name my-repo --max-results 500 --region us-west-2
```

## Expected Output

The command returns a JSON object with an array of image details. Successful output looks like:

```json
{
    "imageIds": [
        {
            "imageDigest": "sha256:exampledigest123...",
            "imageTag": "latest",
            "imageSizeInBytes": 123456789
        },
        {
            "imageDigest": "sha256:anotherexample...",
            "imageTag": "v1.0",
            "imageSizeInBytes": 987654321
        }
    ],
    "nextToken": null
}
```

If the repository is empty, "imageIds" will be an empty array. Errors include AccessDeniedException if permissions are insufficient.

## Related

- [[procedures/aws-ecr-repository-image-enumeration]]
- [[tools/aws-cli]]

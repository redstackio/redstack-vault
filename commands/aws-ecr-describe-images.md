---
id: 8c135a0e-4c5c-4b05-ab59-236734c86f2c
name: aws-ecr-describe-images
type: command
executor: bash
data: >-
  aws ecr describe-images --repository-name $_REPOSITORY_NAME --image-ids
  imageTag=$_IMAGE_TAG --region $_REGION
output: null
created_at: '2023-04-06T03:56:13.091308+00:00'
updated_at: '2023-04-10T20:20:47.456456+00:00'
platforms:
  - AWS
tags:
  - cloud
  - discovery
  - ecr
verified: true
validated: true
---

# aws-ecr-describe-images

## Command

```bash
aws ecr describe-images --repository-name $_REPOSITORY_NAME --image-ids imageTag=$_IMAGE_TAG --region $_REGION
```

## Description

This command queries the AWS ECR API to retrieve detailed information about one or more images in a specified repository, including digests, tags, sizes, and push timestamps. It is used for enumerating container images during cloud reconnaissance to identify potential targets or artifacts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--repository-name $_REPOSITORY_NAME` | The name of the ECR repository (e.g., "my-app-repo") | Yes |
| `--image-ids imageTag=$_IMAGE_TAG` | Specifies the image by tag (e.g., "latest"); omit to list all images | No |
| `--region $_REGION` | AWS region where the repository is located (e.g., "us-east-1") | Yes |
| `--output json` | Format output as JSON (default) | No |

## Examples

### Basic Usage

List all images in a repository:
```bash
aws ecr describe-images --repository-name my-repo --region us-east-1
```

### Advanced Usage

Describe a specific tagged image:
```bash
aws ecr describe-images --repository-name my-repo --image-ids imageTag=latest --region us-east-1
```

## Expected Output

Successful execution returns a JSON object with image details. Example for a single image:
```
{
  "imageDetails": [
    {
      "registryId": "123456789012",
      "repositoryName": "my-repo",
      "imageDigest": "sha256:def456...",
      "imageTags": ["v1.0"],
      "imageSizeInBytes": 987654321,
      "imagePushedAt": "2023-04-01T12:00:00+00:00",
      "imageManifestMediaType": "application/vnd.docker.distribution.manifest.v2+json"
    }
  ],
  "failures": []
}
```
If the image or repository doesn't exist, or permissions are insufficient, it returns an error like "AccessDeniedException".

## Related

- [[procedures/Enumerate-AWS-ECR-Images]]

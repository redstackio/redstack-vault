---
id: c2e276f5-34a7-473a-aa8c-4b322c8a9194
name: aws-eks-describe-fargate-profiles
type: command
executor: bash
data: aws eks describe-fargate-profiles --cluster-name $_CLUSTER_NAME
output: null
created_at: '2023-04-06T03:56:12.951481+00:00'
updated_at: '2023-04-10T20:20:24.339379+00:00'
platforms:
  - AWS
  - Kubernetes
tags:
  - enumeration
  - cloud-discovery
verified: true
validated: true
---

# aws-eks-describe-fargate-profiles

## Command

```bash
aws eks describe-fargate-profiles --cluster-name $_CLUSTER_NAME
```

## Description

This command describes all Fargate profiles in the specified EKS cluster. When no --fargate-profile-names is provided, it enumerates all profiles, providing details useful for discovering serverless workloads and associated IAM roles.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cluster-name $_CLUSTER_NAME | The name of the EKS cluster (e.g., my-cluster). | Yes |
| --fargate-profile-names | Optional list of specific profile names to describe (comma-separated); omit for all. | No |
| --region | AWS region (defaults to default profile). | No |

## Examples

### Basic Usage (All Profiles)

```bash
aws eks describe-fargate-profiles --cluster-name my-cluster
```

### Specific Profile

```bash
aws eks describe-fargate-profiles --cluster-name my-cluster --fargate-profile-names fp-default
```

## Expected Output

Returns JSON with a 'fargateProfiles' array, e.g.:

```json
{
    "fargateProfiles": [
        {
            "fargateProfileName": "fp-default",
            "fargateProfileArn": "arn:aws:eks:...",
            "podExecutionRoleArn": "arn:aws:iam::...",
            "subnets": ["subnet-abc"],
            "selectors": [{"namespace": "default"}]
        }
    ]
}
```

Empty array if no profiles; ResourceNotFoundException if cluster doesn't exist.

## Related

- [[procedures/EKS-Fargate-Profile-Enumeration]]

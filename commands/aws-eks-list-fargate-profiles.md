---
id: b27ceb3b-d8fb-4536-98f8-d929129f6a7c
name: aws-eks-list-fargate-profiles
type: command
executor: bash
data: aws eks list-fargate-profiles --cluster-name $_CLUSTER_NAME
output: null
created_at: '2023-04-06T03:56:12.930210+00:00'
updated_at: '2023-04-10T20:20:42.417195+00:00'
platforms:
  - AWS
tags:
  - cloud
  - eks
  - enumeration
verified: true
validated: true
---

# aws-eks-list-fargate-profiles

## Command

```bash
aws eks list-fargate-profiles --cluster-name $_CLUSTER_NAME
```

## Description

This command queries the AWS EKS API to list all Fargate profiles associated with a specific EKS cluster. Fargate profiles control how pods are scheduled on Fargate infrastructure. Use this during cloud discovery to map serverless Kubernetes workloads and identify potential targets like misconfigured roles.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cluster-name | Specifies the name of the EKS cluster to query | Yes |
| $_CLUSTER_NAME | Placeholder for the actual cluster name (e.g., 'my-eks-cluster') | Yes |

## Examples

### Basic Usage

```bash
aws eks list-fargate-profiles --cluster-name my-eks-cluster
```

### Advanced Usage

To output in a more readable format, pipe to `jq`:

```bash
aws eks list-fargate-profiles --cluster-name my-eks-cluster | jq '.fargateProfiles[] | {name: .fargateProfileName, arn: .fargateProfileArn}'
```

## Expected Output

A JSON object containing the list of Fargate profiles, or an empty list if none exist. Successful output resembles:

```json
{
    "fargateProfiles": [
        {
            "clusterName": "my-eks-cluster",
            "createdAt": "2023-04-06T03:56:12+00:00",
            "fargateProfileArn": "arn:aws:eks:us-west-2:123456789012:cluster/my-eks-cluster/fargate-profile/my-profile",
            "fargateProfileName": "my-profile",
            "podExecutionRoleArn": "arn:aws:iam::123456789012:role/eksFargatePodExecutionRole",
            "status": "ACTIVE",
            "subnets": [
                "subnet-12345678"
            ],
            "tags": {},
            "type": "COMPUTE"
        }
    ]
}
```

If no profiles are found, the `fargateProfiles` array is empty. Errors include `AccessDeniedException` for insufficient permissions or `ResourceNotFoundException` for invalid cluster names.

## Related

- [[procedures/AWS-EKS-Fargate-Enumeration]]

---
id: 6bb28069-1faf-4ff7-97e0-00e35d13b08b
name: aws-eks-list-clusters
type: command
executor: bash
data: aws eks list-clusters
output: null
created_at: '2023-04-06T03:56:12.835297+00:00'
updated_at: '2023-04-10T20:19:58.278089+00:00'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tags:
  - cloud
  - enumeration
  - eks
verified: true
validated: true
---

# AWS EKS List Clusters

## Command

```bash
aws eks list-clusters
```

## Description

This command queries the AWS EKS service to list all cluster names in the current AWS account and region. It is used for discovering Kubernetes clusters during cloud reconnaissance, requiring appropriate IAM permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region to query (e.g., us-east-1); defaults to configured region | No |
| `--output` | Output format (json, text, table); defaults to json | No |
| `--profile` | AWS profile name if using multiple configurations | No |

## Examples

### Basic Usage

```bash
aws eks list-clusters
```

### Specify Region

```bash
aws eks list-clusters --region us-west-2
```

### Text Output

```bash
aws eks list-clusters --output text
```

## Expected Output

Successful execution returns a JSON object with a "clusters" array containing cluster names:

```json
{
    "clusters": [
        "my-eks-cluster-1",
        "my-eks-cluster-2"
    ]
}
```

If no clusters exist:

```json
{
    "clusters": []
}
```

Errors like AccessDenied indicate insufficient permissions.

## Related

- [[commands/aws-sts-get-caller-identity]] (for credential verification)
- [[procedures/aws-eks-cluster-enumeration]] (procedure using this command)

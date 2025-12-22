---
id: 9a6ad9a6-1852-450d-bc41-82a148c44df5
name: aws-eks-list-nodegroups
type: command
executor: bash
data: aws eks list-nodegroups --cluster-name $_CLUSTER_NAME
output: null
created_at: '2023-04-06T03:56:12.883309+00:00'
updated_at: '2023-04-10T20:20:07.000242+00:00'
platforms:
  - AWS
  - Cloud
tags:
  - cloud-aws
  - eks
  - enumeration
verified: true
validated: true
---

# aws-eks-list-nodegroups

## Command

```bash
aws eks list-nodegroups --cluster-name $_CLUSTER_NAME
```

## Description

This command queries the AWS EKS API to retrieve a list of all node groups in a specified EKS cluster. It is used for discovering the worker node infrastructure in Kubernetes environments on AWS, aiding in mapping cloud resources during reconnaissance or auditing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cluster-name $_CLUSTER_NAME | The name of the EKS cluster to query (e.g., my-eks-cluster) | Yes |
| --region (implicit) | AWS region where the cluster is located (defaults to configured region) | No |

## Examples

### Basic Usage

```bash
aws eks list-nodegroups --cluster-name my-cluster
```

### Advanced Usage

```bash
aws eks list-nodegroups --cluster-name my-cluster --region us-west-2 --output json
```

## Expected Output

Successful execution returns a JSON object with a 'nodegroups' array containing the names of the node groups:

```json
{
    "nodegroups": [
        "linux-nodegroup",
        "windows-nodegroup"
    ]
}
```

If no node groups exist, the array is empty: {"nodegroups": []}. Errors appear as JSON with 'error' fields, such as AccessDenied for permission issues.

## Related

- [[procedures/AWS-EKS-Node-Group-Enumeration]]

---
id: f3eefd79-454e-4f43-854e-2c0b0dc50d29
name: aws-eks-describe-cluster
type: command
executor: bash
data: aws eks describe-cluster --name $_CLUSTER_NAME
output: null
created_at: '2023-04-06T03:56:12.859381+00:00'
updated_at: '2023-04-10T20:19:58.933876+00:00'
platforms:
  - AWS
  - Cloud
tags:
  - Enumeration
  - EKS
  - Discovery
verified: true
validated: true
---

# aws-eks-describe-cluster

## Command

```bash
aws eks describe-cluster --name $_CLUSTER_NAME
```

## Description

This command retrieves detailed information about a specified Amazon EKS cluster, including its configuration, status, and networking details. Use it during cloud reconnaissance to gather intelligence on Kubernetes clusters in the target's AWS environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --name $_CLUSTER_NAME | The name of the EKS cluster to describe (e.g., 'prod-cluster-1') | Yes |
| --region | AWS region where the cluster is located (defaults to default region if omitted) | No |
| --output | Output format (json, text, table; defaults to json) | No |

## Examples

### Basic Usage

```bash
aws eks describe-cluster --name my-cluster
```

### Advanced Usage

```bash
aws eks describe-cluster --name my-cluster --region us-west-2 --output json | jq .cluster.version
```

## Expected Output

Successful execution returns a JSON object like:

```json
{
  "cluster": {
    "name": "my-cluster",
    "arn": "arn:aws:eks:us-west-2:123456789012:cluster/my-cluster",
    "createdAt": "2023-01-01T12:00:00Z",
    "version": "1.24",
    "endpoint": "https://1234567890ABCDEF.sk1.us-west-2.eks.amazonaws.com",
    "roleArn": "arn:aws:iam::123456789012:role/eks-cluster-role",
    "resourcesVpcConfig": {
      "subnetIds": ["subnet-123", "subnet-456"],
      "securityGroupIds": ["sg-789"],
      "vpcId": "vpc-abc"
    },
    "status": "ACTIVE"
  }
}
```

Look for the 'endpoint' to identify the Kubernetes API server URL and 'resourcesVpcConfig' for networking details.

## Related

- [[procedures/AWS-EKS-Cluster-Information-Gathering]]
- [[tools/aws-cli]]

---
id: 0f3de123-8947-4971-8197-5d97b5ac7a24
name: describe-eks-nodegroup
type: command
executor: bash
data: >-
  aws eks describe-nodegroup --cluster-name $_CLUSTER_NAME --nodegroup-name
  $_NODEGROUP_NAME
output: null
created_at: '2023-04-06T03:56:12.905817+00:00'
updated_at: '2023-04-10T20:19:59.959559+00:00'
platforms:
  - AWS
tags:
  - cloud
  - eks
  - enumeration
verified: true
validated: true
---

# describe-eks-nodegroup

## Command

```bash
aws eks describe-nodegroup --cluster-name $_CLUSTER_NAME --nodegroup-name $_NODEGROUP_NAME
```

## Description

This command queries the AWS EKS API to retrieve detailed configuration information about a specific node group within an EKS cluster. Use it during cloud discovery to map compute resources and scaling behaviors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cluster-name $_CLUSTER_NAME | The name of the EKS cluster containing the node group (e.g., my-cluster) | Yes |
| --nodegroup-name $_NODEGROUP_NAME | The name of the node group to describe (e.g., my-nodegroup) | Yes |

## Examples

### Basic Usage

```bash
aws eks describe-nodegroup --cluster-name prod-cluster --nodegroup-name worker-nodes
```

### Advanced Usage

```bash
aws eks describe-nodegroup --cluster-name prod-cluster --nodegroup-name worker-nodes --region us-west-2
```

## Expected Output

The command returns a JSON object with node group details. Successful output looks like:

```json
{
  "nodegroup": {
    "nodegroupName": "worker-nodes",
    "nodegroupArn": "arn:aws:eks:us-west-2:123456789012:nodegroup/prod-cluster/worker-nodes/abc123",
    "clusterName": "prod-cluster",
    "version": "1.21",
    "releaseVersion": "1.21.5-eks-12345",
    "createdAt": "2023-01-01T00:00:00Z",
    "modifiedAt": "2023-01-02T00:00:00Z",
    "status": "ACTIVE",
    "capacityType": "ON_DEMAND",
    "scalingConfig": {
      "minSize": 1,
      "maxSize": 10,
      "desiredSize": 3
    },
    "instanceTypes": ["m5.large"],
    "subnets": ["subnet-123", "subnet-456"],
    "remoteAccess": {
      "ec2SshKey": "my-key",
      "sourceSecurityGroups": ["sg-123"]
    },
    "labels": {},
    "resources": {
      "autoScalingGroups": [{"name": "eks-worker-nodes"}],
      "remoteAccessSecurityGroup": "sg-789"
    },
    "health": {
      "issues": []
    }
  }
}
```

Look for fields like scalingConfig to identify misconfigurations and instanceTypes for potential targeting.

## Related

- [[procedures/Enumerate-AWS-EKS-Node-Group-Information]]
- [[tools/aws-cli]]

---
type: command
executor: bash
data: aws ec2 create-route-table --vpc-id $AWS_VPC_ID --region $AWS_REGION
output: null
created_at: '2020-07-31T04:25:33.411321+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - EC2
  - VPC
verified: true
validated: true
---

# aws-ec2-create-route-table

## Command

```bash
aws ec2 create-route-table --vpc-id $AWS_VPC_ID --region $AWS_REGION
```

## Description

Creates a new route table within the specified VPC. Route tables control the routing of traffic for subnets in the VPC, essential for configuring private subnet egress in cloud compromise scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --vpc-id $AWS_VPC_ID | The ID of the VPC (e.g., vpc-0123456789abcdef0) | Yes |
| --region $AWS_REGION | The AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 create-route-table --vpc-id vpc-0123456789abcdef0 --region us-east-1
```

### Advanced Usage

```bash
aws ec2 create-route-table --vpc-id vpc-0123456789abcdef0 --region us-east-1 --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=PrivateRTB}]'
```

## Expected Output

```
{
    "RouteTable": {
        "Associations": [],
        "PropagatingVgws": [],
        "RouteTableId": "rtb-049dfbcf8a8801f9e",
        "VpcId": "vpc-0123456789abcdef0",
        "OwnerId": "123456789012",
        "Tags": [],
        "Routes": []
    }
}
```

## Related

- [[procedures/Configure-Private-Subnet-Route-to-NAT-Gateway]]
- [[tools/aws-cli]]

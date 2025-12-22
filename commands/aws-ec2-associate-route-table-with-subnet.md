---
type: command
executor: bash
data: >-
  aws ec2 associate-route-table --route-table-id $AWS_ROUTE_TABLE_ID --subnet-id
  $AWS_SUBNET_ID --region $AWS_REGION
output: null
created_at: '2020-07-31T04:25:16.594834+00:00'
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

# aws-ec2-associate-route-table-with-subnet

## Command

```bash
aws ec2 associate-route-table --route-table-id $AWS_ROUTE_TABLE_ID --subnet-id $AWS_SUBNET_ID --region $AWS_REGION
```

## Description

Associates a route table with a subnet, applying its routing rules to all instances in that subnet. This is key for directing private subnet traffic through a NAT Gateway.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --route-table-id $AWS_ROUTE_TABLE_ID | The ID of the route table (e.g., rtb-049dfbcf8a8801f9e) | Yes |
| --subnet-id $AWS_SUBNET_ID | The ID of the subnet (e.g., subnet-0123456789abcdef0) | Yes |
| --region $AWS_REGION | The AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 associate-route-table --route-table-id rtb-049dfbcf8a8801f9e --subnet-id subnet-0123456789abcdef0 --region us-east-1
```

### Advanced Usage

Subnets can only have one explicit association; this replaces any existing one.

## Expected Output

```
{
    "AssociationId": "rtbassoc-0123456789abcdef0"
}
```

## Related

- [[procedures/Configure-Private-Subnet-Route-to-NAT-Gateway]]
- [[tools/aws-cli]]

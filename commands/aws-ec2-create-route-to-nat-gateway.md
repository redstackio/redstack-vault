---
type: command
executor: bash
data: >-
  aws ec2 create-route --route-table-id $AWS_ROUTE_TABLE_ID
  --destination-cidr-block 0.0.0.0/0 --nat-gateway-id $AWS_NAT_GATEWAY_ID
  --region $AWS_REGION
output: null
created_at: '2020-07-31T04:25:33.411337+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - EC2
  - VPC
  - NAT
verified: true
validated: true
---

# aws-ec2-create-route-to-nat-gateway

## Command

```bash
aws ec2 create-route --route-table-id $AWS_ROUTE_TABLE_ID --destination-cidr-block 0.0.0.0/0 --nat-gateway-id $AWS_NAT_GATEWAY_ID --region $AWS_REGION
```

## Description

Adds a route to an existing route table, directing traffic for a specified CIDR block (typically 0.0.0.0/0 for internet) to a NAT Gateway. This enables outbound connectivity from private subnets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --route-table-id $AWS_ROUTE_TABLE_ID | The ID of the route table (e.g., rtb-049dfbcf8a8801f9e) | Yes |
| --destination-cidr-block 0.0.0.0/0 | The CIDR block for the route (0.0.0.0/0 for all IPv4 traffic) | Yes |
| --nat-gateway-id $AWS_NAT_GATEWAY_ID | The ID of the NAT Gateway (e.g., nat-0123456789abcdef0) | Yes |
| --region $AWS_REGION | The AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 create-route --route-table-id rtb-049dfbcf8a8801f9e --destination-cidr-block 0.0.0.0/0 --nat-gateway-id nat-0123456789abcdef0 --region us-east-1
```

### Advanced Usage

```bash
aws ec2 create-route --route-table-id rtb-049dfbcf8a8801f9e --destination-cidr-block 0.0.0.0/0 --nat-gateway-id nat-0123456789abcdef0 --region us-east-1 --tag-specifications 'ResourceType=route,Tags=[{Key=Name,Value=InternetToNAT}]'
```

## Expected Output

```
{
    "Return": true
}
```

## Related

- [[procedures/Configure-Private-Subnet-Route-to-NAT-Gateway]]
- [[tools/aws-cli]]

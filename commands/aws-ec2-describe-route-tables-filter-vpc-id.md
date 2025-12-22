---
id: 8a156017-6780-466d-9318-051b40382642
name: aws-ec2-describe-route-tables-filter-vpc-id
type: command
executor: bash
data: >-
  aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID" --region
  $_REGION
output: null
created_at: '2023-04-06T03:56:14.381389+00:00'
updated_at: '2023-04-10T20:20:11.855189+00:00'
platforms:
  - AWS
tags:
  - Enumeration
  - AWS-EC2
verified: true
validated: true
---

# aws-ec2-describe-route-tables-filter-vpc-id

## Command

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID" --region $_REGION
```

## Description

This AWS CLI command queries the EC2 service to retrieve details about all route tables associated with a specific VPC ID. It is used in cloud discovery phases to map network routing configurations, identifying how subnets route traffic to gateways, peers, or the internet. Run this after obtaining a VPC ID to avoid broad queries that could trigger alerts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VPC_ID | The ID of the VPC to filter route tables for (format: vpc-xxxxxxxx) | Yes |
| --filters "Name=vpc-id,Values=$_VPC_ID" | Filter clause to limit results to the specified VPC; uses Name= for attribute and Values= for the ID | Yes |
| --region $_REGION | AWS region to query (e.g., us-east-1); defaults to configured region if omitted | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-0a1b2c3d4e5f67890" --region us-east-1
```

### Advanced Usage

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID" --output table --query 'RouteTables[*].[RouteTableId,Associations[*].SubnetId]'
```

> This variant uses --output table for readable format and --query to select specific fields like table ID and subnet associations.

## Expected Output

The command returns a JSON object with a "RouteTables" array. Each entry includes RouteTableId, VpcId, Associations (with SubnetId and Main flag), and Routes (with DestinationCidrBlock, GatewayId, NatGatewayId, etc.).

Sample output:

```json
{
    "RouteTables": [
        {
            "Associations": [
                {
                    "Main": true,
                    "RouteTableAssociationId": "rtbassoc-12345678",
                    "RouteTableId": "rtb-12345678",
                    "SubnetId": "subnet-12345678"
                }
            ],
            "PropagatingVgws": [],
            "RouteTableId": "rtb-12345678",
            "Routes": [
                {
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "GatewayId": "igw-12345678",
                    "Origin": "CreateRoute",
                    "State": "active"
                }
            ],
            "VpcId": "vpc-0a1b2c3d4e5f67890"
        }
    ]
}
```

Success is a non-empty RouteTables array; errors include "UnauthorizedOperation" if permissions are insufficient.

## Related

- [[procedures/Enumerate-EC2-Route-Tables-by-VPC-ID]]
- [[tools/AWS-CLI]]

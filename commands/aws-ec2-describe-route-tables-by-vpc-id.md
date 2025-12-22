---
id: 9f0b3e32-a81b-4c86-a0a1-19352cc2b063
name: aws-ec2-describe-route-tables-by-vpc-id
type: command
executor: bash
data: 'aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID"'
output: null
created_at: '2023-04-06T03:56:14.480455+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - route-tables
  - discovery
verified: true
validated: true
---

# aws-ec2-describe-route-tables-by-vpc-id

## Command

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID"
```

## Description

This AWS CLI command retrieves detailed information about all route tables associated with a specific VPC, including routes, associations, and propagations. It is used in cloud reconnaissance to map network paths and identify internal resources like RDS instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--filters` | Filter results by attributes like vpc-id | Yes |
| `Name=vpc-id,Values=$_VPC_ID` | Specifies the VPC ID to query (e.g., vpc-12345678) | Yes |
| `$_VPC_ID` | Placeholder for the actual VPC identifier | Yes |

## Examples

### Basic Usage

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-12345678"
```

### With Output Formatting

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID" --query "RouteTables[].Routes[].DestinationCidrBlock" --output table
```

## Expected Output

```
{
    "RouteTables": [
        {
            "Associations": [...],
            "PropagatingVgws": [],
            "RouteTableId": "rtb-12345678",
            "Routes": [
                {
                    "DestinationCidrBlock": "10.0.0.0/16",
                    "GatewayId": "local",
                    "Origin": "Local",
                    "State": "active"
                },
                {
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "GatewayId": "igw-12345678",
                    "Origin": "Manual",
                    "State": "active"
                }
            ],
            "Tags": [],
            "VpcId": "vpc-12345678"
        }
    ]
}
```

Success is indicated by a JSON array of RouteTables with active routes pointing to internal CIDRs or instances.

## Related

- [[procedures/RDS-Lateral-Movement-via-EC2-Route-Tables]]
- [[tools/AWS-CLI]]

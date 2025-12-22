---
type: command
executor: bash
data: aws rds describe-db-instances --region $_AWS_REGION
tags:
  - aws
  - rds
  - discovery
platforms:
  - AWS
verified: true
validated: true
---

# aws-rds-describe-db-instances

## Command

```bash
aws rds describe-db-instances --region $_AWS_REGION
```

## Description

This command queries the AWS RDS service to list all DB instances in the specified region, providing details like instance identifiers, engine types, and network configurations (e.g., subnet groups linking to VPCs). Use it during cloud reconnaissance to map database resources and their isolation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region to query (e.g., us-east-1) | Yes |
| `$_AWS_REGION` | Placeholder for the region value | Yes |

## Examples

### Basic Usage

```bash
aws rds describe-db-instances --region us-east-1
```

### Advanced Usage

```bash
aws rds describe-db-instances --region us-east-1 --db-instance-identifier mydbinstance --query 'DBInstances[0].DBSubnetGroup'
```

(Uses --query to filter for subnet group info relevant to VPCs.)

## Expected Output

```
{
    "DBInstances": [
        {
            "DBInstanceIdentifier": "mydbinstance",
            "Engine": "postgres",
            "DBInstanceStatus": "available",
            "DBSubnetGroup": {
                "DBSubnetGroupName": "default-vpc-123",
                "SubnetGroupStatus": "Complete",
                "Subnets": [
                    {
                        "SubnetIdentifier": "subnet-abc123",
                        "SubnetAvailabilityZone": {
                            "Name": "us-east-1a"
                        },
                        "SubnetStatus": "Available"
                    }
                ],
                "VpcId": "vpc-12345678"
            }
        }
    ]
}
```

Success is indicated by a non-empty "DBInstances" array with VPC-related fields like "VpcId" in DBSubnetGroup.

## Related

- [[procedures/Enumerate-AWS-RDS-VPCs]]
- [[commands/aws-ec2-describe-vpcs-by-id]]

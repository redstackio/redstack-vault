---
id: ccc1858e-d69d-412b-b6de-72e7f52d281f
name: aws-rds-describe-db-subnet-groups
type: command
executor: bash
data: aws rds describe-db-subnet-groups --region $_AWS_REGION
output: null
created_at: '2023-04-06T03:56:13.898127+00:00'
updated_at: '2023-04-10T20:20:39.647653+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - aws
  - rds
verified: true
validated: true
---

# AWS RDS Describe DB Subnet Groups

## Command

```bash
aws rds describe-db-subnet-groups --region $_AWS_REGION
```

## Description

This command retrieves detailed information about all DB subnet groups in the specified AWS region for Amazon RDS. It is used during cloud reconnaissance to map database networking configurations, including VPC associations and individual subnets, helping identify potential targets for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region $_AWS_REGION | The AWS region to query (e.g., us-east-1, eu-west-1). If omitted, uses the default region from AWS config. | No |
| DBSubnetGroupName (optional) | Name of a specific subnet group to describe. Omit for all groups. | No |

## Examples

### Basic Usage

```bash
aws rds describe-db-subnet-groups --region us-east-1
```

### Advanced Usage (Specific Group)

```bash
aws rds describe-db-subnet-groups --db-subnet-group-name my-subnet-group --region us-east-1
```

## Expected Output

Successful execution returns a JSON object with DB subnet group details:

```json
{
  "DBSubnetGroups": [
    {
      "DBSubnetGroupName": "default-vpc-12345678",
      "DBSubnetGroupDescription": "default VPC subnet group",
      "VpcId": "vpc-12345678",
      "SubnetGroupStatus": "Complete",
      "Subnets": [
        {
          "SubnetIdentifier": "subnet-12345678",
          "SubnetAvailabilityZone": {
            "Name": "us-east-1a"
          },
          "SubnetStatus": "Active"
        }
      ]
    }
  ]
}
```

Look for VpcId and Subnets arrays to extract network identifiers. Errors like "AccessDenied" indicate permission issues.

## Related

- [[procedures/rds-subnet-group-enumeration]]
- [[tools/aws-cli]]

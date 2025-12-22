---
id: ee316314-8a47-420b-823f-909a486281a9
name: aws-ec2-describe-subnets
type: command
executor: bash
data: aws ec2 describe-subnets
output: null
created_at: '2023-04-06T03:56:14.298774+00:00'
updated_at: '2023-04-10T20:20:22.899114+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - cloud
verified: true
validated: true
---

# AWS EC2 Describe Subnets

## Command

```bash
aws ec2 describe-subnets $_FILTERS $_VPC_IDS $_SUBNET_IDS
```

## Description

This command queries the AWS EC2 API to retrieve detailed information about subnets in one or more VPCs. It is used for enumerating network segments, including those hosting RDS instances, to map cloud infrastructure during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILTERS | Filters for specific criteria, e.g., `--filters "Name=tag:Name,Values=RDS*"` to match RDS-tagged subnets | No |
| $_VPC_IDS | Limit to specific VPCs, e.g., `--vpc-ids vpc-12345` | No |
| $_SUBNET_IDS | Limit to specific subnets, e.g., `--subnet-ids subnet-abc` | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-subnets
```

Retrieves all subnets in the default region.

### Advanced Usage

```bash
aws ec2 describe-subnets --filters "Name=tag:Name,Values=*RDS*" --output json | jq '.Subnets[] | {SubnetId, CidrBlock}'
```

Filters for RDS-related subnets and formats output.

## Expected Output

JSON structure with subnet details:

```json
{
  "Subnets": [
    {
      "SubnetId": "subnet-0123456789abcdef0",
      "VpcId": "vpc-0123456789abcdef0",
      "CidrBlock": "10.0.1.0/24",
      "AvailabilityZone": "us-east-1a",
      "Tags": [
        {
          "Key": "Name",
          "Value": "RDS-Private-Subnet"
        }
      ]
    }
  ]
}
```

Success is indicated by a non-empty Subnets array without permission errors.

## Related

- [[procedures/enumerate-rds-subnets-via-ec2-describe-subnets]]
- [[tools/aws-cli]]

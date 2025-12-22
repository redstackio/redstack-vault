---
id: d94cf57e-862a-4b89-8eb2-5a5ee2c480e0
name: aws-ec2-describe-subnets-by-vpc-id
type: command
executor: bash
data: 'aws ec2 describe-subnets --filters "Name=vpc-id,Values=$_VPC_ID"'
output: null
created_at: '2023-04-06T03:56:14.455557+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - aws
  - ec2
verified: true
validated: true
---

# aws-ec2-describe-subnets-by-vpc-id

## Command

```bash
aws ec2 describe-subnets --filters "Name=vpc-id,Values=$_VPC_ID"
```

## Description

This command queries the AWS EC2 API to list all subnets associated with a specific VPC ID. It is used during cloud reconnaissance to map network infrastructure, identifying segments that may contain targets like RDS databases. Requires AWS CLI v2 and appropriate IAM permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VPC_ID | The VPC identifier to filter subnets by (e.g., vpc-0a1b2c3d4e5f67890) | Yes |
| --filters | Specifies the filter criteria; here, Name=vpc-id,Values=$_VPC_ID to target a single VPC | Yes |

## Examples

### Basic Usage

```bash
aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-12345678"
```

### Advanced Usage

```bash
aws ec2 describe-subnets --filters "Name=vpc-id,Values=$_VPC_ID" --query "Subnets[*].[SubnetId,CidrBlock,AvailabilityZone,MapPublicIpOnLaunch]" --output table
```

> This variant uses --query to extract specific fields and --output table for readable formatting.

## Expected Output

Successful execution returns a JSON array of subnet objects. Example:

```json
{
    "Subnets": [
        {
            "SubnetId": "subnet-abcdef01",
            "AvailabilityZone": "us-east-1a",
            "CidrBlock": "10.0.1.0/24",
            "MapPublicIpOnLaunch": false,
            "State": "available"
        }
    ]
}
```

Look for "State": "available" and private CIDR blocks as indicators of potential internal resources. Errors like "UnauthorizedOperation" indicate insufficient permissions.

## Related

- [[procedures/Enumerate-AWS-Subnets-by-VPC-ID]]
- [[tools/AWS-CLI]]

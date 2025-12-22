---
id: e1cabcf7-45cd-4a33-8a48-14bb0a2c8bca
name: aws-ec2-describe-vpcs-us-west-1
type: command
executor: bash
data: aws ec2 describe-vpcs --region us-west-1
output: null
created_at: '2023-04-06T03:56:14.252494+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - aws
  - vpc
verified: true
validated: true
---

# AWS EC2 Describe VPCs us-west-1

## Command

```bash
aws ec2 describe-vpcs --region us-west-1
```

## Description

This command queries the AWS EC2 API to retrieve details about all Virtual Private Clouds (VPCs) in the us-west-1 region. It is used during cloud reconnaissance to map network infrastructure, identify potential RDS hosting environments, and discover CIDR blocks for further targeting. Requires AWS CLI v2 and valid credentials with EC2 read permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region us-west-1` | Specifies the AWS region (Oregon) for the query; fixed for this command | Yes |
| (Implicit) AWS credentials | Access key and secret for authentication; sourced from environment, profile, or ~/.aws/config | Yes |

## Examples

### Basic Usage

```bash
aws ec2 describe-vpcs --region us-west-1
```

### Advanced Usage (with output formatting)

```bash
aws ec2 describe-vpcs --region us-west-1 --output table --query 'Vpcs[*].[VpcId,CidrBlock,State]'
```

## Expected Output

Successful execution returns a JSON structure like:

```json
{
    "Vpcs": [
        {
            "CidrBlock": "172.31.0.0/16",
            "DhcpOptionsId": "dopt-12345678",
            "State": "available",
            "VpcId": "vpc-abcdef12",
            "OwnerId": "123456789012",
            "InstanceTenancy": "default",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "default-vpc"
                }
            ]
        }
    ]
}
```

If no VPCs exist, "Vpcs" is an empty array. Errors include InvalidInstanceID.NotFound for permission issues.

## Related

- [[procedures/enumerate-vpcs-in-aws-us-west-1-region]]
- [[tools/AWS-CLI]]

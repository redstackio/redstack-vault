---
id: 2ccd1fa6-61a7-4ca1-9aac-82c2e74cb29a
name: aws-ec2-create-vpc
type: command
executor: bash
data: aws ec2 create-vpc --cidr-block $_CIDR_BLOCK --region $_REGION
output: null
created_at: '2020-07-31T04:25:22.966125+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - aws
  - vpc
  - creation
verified: true
validated: true
---

# aws-ec2-create-vpc

## Command

```bash
aws ec2 create-vpc --cidr-block $_CIDR_BLOCK --region $_REGION
```

## Description

This command creates a new Virtual Private Cloud (VPC) in the specified AWS region with the given CIDR block. Use this to provision isolated network environments, particularly in alternate regions for evasion purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CIDR_BLOCK | The IPv4 CIDR block for the VPC (e.g., 10.0.0.0/16) | Yes |
| $_REGION | The AWS region to create the VPC in (e.g., eu-west-1) | Yes |
| --cidr-block | Specifies the CIDR block | Built-in |
| --region | Targets the specific AWS region | Built-in |

## Examples

### Basic Usage

```bash
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --region eu-west-1
```

### Advanced Usage

```bash
aws ec2 create-vpc --cidr-block 172.16.0.0/16 --region ap-southeast-2 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=HiddenVPC}]'
```

## Expected Output

```
{
    "Vpc": {
        "CidrBlock": "10.0.0.0/16",
        "DhcpOptionsId": "dopt-12345678",
        "State": "available",
        "VpcId": "vpc-0abcdef1234567890",
        "OwnerId": "123456789012",
        "InstanceTenancy": "default",
        "Ipv6CidrBlockAssociationSet": [],
        "CidrBlockAssociationSet": [
            {
                "AssociationId": "vpc-cidr-assoc-12345678",
                "CidrBlock": "10.0.0.0/16",
                "CidrBlockState": {
                    "State": "associated"
                }
            }
        ],
        "IsDefault": false
    }
}
```

## Related

- [[procedures/Create-AWS-VPC-in-Alternate-Region-for-Resource-Hiding]]
- [[commands/aws-ec2-modify-vpc-dns-hostnames]]

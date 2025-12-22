---
id: 84d4be8c-dde8-43cc-b320-6ee940054f9c
name: aws-ec2-modify-vpc-dns-hostnames
type: command
executor: bash
data: >-
  aws ec2 modify-vpc-attribute --vpc-id $_VPC_ID --enable-dns-hostnames
  "{\"Value\":$_ENABLE_VALUE}" --region $_REGION
output: null
created_at: '2020-07-31T04:25:22.966322+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - aws
  - vpc
  - dns
verified: true
validated: true
---

# aws-ec2-modify-vpc-dns-hostnames

## Command

```bash
aws ec2 modify-vpc-attribute --vpc-id $_VPC_ID --enable-dns-hostnames "{\"Value\":$_ENABLE_VALUE}" --region $_REGION
```

## Description

This command modifies a VPC attribute to enable or disable DNS hostnames, allowing instances to resolve to their private DNS hostnames. Useful for configuring internal networking in hidden VPCs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VPC_ID | The ID of the VPC to modify (e.g., vpc-12345678) | Yes |
| $_ENABLE_VALUE | Boolean value as string (true or false) | Yes |
| $_REGION | The AWS region of the VPC | Yes |
| --vpc-id | Specifies the VPC ID | Built-in |
| --enable-dns-hostnames | Sets the DNS hostnames attribute | Built-in |
| --region | Targets the specific AWS region | Built-in |

## Examples

### Basic Usage

```bash
aws ec2 modify-vpc-attribute --vpc-id vpc-12345678 --enable-dns-hostnames "{\"Value\":true}" --region eu-west-1
```

### Advanced Usage

```bash
aws ec2 modify-vpc-attribute --vpc-id vpc-12345678 --enable-dns-support "{\"Value\":true}" --region eu-west-1
```

## Expected Output

```
{
    "Return": true
}
```

## Related

- [[procedures/Create-AWS-VPC-in-Alternate-Region-for-Resource-Hiding]]
- [[commands/aws-ec2-create-vpc]]
